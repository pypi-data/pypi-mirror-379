from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="CreateDataSourceFieldSchemaRequest")


@_attrs_define
class CreateDataSourceFieldSchemaRequest:
    """Example:
        {'name': 'History', 'type': 'text', 'isMultipleLines': True, 'defaultValue': 'The city was established in the
            year 1652 by Dutch explorers...', 'isRequired': False}

    Attributes:
        type_ (str): Data source field schema type.
        name (str): The name of the field. It must be unique within the data source.
        is_required (Union[Unset, bool]): Whether the field is required. If true, the field must be filled in when
            creating a data source item.
    """

    type_: str
    name: str
    is_required: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        """Convert the object to a dictionary."""
        type_ = self.type_

        name = self.name

        is_required = self.is_required

        field_dict: dict[str, Any] = {}

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
        """Create an instance from a dictionary."""
        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        is_required = d.pop("isRequired", UNSET)

        create_data_source_field_schema_request = cls(
            type_=type_,
            name=name,
            is_required=is_required,
        )

        return create_data_source_field_schema_request
