from enum import Enum


class LockReason(str, Enum):
    """Enumeration of reasons why a resource may be locked.

    Values indicate the cause for locking, such as a hard dependency or
    restricted access control preventing modifications.
    """

    HARDDEPENDENCY = "hardDependency"
    RESTRICTEDACCESS = "restrictedAccess"

    def __str__(self) -> str:
        return str(self.value)
