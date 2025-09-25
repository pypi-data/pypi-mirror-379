from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="CreateNumberFieldSchemaRequest")


@_attrs_define
class CreateNumberFieldSchemaRequest:
    """Example:
        {'name': 'Population', 'type': 'number', 'defaultValue': 100222, 'isRequired': True}

    Attributes:
        type_ (str): Data source field schema type.
        name (str): The name of the field. It must be unique within the data source.
        is_required (Union[Unset, bool]): Whether the field is required. If true, the field must be filled in when
            creating a data source item.
        default_value (Union[None, Unset, float]): The default value of the field. If specified, the field will be pre-
            filled with this value when creating a data source item.
    """

    type_: str
    name: str
    is_required: Unset | bool = UNSET
    default_value: None | Unset | float = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        is_required = self.is_required

        default_value: None | Unset | float
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

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
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        is_required = d.pop("isRequired", UNSET)

        def _parse_default_value(data: object) -> None | Unset | float:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | float", data)

        default_value = _parse_default_value(d.pop("defaultValue", UNSET))

        create_number_field_schema_request = cls(
            type_=type_,
            name=name,
            is_required=is_required,
            default_value=default_value,
        )

        create_number_field_schema_request.additional_properties = d
        return create_number_field_schema_request

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
