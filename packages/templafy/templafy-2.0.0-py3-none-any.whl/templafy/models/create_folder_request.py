from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="CreateFolderRequest")


@_attrs_define
class CreateFolderRequest:
    """The request model to create a folder

    Attributes:
        name (str): Display name
    """

    name: str

    def to_dict(self) -> dict[str, Any]:
        """Convert the object to a dictionary."""
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create an instance from a dictionary."""
        d = dict(src_dict)
        name = d.pop("name")

        create_folder_request = cls(
            name=name,
        )

        return create_folder_request
