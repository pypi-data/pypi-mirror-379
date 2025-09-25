from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="TextFieldSchema")


@_attrs_define
class TextFieldSchema:
    """Example:
        {'id': 1, 'name': 'History', 'type': 'text', 'isRequired': True, 'isLocked': False, 'isMultipleLines': False,
            'defaultValue': 'The city was established in the year 1652 by Dutch explorers...'}

    Attributes:
        type_ (str): Data source field schema type.
        id (int): Unique data source field schema identifier
        name (str): Data source field schema name. It must be unique within the data source.
        is_locked (bool): Value indicating whether data source schema is locked. If true, the field cannot be deleted or
            modified.
        is_required (bool): Whether the field is required. If true, the field must be filled in when creating a data
            source item.
        is_multiple_lines (bool): Whether the field is multiple lines. If true, the field will be rendered as a text
            area.
        default_value (Union[None, Unset, str]): The default value of the field. If specified, the field will be pre-
            filled with this value when creating a data source item.
    """

    type_: str
    id: int
    name: str
    is_locked: bool
    is_required: bool
    is_multiple_lines: bool
    default_value: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        name = self.name

        is_locked = self.is_locked

        is_required = self.is_required

        is_multiple_lines = self.is_multiple_lines

        default_value: None | Unset | str
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "name": name,
                "isLocked": is_locked,
                "isRequired": is_required,
                "isMultipleLines": is_multiple_lines,
            }
        )
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id")

        name = d.pop("name")

        is_locked = d.pop("isLocked")

        is_required = d.pop("isRequired")

        is_multiple_lines = d.pop("isMultipleLines")

        def _parse_default_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        default_value = _parse_default_value(d.pop("defaultValue", UNSET))

        text_field_schema = cls(
            type_=type_,
            id=id,
            name=name,
            is_locked=is_locked,
            is_required=is_required,
            is_multiple_lines=is_multiple_lines,
            default_value=default_value,
        )

        text_field_schema.additional_properties = d
        return text_field_schema

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
