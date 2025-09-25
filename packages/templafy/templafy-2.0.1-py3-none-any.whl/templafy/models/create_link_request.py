from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="CreateLinkRequest")


@_attrs_define
class CreateLinkRequest:
    """The request model to create a link asset

    Attributes:
        name (str): Display name
        url (str): A reference to the web resource. HTTP and HTTPS are supported
        description (Union[None, Unset, str]): Describing intended usage of the asset
        tags (Union[None, Unset, list[str]]): Tags should describe the content of the asset making it easier for a user
            to locate it
        external_data (Union[None, Unset, str]): External data which can be attached for future reference
    """

    name: str
    url: str
    description: None | Unset | str = UNSET
    tags: None | Unset | list[str] = UNSET
    external_data: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        """Convert the object to a dictionary."""
        name = self.name

        url = self.url

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

        external_data: None | Unset | str
        if isinstance(self.external_data, Unset):
            external_data = UNSET
        else:
            external_data = self.external_data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if external_data is not UNSET:
            field_dict["externalData"] = external_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create an instance from a dictionary."""
        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

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

        def _parse_external_data(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        external_data = _parse_external_data(d.pop("externalData", UNSET))

        create_link_request = cls(
            name=name,
            url=url,
            description=description,
            tags=tags,
            external_data=external_data,
        )

        return create_link_request
