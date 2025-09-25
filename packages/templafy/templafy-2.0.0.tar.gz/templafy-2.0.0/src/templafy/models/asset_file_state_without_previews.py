from enum import Enum


class AssetFileStateWithoutPreviews(str, Enum):
    """Enumeration of possible file processing states for an asset that
    does not include generated previews.

    Values indicate server-side lifecycle stages for an asset's file only.
    """

    DELETING = "deleting"
    PROCESSING = "processing"
    PROCESSINGFAILED = "processingFailed"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
