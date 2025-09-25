from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="DataSourceColorThemeItemField")


@_attrs_define
class DataSourceColorThemeItemField:
    """Example:
        {'dataSourceFieldId': 5, 'type': 'colorTheme', 'xmlValue': '<a:clrScheme
            xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Templafy_New"><a:dk1><a:srgbClr
            val="0078FF"/></a:dk1><a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr
            val="000000"/></a:dk2><a:lt2><a:srgbClr val="E5E5E5"/></a:lt2><a:accent1><a:srgbClr
            val="0078FF"/></a:accent1><a:accent2><a:srgbClr val="575757"/></a:accent2><a:accent3><a:srgbClr
            val="12AA96"/></a:accent3><a:accent4><a:srgbClr val="15436B"/></a:accent4><a:accent5><a:srgbClr
            val="D44849"/></a:accent5><a:accent6><a:srgbClr val="7F7F7F"/></a:accent6><a:hlink><a:srgbClr
            val="0078FF"/></a:hlink><a:folHlink><a:srgbClr val="55CBFF"/></a:folHlink></a:clrScheme>'}

    Attributes:
        type_ (Union[None, str]): Data source item field type.
        data_source_field_id (Union[Unset, int]): Unique data source field identifier.
        xml_value (Union[None, Unset, str]): The value of the field based on the schema
            http://schemas.openxmlformats.org/drawingml/2006/main.
    """

    type_: None | str
    data_source_field_id: Unset | int = UNSET
    xml_value: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: None | str
        type_ = self.type_

        data_source_field_id = self.data_source_field_id

        xml_value: None | Unset | str
        if isinstance(self.xml_value, Unset):
            xml_value = UNSET
        else:
            xml_value = self.xml_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if data_source_field_id is not UNSET:
            field_dict["dataSourceFieldId"] = data_source_field_id
        if xml_value is not UNSET:
            field_dict["xmlValue"] = xml_value

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

        def _parse_xml_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        xml_value = _parse_xml_value(d.pop("xmlValue", UNSET))

        data_source_color_theme_item_field = cls(
            type_=type_,
            data_source_field_id=data_source_field_id,
            xml_value=xml_value,
        )

        data_source_color_theme_item_field.additional_properties = d
        return data_source_color_theme_item_field

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
