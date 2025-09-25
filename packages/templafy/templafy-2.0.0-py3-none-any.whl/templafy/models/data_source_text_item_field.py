from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="DataSourceTextItemField")


@_attrs_define
class DataSourceTextItemField:
    """Example:
        {'dataSourceFieldId': 0, 'type': 'text', 'value': 'Sample text'}

    Attributes:
        type_ (Union[None, str]): Data source item field type.
        data_source_field_id (Union[Unset, int]): Unique data source field identifier.
        value (Union[None, Unset, str]): Text data source item field value.
    """

    type_: None | str
    data_source_field_id: Unset | int = UNSET
    value: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: None | str
        type_ = self.type_

        data_source_field_id = self.data_source_field_id

        value: None | Unset | str
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if data_source_field_id is not UNSET:
            field_dict["dataSourceFieldId"] = data_source_field_id
        if value is not UNSET:
            field_dict["value"] = value

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

        def _parse_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        value = _parse_value(d.pop("value", UNSET))

        data_source_text_item_field = cls(
            type_=type_,
            data_source_field_id=data_source_field_id,
            value=value,
        )

        data_source_text_item_field.additional_properties = d
        return data_source_text_item_field

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
