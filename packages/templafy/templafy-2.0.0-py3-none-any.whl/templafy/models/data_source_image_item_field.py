from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="DataSourceImageItemField")


@_attrs_define
class DataSourceImageItemField:
    """Example:
        {'dataSourceFieldId': 2, 'type': 'image', 'fileName': 'Cat', 'fileUrl':
            'https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg'}

    Attributes:
        type_ (Union[None, str]): Data source item field type.
        data_source_field_id (Union[Unset, int]): Unique data source field identifier.
        file_name (Union[None, Unset, str]): The name of the file.
        file_url (Union[None, Unset, str]): The file size must be under 2MB, and it should be in one of these formats:
            .png, .jpg, .jpeg, .gif, .bmp, .emf, .wmf, .svg.
    """

    type_: None | str
    data_source_field_id: Unset | int = UNSET
    file_name: None | Unset | str = UNSET
    file_url: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: None | str
        type_ = self.type_

        data_source_field_id = self.data_source_field_id

        file_name: None | Unset | str
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        file_url: None | Unset | str
        if isinstance(self.file_url, Unset):
            file_url = UNSET
        else:
            file_url = self.file_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if data_source_field_id is not UNSET:
            field_dict["dataSourceFieldId"] = data_source_field_id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if file_url is not UNSET:
            field_dict["fileUrl"] = file_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast("None | str", data)

        type_ = _parse_type_(d.pop("type"))

        data_source_field_id = d.pop("dataSourceFieldId", UNSET)

        def _parse_file_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))

        def _parse_file_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        file_url = _parse_file_url(d.pop("fileUrl", UNSET))

        data_source_image_item_field = cls(
            type_=type_,
            data_source_field_id=data_source_field_id,
            file_name=file_name,
            file_url=file_url,
        )

        data_source_image_item_field.additional_properties = d
        return data_source_image_item_field

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
