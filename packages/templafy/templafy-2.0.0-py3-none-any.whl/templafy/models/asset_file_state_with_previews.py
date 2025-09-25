from enum import Enum


class AssetFileStateWithPreviews(str, Enum):
    """Enumeration of possible file processing states for an asset that
    includes previews.

    Values represent server-side lifecycle stages for an asset's file and
    its generated previews.
    """

    DELETING = "deleting"
    GENERATINGPREVIEWS = "generatingPreviews"
    GENERATINGPREVIEWSFAILED = "generatingPreviewsFailed"
    PROCESSING = "processing"
    PROCESSINGFAILED = "processingFailed"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
