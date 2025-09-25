from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.models.asset_file_state_without_previews import (
    AssetFileStateWithoutPreviews,
)
from templafy.types import UNSET, Unset

T = TypeVar("T", bound="TextElement")


@_attrs_define
class TextElement:
    """Attributes:
    id (int): Unique asset identifier
    folder_id (int): Unique folder identifier
    name (str): Display name
    description (str):
    tags (list[str]):
    file_size (int): File size in bytes
    checksum (str): MD5 checksum of the bytes
    file_extension (str): Suffix to the name of the file
    navigation_path (str): Hierarchical path in lowercase based on the location of a text element. E.g.
        "folder-a/folder-b/_my-text-element" when the location is "Folder A > Folder B > My Text Element"
    modified_at (str): Date and time in ISO 8601 format of when the asset was last modified
    asset_state (AssetFileStateWithoutPreviews): The current state of the asset
    external_data (Union[None, Unset, str]): External data which can be attached for future reference
    """

    id: int
    folder_id: int
    name: str
    description: str
    tags: list[str]
    file_size: int
    checksum: str
    file_extension: str
    navigation_path: str
    modified_at: str
    asset_state: AssetFileStateWithoutPreviews
    external_data: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        folder_id = self.folder_id

        name = self.name

        description = self.description

        tags = self.tags

        file_size = self.file_size

        checksum = self.checksum

        file_extension = self.file_extension

        navigation_path = self.navigation_path

        modified_at = self.modified_at

        asset_state = self.asset_state.value

        external_data: None | Unset | str
        if isinstance(self.external_data, Unset):
            external_data = UNSET
        else:
            external_data = self.external_data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "folderId": folder_id,
                "name": name,
                "description": description,
                "tags": tags,
                "fileSize": file_size,
                "checksum": checksum,
                "fileExtension": file_extension,
                "navigationPath": navigation_path,
                "modifiedAt": modified_at,
                "assetState": asset_state,
            }
        )
        if external_data is not UNSET:
            field_dict["externalData"] = external_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        folder_id = d.pop("folderId")

        name = d.pop("name")

        description = d.pop("description")

        tags = cast("list[str]", d.pop("tags"))

        file_size = d.pop("fileSize")

        checksum = d.pop("checksum")

        file_extension = d.pop("fileExtension")

        navigation_path = d.pop("navigationPath")

        modified_at = d.pop("modifiedAt")

        asset_state = AssetFileStateWithoutPreviews(d.pop("assetState"))

        def _parse_external_data(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        external_data = _parse_external_data(d.pop("externalData", UNSET))

        text_element = cls(
            id=id,
            folder_id=folder_id,
            name=name,
            description=description,
            tags=tags,
            file_size=file_size,
            checksum=checksum,
            file_extension=file_extension,
            navigation_path=navigation_path,
            modified_at=modified_at,
            asset_state=asset_state,
            external_data=external_data,
        )

        return text_element
