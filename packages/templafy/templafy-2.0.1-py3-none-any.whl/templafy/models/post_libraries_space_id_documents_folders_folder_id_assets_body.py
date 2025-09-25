from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy import types
from templafy.types import UNSET, File, Unset

T = TypeVar("T", bound="PostLibrariesSpaceIdDocumentsFoldersFolderIdAssetsBody")


@_attrs_define
class PostLibrariesSpaceIdDocumentsFoldersFolderIdAssetsBody:
    """Attributes:
    file (File): A file to be uploaded. The maximum file size is 50 mb
    name (Union[Unset, str]): The name is inferred from the file name by default. It can be overridden by providing
        a different value with this field
    description (Union[Unset, str]): Description is used to specify the intended usage of the asset
    tags (Union[Unset, list[str]]): Tags should describe the content of the asset making it easier for a user to
        locate it
    external_data (Union[Unset, str]): External data which can be attached for future reference
    """

    file: File
    name: Unset | str = UNSET
    description: Unset | str = UNSET
    tags: Unset | list[str] = UNSET
    external_data: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        name = self.name

        description = self.description

        tags: Unset | list[str] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        external_data = self.external_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "File": file,
            }
        )
        if name is not UNSET:
            field_dict["Name"] = name
        if description is not UNSET:
            field_dict["Description"] = description
        if tags is not UNSET:
            field_dict["Tags"] = tags
        if external_data is not UNSET:
            field_dict["ExternalData"] = external_data

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("File", self.file.to_tuple()))

        if not isinstance(self.name, Unset):
            files.append(("Name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(
                ("Description", (None, str(self.description).encode(), "text/plain"))
            )

        if not isinstance(self.tags, Unset):
            for tags_item_element in self.tags:
                files.append(
                    ("Tags", (None, str(tags_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.external_data, Unset):
            files.append(
                ("ExternalData", (None, str(self.external_data).encode(), "text/plain"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("File")))

        name = d.pop("Name", UNSET)

        description = d.pop("Description", UNSET)

        tags = cast("list[str]", d.pop("Tags", UNSET))

        external_data = d.pop("ExternalData", UNSET)

        post_libraries_space_id_documents_folders_folder_id_assets_body = cls(
            file=file,
            name=name,
            description=description,
            tags=tags,
            external_data=external_data,
        )

        post_libraries_space_id_documents_folders_folder_id_assets_body.additional_properties = d
        return post_libraries_space_id_documents_folders_folder_id_assets_body

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
