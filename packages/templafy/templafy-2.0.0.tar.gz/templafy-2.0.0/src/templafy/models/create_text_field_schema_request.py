from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="CreateTextFieldSchemaRequest")


@_attrs_define
class CreateTextFieldSchemaRequest:
    """Example:
        {'name': 'History', 'type': 'text', 'isMultipleLines': True, 'defaultValue': 'The city was established in the
            year 1652 by Dutch explorers...', 'isRequired': False}

    Attributes:
        type_ (str): Data source field schema type.
        name (str): The name of the field. It must be unique within the data source.
        is_required (Union[Unset, bool]): Whether the field is required. If true, the field must be filled in when
            creating a data source item.
        is_multiple_lines (Union[Unset, bool]): Whether the field is multiple lines. If true, the field will be rendered
            as a text area.
        default_value (Union[None, Unset, str]): The default value of the field. If specified, the field will be pre-
            filled with this value when creating a data source item.
    """

    type_: str
    name: str
    is_required: Unset | bool = UNSET
    is_multiple_lines: Unset | bool = UNSET
    default_value: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

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
                "name": name,
            }
        )
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if is_multiple_lines is not UNSET:
            field_dict["isMultipleLines"] = is_multiple_lines
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        is_required = d.pop("isRequired", UNSET)

        is_multiple_lines = d.pop("isMultipleLines", UNSET)

        def _parse_default_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        default_value = _parse_default_value(d.pop("defaultValue", UNSET))

        create_text_field_schema_request = cls(
            type_=type_,
            name=name,
            is_required=is_required,
            is_multiple_lines=is_multiple_lines,
            default_value=default_value,
        )

        create_text_field_schema_request.additional_properties = d
        return create_text_field_schema_request

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
