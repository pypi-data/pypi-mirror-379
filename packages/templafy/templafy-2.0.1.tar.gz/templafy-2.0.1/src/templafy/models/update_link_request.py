from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="UpdateLinkRequest")


@_attrs_define
class UpdateLinkRequest:
    """Attributes:
    folder_id (Union[None, Unset, int]): The identifier of the destination folder
    name (Union[None, Unset, str]): A new display name of the asset
    description (Union[None, Unset, str]): Description is used to specify the intended usage of the asset
    tags (Union[None, Unset, list[str]]): Tags should describe the content of the asset making it easier for a user
        to locate it
    url (Union[None, Unset, str]): A reference to the web resource. HTTP and HTTPS are supported
    external_data (Union[None, Unset, str]): External data which can be attached for future reference
    """

    folder_id: None | Unset | int = UNSET
    name: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    tags: None | Unset | list[str] = UNSET
    url: None | Unset | str = UNSET
    external_data: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        folder_id: None | Unset | int
        if isinstance(self.folder_id, Unset):
            folder_id = UNSET
        else:
            folder_id = self.folder_id

        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tags: None | Unset | list[str]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        url: None | Unset | str
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        external_data: None | Unset | str
        if isinstance(self.external_data, Unset):
            external_data = UNSET
        else:
            external_data = self.external_data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if url is not UNSET:
            field_dict["url"] = url
        if external_data is not UNSET:
            field_dict["externalData"] = external_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_folder_id(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | int", data)

        folder_id = _parse_folder_id(d.pop("folderId", UNSET))

        def _parse_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tags(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError
                tags_type_0 = cast("list[str]", data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast("None | Unset | list[str]", data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_external_data(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        external_data = _parse_external_data(d.pop("externalData", UNSET))

        update_link_request = cls(
            folder_id=folder_id,
            name=name,
            description=description,
            tags=tags,
            url=url,
            external_data=external_data,
        )

        return update_link_request
