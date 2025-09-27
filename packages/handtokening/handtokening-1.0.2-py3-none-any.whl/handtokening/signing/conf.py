from functools import cached_property
from pathlib import Path

from django.conf import settings


class Configuration:
    @cached_property
    def OSSL_PROVIDER_PATH(self) -> str | None:
        return getattr(settings, "OSSL_PROVIDER_PATH", None)

    @cached_property
    def OSSL_ENGINE_PATH(self) -> str | None:
        return getattr(settings, "OSSL_ENGINE_PATH", None)

    @cached_property
    def PKCS11_MODULE_PATH(self) -> str | None:
        return getattr(settings, "PKCS11_MODULE_PATH", None)

    @cached_property
    def OSSLSIGNCODE_PATH(self) -> str:
        return getattr(settings, "OSSLSIGNCODE_PATH", None) or "osslsigncode"

    @cached_property
    def CLAMSCAN_PATH(self) -> str:
        return getattr(settings, "CLAMSCAN_PATH", None) or "/usr/bin/clamdscan"

    @cached_property
    def PIN_COMMS_LOCATION(self) -> Path:
        return Path(
            getattr(settings, "PIN_COMMS_LOCATION", None) or "/run/handtokening"
        )

    @cached_property
    def STATE_DIRECTORY(self) -> Path:
        return Path(
            getattr(settings, "STATE_DIRECTORY", None) or "/var/lib/handtokening"
        )

    @cached_property
    def VIRUS_TOTAL_API_KEY(self) -> str | None:
        return getattr(settings, "VIRUS_TOTAL_API_KEY", None)

    @cached_property
    def TEST_CERTIFICATE_DIRECTORY(self) -> Path:
        return Path(
            getattr(settings, "TEST_CERTIFICATE_DIRECTORY", None)
            or self.STATE_DIRECTORY / "certs"
        )


config = Configuration()
