from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="CreateImageFieldSchemaRequest")


@_attrs_define
class CreateImageFieldSchemaRequest:
    """Example:
        {'name': 'Flag', 'type': 'image', 'isRequired': True}

    Attributes:
        type_ (str): Data source field schema type.
        name (str): The name of the field. It must be unique within the data source.
        is_required (Union[Unset, bool]): Whether the field is required. If true, the field must be filled in when
            creating a data source item.
    """

    type_: str
    name: str
    is_required: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        is_required = self.is_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        is_required = d.pop("isRequired", UNSET)

        create_image_field_schema_request = cls(
            type_=type_,
            name=name,
            is_required=is_required,
        )

        create_image_field_schema_request.additional_properties = d
        return create_image_field_schema_request

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
