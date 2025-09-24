import logging
from typing import Any

from certbot import errors
from certbot.plugins import dns_common

from .abion_client import AbionClient

logger = logging.getLogger(__name__)


class Authenticator(dns_common.DNSAuthenticator):
    """DNS Authenticator for Abion DNS API"""

    description = (
        "Obtain certificates using a DNS TXT record "
        "(DNS-01 challenge) via the Abion DNS API."
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.credentials = None  # type: dns_common.CredentialsConfiguration
        self.abion = None        # type: AbionClient

    @classmethod
    def add_parser_arguments(cls, add: Any) -> None:
        super().add_parser_arguments(add)
        add(
            "credentials",
            help="Path to Abion API credentials INI file",
        )

    def more_info(self) -> str:
        return "This plugin configures DNS records using the Abion DNS API."

    def _setup_credentials(self) -> None:
        self.credentials = self._configure_credentials(
            "credentials",
            "Abion credentials INI file",
            {
                "dns_abion_api_key": "API key for Abion",
                "dns_abion_api_key": "Base URL for Abion API (default: https://api.abion.com/)",
            },
        )
        self.abion = AbionClient(
            api_key=self.credentials.conf("dns_abion_api_key"),
            api_url=self.credentials.conf("dns_abion_api_url") or "https://api.abion.com/",
        )

    def _perform(self, domain: str, validation_name: str, validation: str) -> None:
        try:
            logger.debug("Adding TXT record %s = %s", validation_name, validation)
            self.abion.add_txt_record(domain, validation_name, validation)
        except Exception as e:
            raise errors.PluginError(f"Error adding TXT record: {e}") from e

    def _cleanup(self, domain: str, validation_name: str, validation: str) -> None:
        try:
            logger.debug("Removing TXT record %s = %s", validation_name, validation)
            self.abion.del_txt_record(domain, validation_name, validation)
        except Exception as e:
            raise errors.PluginError(f"Error removing TXT record: {e}") from e
