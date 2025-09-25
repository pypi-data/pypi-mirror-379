from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="FontFieldSchema")


@_attrs_define
class FontFieldSchema:
    """Example:
        {'id': 5, 'name': 'PreferredFont', 'type': 'font', 'isRequired': False, 'isLocked': False}

    Attributes:
        type_ (str): Data source field schema type.
        id (int): Unique data source field schema identifier
        name (str): Data source field schema name. It must be unique within the data source.
        is_locked (bool): Value indicating whether data source schema is locked. If true, the field cannot be deleted or
            modified.
        is_required (bool): Whether the field is required. If true, the field must be filled in when creating a data
            source item.
    """

    type_: str
    id: int
    name: str
    is_locked: bool
    is_required: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        name = self.name

        is_locked = self.is_locked

        is_required = self.is_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "name": name,
                "isLocked": is_locked,
                "isRequired": is_required,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id")

        name = d.pop("name")

        is_locked = d.pop("isLocked")

        is_required = d.pop("isRequired")

        font_field_schema = cls(
            type_=type_,
            id=id,
            name=name,
            is_locked=is_locked,
            is_required=is_required,
        )

        font_field_schema.additional_properties = d
        return font_field_schema

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
