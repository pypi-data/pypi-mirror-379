from enum import Enum


class SourceEntityType(str, Enum):
    """Enumeration of source entity types that can be referenced by the API.

    Identifies whether the source is a data source, a data source item, or
    some other external entity.
    """

    DATASOURCE = "dataSource"
    DATASOURCEITEM = "dataSourceItem"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
