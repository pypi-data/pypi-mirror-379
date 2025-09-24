import requests
from typing import Optional, Tuple

class AbionClient:
    def __init__(self, api_key: str, base_url: str = "https://api.abion.com/"):
        if not base_url.endswith("/"):
            base_url += "/"
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"X-API-KEY": api_key, "Content-Type": "application/json"})

    def _url(self, path: str) -> str:
        if path.startswith("/"):
            path = path[1:]
        return f"{self.base_url}{path}"

    def get_zone(self, name: str) -> Optional[dict]:
        # GET /v1/zones/{name}
        resp = self.session.get(self._url(f"v1/zones/{name}"))
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code in (401, 403):
            raise RuntimeError(f"Abion auth failed: HTTP {resp.status_code}")
        if resp.status_code == 404:
            return None
        raise RuntimeError(f"Abion get_zone failed: HTTP {resp.status_code} - {resp.text}")

    def patch_zone_records(self, zone: str, payload: dict) -> dict:
        # PATCH /v1/zones/{name}
        resp = self.session.patch(self._url(f"v1/zones/{zone}"), json=payload)
        if resp.status_code in (200, 202):
            return resp.json()
        raise RuntimeError(f"Abion patch_zone_records failed: HTTP {resp.status_code} - {resp.text}")
