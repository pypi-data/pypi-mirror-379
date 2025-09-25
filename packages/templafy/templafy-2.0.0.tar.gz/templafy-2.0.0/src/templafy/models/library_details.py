from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.models.library_type import LibraryType

T = TypeVar("T", bound="LibraryDetails")


@_attrs_define
class LibraryDetails:
    """Attributes:
    id (int): Unique library identifier
    name (str): Display name of the library
    library_type (LibraryType): Type of the assets that can be stored in the library
    space_id (int): Unique identifier of the space to which the library belongs
    root_folder_id (int): Unique identifier of the root folder of the library
    """

    id: int
    name: str
    library_type: LibraryType
    space_id: int
    root_folder_id: int

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        library_type = self.library_type.value

        space_id = self.space_id

        root_folder_id = self.root_folder_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "libraryType": library_type,
                "spaceId": space_id,
                "rootFolderId": root_folder_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        library_type = LibraryType(d.pop("libraryType"))

        space_id = d.pop("spaceId")

        root_folder_id = d.pop("rootFolderId")

        library_details = cls(
            id=id,
            name=name,
            library_type=library_type,
            space_id=space_id,
            root_folder_id=root_folder_id,
        )

        return library_details
