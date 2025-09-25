from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ValidationProblemDetailsErrorsType0")


@_attrs_define
class ValidationProblemDetailsErrorsType0:
    """Mapping of validation error fields to lists of error messages."""

    additional_properties: dict[str, list[str]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = dict(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        validation_problem_details_errors_type_0 = cls()

        additional_properties = {
            prop_name: cast("list[str]", prop_dict)
            for prop_name, prop_dict in d.items()
        }

        validation_problem_details_errors_type_0.additional_properties = (
            additional_properties
        )
        return validation_problem_details_errors_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
