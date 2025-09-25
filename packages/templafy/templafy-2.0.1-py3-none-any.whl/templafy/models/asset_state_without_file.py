from enum import Enum


class AssetStateWithoutFile(str, Enum):
    """Enumeration of possible states for an asset that has no file
    attached.

    Currently only indicates readiness state returned by the API.
    """

    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
