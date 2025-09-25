from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.models.asset_file_state_with_previews import AssetFileStateWithPreviews
from templafy.types import UNSET, Unset

if TYPE_CHECKING:
    from templafy.models.dimensions import Dimensions
from templafy.models.dimensions import Dimensions

T = TypeVar("T", bound="Image")


@_attrs_define
class Image:
    """Attributes:
    id (int): Unique asset identifier
    folder_id (int): Unique folder identifier
    name (str): Display name
    description (str):
    tags (list[str]):
    file_size (int): File size in bytes
    checksum (str): MD5 checksum of the bytes
    file_extension (str): Suffix to the name of the file
    dimensions (Dimensions): Asset dimensions
    mime_type (str):
    automatic_tags (list[str]): Tags that are automatically generated based on the image
    navigation_path (str): Hierarchical path in lowercase based on the location of an image. E.g.
        "folder-a/folder-b/_my-image" when the location is "Folder A > Folder B > My Image"
    modified_at (str): Date and time in ISO 8601 format of when the asset was last modified
    asset_state (AssetFileStateWithPreviews): The current state of the asset
    small_preview_link (Union[None, Unset, str]): Link to the image with the maximum width 400px
    large_preview_link (Union[None, Unset, str]): Link to the image with the maximum width 1500px
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
    dimensions: "Dimensions"
    mime_type: str
    automatic_tags: list[str]
    navigation_path: str
    modified_at: str
    asset_state: AssetFileStateWithPreviews
    small_preview_link: None | Unset | str = UNSET
    large_preview_link: None | Unset | str = UNSET
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

        dimensions = self.dimensions.to_dict()

        mime_type = self.mime_type

        automatic_tags = self.automatic_tags

        navigation_path = self.navigation_path

        modified_at = self.modified_at

        asset_state = self.asset_state.value

        small_preview_link: None | Unset | str
        if isinstance(self.small_preview_link, Unset):
            small_preview_link = UNSET
        else:
            small_preview_link = self.small_preview_link

        large_preview_link: None | Unset | str
        if isinstance(self.large_preview_link, Unset):
            large_preview_link = UNSET
        else:
            large_preview_link = self.large_preview_link

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
                "dimensions": dimensions,
                "mimeType": mime_type,
                "automaticTags": automatic_tags,
                "navigationPath": navigation_path,
                "modifiedAt": modified_at,
                "assetState": asset_state,
            }
        )
        if small_preview_link is not UNSET:
            field_dict["smallPreviewLink"] = small_preview_link
        if large_preview_link is not UNSET:
            field_dict["largePreviewLink"] = large_preview_link
        if external_data is not UNSET:
            field_dict["externalData"] = external_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        # Top-level imports are used to avoid inline imports (PLC0415)
        d = dict(src_dict)
        id = d.pop("id")

        folder_id = d.pop("folderId")

        name = d.pop("name")

        description = d.pop("description")

        tags = cast("list[str]", d.pop("tags"))

        file_size = d.pop("fileSize")

        checksum = d.pop("checksum")

        file_extension = d.pop("fileExtension")

        dimensions = Dimensions.from_dict(d.pop("dimensions"))

        mime_type = d.pop("mimeType")

        automatic_tags = cast("list[str]", d.pop("automaticTags"))

        navigation_path = d.pop("navigationPath")

        modified_at = d.pop("modifiedAt")

        asset_state = AssetFileStateWithPreviews(d.pop("assetState"))

        def _parse_small_preview_link(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        small_preview_link = _parse_small_preview_link(d.pop("smallPreviewLink", UNSET))

        def _parse_large_preview_link(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        large_preview_link = _parse_large_preview_link(d.pop("largePreviewLink", UNSET))

        def _parse_external_data(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        external_data = _parse_external_data(d.pop("externalData", UNSET))

        image = cls(
            id=id,
            folder_id=folder_id,
            name=name,
            description=description,
            tags=tags,
            file_size=file_size,
            checksum=checksum,
            file_extension=file_extension,
            dimensions=dimensions,
            mime_type=mime_type,
            automatic_tags=automatic_tags,
            navigation_path=navigation_path,
            modified_at=modified_at,
            asset_state=asset_state,
            small_preview_link=small_preview_link,
            large_preview_link=large_preview_link,
            external_data=external_data,
        )

        return image
