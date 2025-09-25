from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.models.folder_state import FolderState
from templafy.types import UNSET, Unset

T = TypeVar("T", bound="Folder")


@_attrs_define
class Folder:
    """Attributes:
    id (int): Unique folder identifier
    library_id (int): Unique library identifier
    name (str): Display name
    navigation_path (str): Hierarchical path in lowercase based on the location of a folder. E.g.
        "folder-a/folder-b" when the location is "Folder A > Folder B"
    modified_at (str): Date and time in ISO 8601 format of when the folder was last modified
    state (FolderState): The current state of the folder
    parent_id (Union[None, Unset, int]): Unique identifier for the parent folder. The root folder does not have a
        parent folder identifier
    """

    id: int
    library_id: int
    name: str
    navigation_path: str
    modified_at: str
    state: FolderState
    parent_id: None | Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        library_id = self.library_id

        name = self.name

        navigation_path = self.navigation_path

        modified_at = self.modified_at

        state = self.state.value

        parent_id: None | Unset | int
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "libraryId": library_id,
                "name": name,
                "navigationPath": navigation_path,
                "modifiedAt": modified_at,
                "state": state,
            }
        )
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        library_id = d.pop("libraryId")

        name = d.pop("name")

        navigation_path = d.pop("navigationPath")

        modified_at = d.pop("modifiedAt")

        state = FolderState(d.pop("state"))

        def _parse_parent_id(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | int", data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        folder = cls(
            id=id,
            library_id=library_id,
            name=name,
            navigation_path=navigation_path,
            modified_at=modified_at,
            state=state,
            parent_id=parent_id,
        )

        return folder
