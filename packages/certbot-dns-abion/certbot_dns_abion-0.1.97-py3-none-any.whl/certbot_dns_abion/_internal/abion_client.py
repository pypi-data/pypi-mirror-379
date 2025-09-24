import logging
import requests

logger = logging.getLogger(__name__)


class AbionClient:
    """Client for Abion DNS API (v1)."""

    def __init__(self, api_key: str, api_url: str = "https://api.abion.com/") -> None:
        self.api_key = api_key
        self.api_url = api_url.rstrip("/")

    def _headers(self) -> dict[str, str]:
        return {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json",
        }

    def add_txt_record(self, domain: str, validation_name: str, validation: str) -> None:
        zone = self._get_zone_from_domain(domain)
        record_name = self._relative_record_name(zone, validation_name)

        url = f"{self.api_url}/v1/zones/{zone}"
        payload = {
            "data": {
                "type": "zone",
                "id": zone,
                "attributes": {
                    "records": {
                        record_name: {
                            "TXT": [{"rdata": validation}]
                        }
                    }
                }
            }
        }

        logger.debug("Adding TXT record")
        logger.debug("URL: %s", url)
        logger.debug("Headers: %s", self._headers())
        logger.debug("Payload: %s", payload)

        resp = requests.patch(url, headers=self._headers(), json=payload, timeout=30)

        logger.debug("Response status: %s", resp.status_code)
        logger.debug("Response body: %s", resp.text)

        if resp.status_code != 200:
            raise Exception(f"Failed to add TXT record: {resp.status_code} {resp.text}")

    def del_txt_record(self, domain: str, validation_name: str, validation: str) -> None:
        zone = self._get_zone_from_domain(domain)
        record_name = self._relative_record_name(zone, validation_name)

        url = f"{self.api_url}/v1/zones/{zone}"
        payload = {
            "data": {
                "type": "zone",
                "id": zone,
                "attributes": {
                    "records": {
                        record_name: {
                            "TXT": None
                        }
                    }
                }
            }
        }

        logger.debug("Deleting TXT record")
        logger.debug("URL: %s", url)
        logger.debug("Headers: %s", self._headers())
        logger.debug("Payload: %s", payload)

        resp = requests.patch(url, headers=self._headers(), json=payload, timeout=30)

        logger.debug("Response status: %s", resp.status_code)
        logger.debug("Response body: %s", resp.text)

        if resp.status_code != 200:
            raise Exception(f"Failed to delete TXT record: {resp.status_code} {resp.text}")

    @staticmethod
    def _get_zone_from_domain(domain: str) -> str:
        """Extract apex zone from FQDN."""
        parts = domain.strip(".").split(".")
        if len(parts) < 2:
            raise ValueError(f"Invalid domain: {domain}")
        return ".".join(parts[-2:])

    @staticmethod
    def _relative_record_name(zone: str, fqdn: str) -> str:
        """Convert full record name into relative name for the zone."""
        if fqdn.endswith("." + zone):
            return fqdn[: -(len(zone) + 1)]
        if fqdn == zone:
            return "@"
        return fqdn
