import requests


class AbionClient:
    """Simple client for the Abion DNS API."""

    def __init__(self, api_key: str, api_url: str = "https://api.abion.com/") -> None:
        self.api_key = api_key
        self.api_url = api_url.rstrip("/")

    def _headers(self) -> dict[str, str]:
        return {
            "X-Api-Key": self.api_key,
            "Content-Type": "application/json",
        }

    def add_txt_record(self, domain: str, name: str, value: str) -> None:
        """Create a TXT record via Abion API."""
        url = f"{self.api_url}/dns/{domain}/records"
        payload = {
            "type": "TXT",
            "name": name,
            "content": value,
            "ttl": 60,
        }
        resp = requests.post(url, headers=self._headers(), json=payload, timeout=30)
        if resp.status_code not in (200, 201):
            raise Exception(f"Failed to add TXT record: {resp.status_code} {resp.text}")

    def del_txt_record(self, domain: str, name: str, value: str) -> None:
        """Delete a TXT record via Abion API."""
        # Hypothèse: suppression par type+name+content (à adapter selon Swagger exact)
        url = f"{self.api_url}/dns/{domain}/records"
        payload = {
            "type": "TXT",
            "name": name,
            "content": value,
        }
        resp = requests.delete(url, headers=self._headers(), json=payload, timeout=30)
        if resp.status_code not in (200, 204):
            raise Exception(f"Failed to delete TXT record: {resp.status_code} {resp.text}")
