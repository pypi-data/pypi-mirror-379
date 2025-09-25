from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="PatchDataSourceItemFieldRequest")


@_attrs_define
class PatchDataSourceItemFieldRequest:
    """Attributes:
    type_ (str): Data source item field type.
    data_source_field_id (int): The identifier of the field to be updated.
    """

    type_: str
    data_source_field_id: int

    def to_dict(self) -> dict[str, Any]:
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
        d = dict(src_dict)
        type_ = d.pop("type")

        data_source_field_id = d.pop("dataSourceFieldId")

        patch_data_source_item_field_request = cls(
            type_=type_,
            data_source_field_id=data_source_field_id,
        )

        return patch_data_source_item_field_request
