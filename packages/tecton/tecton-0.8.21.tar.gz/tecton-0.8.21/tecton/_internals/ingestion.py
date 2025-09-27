from datetime import datetime
from typing import Any
from typing import Dict
from typing import Tuple
from urllib.parse import urljoin

import requests

from tecton._internals import errors
from tecton_core import conf


class IngestionClient:
    def __init__(self):
        preview_domain = conf.get_or_raise("FEATURE_SERVICE")
        preview_domain = preview_domain.replace("https://", "https://preview.")
        if preview_domain.endswith("/"):
            preview_domain = preview_domain[:-1]
        if preview_domain.endswith("/api"):
            preview_domain = preview_domain[:-4]
        self.ingestion_url: str = urljoin(preview_domain + "/", "ingest")
        self.session = requests.Session()
        self.session.headers.update(self._prepare_headers())

    def ingest(
        self, workspace_name: str, push_source_name: str, ingestion_record: Dict[str, Any], dry_run: bool = False
    ) -> Tuple[int, str, Dict[str, Any]]:
        http_request = {
            "workspace_name": workspace_name,
            "dry_run": dry_run,
            "records": {
                push_source_name: [
                    {
                        "record": self._serialize_record(ingestion_record),
                    }
                ]
            },
        }
        response = self.session.post(self.ingestion_url, json=http_request)
        return response.status_code, response.reason, response.json()

    @staticmethod
    def _prepare_headers() -> Dict[str, str]:
        token = conf.get_or_none("TECTON_API_KEY")
        if not token:
            raise errors.FS_API_KEY_MISSING

        return {
            "authorization": f"Tecton-key {token}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def _serialize_record(record: Dict[str, Any]) -> Dict[str, Any]:
        serialized_record = {}
        for k, v in record.items():
            if isinstance(v, datetime):
                serialized_record[k] = v.isoformat()
            else:
                serialized_record[k] = v
        return serialized_record
