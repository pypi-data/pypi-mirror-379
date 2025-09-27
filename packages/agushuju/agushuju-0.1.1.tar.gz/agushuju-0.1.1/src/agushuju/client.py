import os
import requests
import pandas as pd
from typing import Any, Dict, List, Optional


DEFAULT_BASE_URL = os.getenv("AGU_BASE_URL", "https://www.agushuju.com/api").rstrip("/")


class _AguProClient:
    def __init__(self, token: Optional[str] = None, base_url: Optional[str] = None):
        self.token = token or os.getenv("AGU_TOKEN") or ""
        self.base_url = (base_url or DEFAULT_BASE_URL).rstrip("/")

    def _call_endpoint(self, endpoint: str, request: Optional[Dict[str, Any]] = None, response: Optional[List[str]] = None) -> pd.DataFrame:
        query: Dict[str, Any] = {}
        if request is not None:
            query.update({k: v for k, v in request.items() if v is not None})

        fields_list: Optional[List[str]] = response
        if fields_list:
            query["fields"] = ",".join(fields_list)

        url = f"{self.base_url}/{endpoint}"
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        resp = requests.get(url, params=query, headers=headers, timeout=30)
        resp.raise_for_status()
        payload = resp.json()
        if not isinstance(payload, dict) or payload.get("code") != 0:
            raise RuntimeError(f"API error: {payload}")

        data = payload.get("data") or []
        df = pd.DataFrame(data)

        if fields_list:
            existing_cols = [c for c in fields_list if c in df.columns]
            if existing_cols:
                df = df.loc[:, existing_cols]

        return df

    def __getattr__(self, name: str):
        def _endpoint_method(*, request: Optional[Dict[str, Any]] = None, response: Optional[List[str]] = None) -> pd.DataFrame:
            return self._call_endpoint(name, request=request, response=response)
        return _endpoint_method

    def stock_basic(self, request: Optional[Dict[str, Any]] = None, response: Optional[List[str]] = None) -> pd.DataFrame:
        return self._call_endpoint("stock_basic", request=request, response=response)


def api(token: Optional[str] = None, base_url: Optional[str] = None) -> _AguProClient:
    return _AguProClient(token=token, base_url=base_url)


