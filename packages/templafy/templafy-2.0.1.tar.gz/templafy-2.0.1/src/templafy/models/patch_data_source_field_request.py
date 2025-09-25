from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="PatchDataSourceFieldRequest")


@_attrs_define
class PatchDataSourceFieldRequest:
    """Example:
        {'name': 'Population', 'isRequired': True, 'defaultValue': 130000}

    Attributes:
        name (Union[None, Unset, str]): The name of the field. It must be unique within the data source.
        is_required (Union[None, Unset, bool]): Whether the field is required. If true, the field must be filled in when
            creating a data source item.
        is_multiple_lines (Union[None, Unset, bool]): Whether the field is multiple lines. If true, the field will be
            rendered as a text area.
        default_value (Union[None, Unset, str]): The default value of the field. If specified, the field will be pre-
            filled with this value when creating a data source item.
    """

    name: None | Unset | str = UNSET
    is_required: None | Unset | bool = UNSET
    is_multiple_lines: None | Unset | bool = UNSET
    default_value: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_required: None | Unset | bool
        if isinstance(self.is_required, Unset):
            is_required = UNSET
        else:
            is_required = self.is_required

        is_multiple_lines: None | Unset | bool
        if isinstance(self.is_multiple_lines, Unset):
            is_multiple_lines = UNSET
        else:
            is_multiple_lines = self.is_multiple_lines

        default_value: None | Unset | str
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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

        def _parse_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_is_required(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | bool", data)

        is_required = _parse_is_required(d.pop("isRequired", UNSET))

        def _parse_is_multiple_lines(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | bool", data)

        is_multiple_lines = _parse_is_multiple_lines(d.pop("isMultipleLines", UNSET))

        def _parse_default_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        default_value = _parse_default_value(d.pop("defaultValue", UNSET))

        patch_data_source_field_request = cls(
            name=name,
            is_required=is_required,
            is_multiple_lines=is_multiple_lines,
            default_value=default_value,
        )

        return patch_data_source_field_request
