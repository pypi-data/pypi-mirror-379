"""
Gedys ETL Extract Module.

This module handles the extraction phase of the Gedys ETL pipeline.
It provides functionality to extract data from Gedys systems and
prepare it for the transformation phase.

The extraction process:
1. Connects to the Gedys system using configured credentials
2. Iterates through configured tables and extracts data
3. Handles inactive tables by skipping them
4. Uses ETLFileHandler for data persistence
5. Provides comprehensive logging throughout the process

Classes:
    GedysExtract: Main class handling Gedys data extraction.
"""

import json
from pathlib import Path
from typing import List
from prefect import get_run_logger
import requests
from nemo_library_etl.adapter._utils.db_handler import ETLDuckDBHandler, NDJSONRotation
from nemo_library_etl.adapter._utils.enums import ETLAdapter, ETLStep
from nemo_library_etl.adapter.gedys.config_models import PipelineGedys
from nemo_library_etl.adapter._utils.file_handler import ETLFileHandler
from nemo_library.core import NemoLibrary


class GedysExtract:
    """
    Handles extraction of data from Gedys system.

    This class manages the extraction phase of the Gedys ETL pipeline,
    providing methods to connect to Gedys systems, retrieve data,
    and prepare it for subsequent transformation and loading phases.

    The extractor:
    - Uses NemoLibrary for core functionality and configuration
    - Integrates with Prefect logging for pipeline visibility
    - Processes tables based on configuration settings
    - Handles both active and inactive table configurations
    - Leverages ETLFileHandler for data persistence

    Attributes:
        nl (NemoLibrary): Core Nemo library instance for system integration.
        config: Configuration object from the Nemo library.
        logger: Prefect logger for pipeline execution tracking.
        cfg (PipelineGedys): Pipeline configuration with extraction settings.
    """

    def __init__(self, cfg: PipelineGedys):
        """
        Initialize the GedysExtract instance.

        Sets up the extractor with the necessary library instances, configuration,
        and logging capabilities for the extraction process.

        Args:
            cfg (PipelineGedys): Pipeline configuration object containing
                                                         extraction settings including table
                                                         configurations and activation flags.
        """
        self.nl = NemoLibrary()
        self.config = self.nl.config
        self.logger = get_run_logger()
        self.cfg = cfg
        self.gedys_token = self._get_token()

        super().__init__()

    def extract(self) -> None:
        """
        Extract Gedys objects into NDJSON (rotated, gzipped) and ingest into DuckDB.
        """
        self.logger.info("Extracting all Gedys objects")

        # --- DuckDB: choose a persistent DB file (adapt path to your environment)
        # Suggestion: keep a single warehouse DB per adapter
        db = ETLDuckDBHandler(adapter=ETLAdapter.GEDYS)

        # --- NDJSON rotation/gzip settings (tweak to your scale)
        # Rotate after N records per file; gzip keeps files small
        rotation = NDJSONRotation(
            rotate_every_n=self.cfg.file_chunksize,
            rotate_max_bytes=None,
            suffix_template="{stem}.{part:05d}.ndjson",  # yields e.g. table.00001.ndjson[.gz]
        )
        gzip_enabled = self.cfg.gzip_enabled

        # Use a Session for connection pooling
        with requests.Session() as session:
            headers = {"Authorization": f"Bearer {self.gedys_token}"}

            for table, model in self.cfg.extract.tables.items():
                if model.active is False:
                    self.logger.info(f"Skipping inactive table: {table}")
                    continue

                self.logger.info(f"Extracting table: {table}")

                take = self.cfg.chunksize
                skip = 0
                total_count_reported = None
                total_written = 0

                # --- Write NDJSON stream (rotating, gz) into the same ETL directory layout
                #     We keep step=EXTRACT and use substep="raw" to separate raw dumps from curated outputs.
                with db.streamNDJSON(
                    adapter=ETLAdapter.GEDYS,
                    step=ETLStep.EXTRACT,
                    entity=table,
                    gzip_enabled=gzip_enabled,
                    substep="raw",
                    rotation=rotation,
                ) as writer:

                    while True:
                        body = {"Skip": skip, "Take": take}
                        params = {
                            "includeRecordHistory": getattr(model, "history", False)
                        }

                        resp = session.post(
                            f"{self.cfg.URL}/rest/v1/records/list/{model.GUID}",
                            headers=headers,
                            json=body,
                            params=params,
                            timeout=60,
                        )

                        if resp.status_code != 200:
                            raise Exception(
                                f"request failed. Status: {resp.status_code}, "
                                f"error: {resp.text}, entity: {table}"
                            )

                        result = resp.json()
                        data = result.get("Data", []) or []
                        total_count = result.get("TotalCount", 0)
                        return_count = result.get("ReturnCount", len(data))

                        # Stream this page immediately to NDJSON (one record per line)
                        if data:
                            writer.write_many(data)
                            total_written += len(data)

                        # First page: remember advertised total for logging
                        if total_count_reported is None:
                            total_count_reported = total_count

                        self.logger.info(
                            f"Received {return_count:,} records out of {total_count:,} "
                            f"(Skip: {skip:,}). Written so far: {total_written:,}."
                        )

                        skip += return_count
                        if (
                            return_count == 0
                            or skip >= total_count
                            or (
                                getattr(self.cfg, "maxrecords", None)
                                and total_written >= self.cfg.maxrecords
                            )
                        ):
                            break

                # --- Ingest all rotated parts for this table into DuckDB
                #     We look up the exact directory where streamNDJSON wrote the files.
                raw_dir = db._base_dir(ETLAdapter.GEDYS, ETLStep.EXTRACT, "raw")
                stem = writer.current_path.stem.replace(".ndjson", "").replace(
                    ".ndjson.gz", ""
                )
                # Collect both gz and plain files in case gzip was toggled
                patterns: List[str] = [f"{stem}.*.ndjson", f"{stem}.*.ndjson.gz"]
                ndjson_parts: List[Path] = []
                for pat in patterns:
                    ndjson_parts.extend(sorted(raw_dir.glob(pat)))

                if not ndjson_parts:
                    # Fallback: single-file case (no rotation)
                    single_candidates = [f"{stem}.ndjson", f"{stem}.ndjson.gz"]
                    for c in single_candidates:
                        p = raw_dir / c
                        if p.exists():
                            ndjson_parts.append(p)

                if not ndjson_parts:
                    self.logger.warning(
                        f"No NDJSON files found for {table} in {raw_dir}. Skipping ingest."
                    )
                else:
                    # Choose a stable DuckDB table name per source table
                    duckdb_table = f"{table}_raw"
                    db.ingest_ndjson(
                        table=duckdb_table,
                        ndjson_paths=[str(p) for p in ndjson_parts],
                        create_table=True,
                        replace_table=False,  # appends if table already exists
                        sampling_rows=100_000,  # tune if schema inference needs more rows
                    )
                    self.logger.info(
                        f"Finished {table}: wrote {total_written:,} records to NDJSON "
                        f"and ingested into DuckDB table '{duckdb_table}'."
                    )

    def _get_token(self) -> str:
        data = {
            "username": self.config.get_gedys_user_id(),
            "password": self.config.get_gedys_password(),
        }
        response_auth = requests.post(
            f"{self.cfg.URL}/api/auth/login",
            data=data,
        )
        if response_auth.status_code != 200:
            raise Exception(
                f"request failed. Status: {response_auth.status_code}, error: {response_auth.text}"
            )
        token = json.loads(response_auth.text)
        return token["token"]
