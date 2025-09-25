from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="UpdateDataSourceItemFieldRequest")


@_attrs_define
class UpdateDataSourceItemFieldRequest:
    """Example:
        {'type': 'text', 'value': 'An updated value'}

    Attributes:
        type_ (str): Data source item field type.
    """

    type_: str

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        update_data_source_item_field_request = cls(
            type_=type_,
        )

        return update_data_source_item_field_request
