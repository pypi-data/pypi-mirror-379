from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="CreateDataSourceItemFieldRequest")


@_attrs_define
class CreateDataSourceItemFieldRequest:
    """Attributes:
    type_ (str): Data source item field type.
    data_source_field_id (int): Data source field identifier.
    """

    type_: str
    data_source_field_id: int

    def to_dict(self) -> dict[str, Any]:
        """Convert the object to a dictionary."""
        type_ = self.type_

        data_source_field_id = self.data_source_field_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "dataSourceFieldId": data_source_field_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create an instance from a dictionary."""
        d = dict(src_dict)
        type_ = d.pop("type")

        data_source_field_id = d.pop("dataSourceFieldId")

        create_data_source_item_field_request = cls(
            type_=type_,
            data_source_field_id=data_source_field_id,
        )

        return create_data_source_item_field_request
