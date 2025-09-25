from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="CreateImageDataSourceItemFieldRequest")


@_attrs_define
class CreateImageDataSourceItemFieldRequest:
    """Example:
        {'type': 'image', 'dataSourceFieldId': 3, 'fileName': 'Cat', 'fileUrl':
            'https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg'}

    Attributes:
        type_ (str): Data source item field type.
        data_source_field_id (int): Data source field identifier.
        file_name (str): The name of the file.
        file_url (Union[None, Unset, str]): The file size must be under 2MB, and it should be in one of these formats:
            .png, .jpg, .jpeg, .gif, .bmp, .emf, .wmf, .svg.
        content (Union[None, Unset, str]): The base64 content size must be under 2MB, and it should be in one of these
            formats: .png, .jpg, .jpeg, .gif, .bmp, .emf, .wmf, .svg.
    """

    type_: str
    data_source_field_id: int
    file_name: str
    file_url: None | Unset | str = UNSET
    content: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        data_source_field_id = self.data_source_field_id

        file_name = self.file_name

        file_url: None | Unset | str
        if isinstance(self.file_url, Unset):
            file_url = UNSET
        else:
            file_url = self.file_url

        content: None | Unset | str
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "dataSourceFieldId": data_source_field_id,
                "fileName": file_name,
            }
        )
        if file_url is not UNSET:
            field_dict["fileUrl"] = file_url
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        data_source_field_id = d.pop("dataSourceFieldId")

        file_name = d.pop("fileName")

        def _parse_file_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        file_url = _parse_file_url(d.pop("fileUrl", UNSET))

        def _parse_content(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        content = _parse_content(d.pop("content", UNSET))

        create_image_data_source_item_field_request = cls(
            type_=type_,
            data_source_field_id=data_source_field_id,
            file_name=file_name,
            file_url=file_url,
            content=content,
        )

        create_image_data_source_item_field_request.additional_properties = d
        return create_image_data_source_item_field_request

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
