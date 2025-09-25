from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="DataSourceReferenceItemField")


@_attrs_define
class DataSourceReferenceItemField:
    """Example:
        {'dataSourceFieldId': 4, 'type': 'reference', 'dataSourceItemId': '638247997437572264'}

    Attributes:
        type_ (Union[None, str]): Data source item field type.
        data_source_field_id (Union[Unset, int]): Unique data source field identifier.
        data_source_item_id (Union[Unset, int]): The identifier of the data source item to be referenced.
    """

    type_: None | str
    data_source_field_id: Unset | int = UNSET
    data_source_item_id: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: None | str
        type_ = self.type_

        data_source_field_id = self.data_source_field_id

        data_source_item_id = self.data_source_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if data_source_field_id is not UNSET:
            field_dict["dataSourceFieldId"] = data_source_field_id
        if data_source_item_id is not UNSET:
            field_dict["dataSourceItemId"] = data_source_item_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast("None | str", data)

        type_ = _parse_type_(d.pop("type"))

        data_source_field_id = d.pop("dataSourceFieldId", UNSET)

        data_source_item_id = d.pop("dataSourceItemId", UNSET)

        data_source_reference_item_field = cls(
            type_=type_,
            data_source_field_id=data_source_field_id,
            data_source_item_id=data_source_item_id,
        )

        data_source_reference_item_field.additional_properties = d
        return data_source_reference_item_field

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
