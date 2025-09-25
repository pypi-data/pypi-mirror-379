from enum import Enum


class FolderState(str, Enum):
    """Enumeration of possible lifecycle states for a folder resource.

    Typical values indicate whether the folder is ready for use or in the
    process of being deleted on the server.
    """

    DELETING = "deleting"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
