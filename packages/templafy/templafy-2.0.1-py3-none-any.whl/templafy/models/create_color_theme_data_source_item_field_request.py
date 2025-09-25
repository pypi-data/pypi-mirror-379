from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="CreateColorThemeDataSourceItemFieldRequest")


@_attrs_define
class CreateColorThemeDataSourceItemFieldRequest:
    """Example:
        {'type': 'colorTheme', 'dataSourceFieldId': 5, 'xmlValue': '<a:clrScheme
            xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Templafy_New"><a:dk1><a:srgbClr
            val="0078FF"/></a:dk1><a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr
            val="000000"/></a:dk2><a:lt2><a:srgbClr val="E5E5E5"/></a:lt2><a:accent1><a:srgbClr
            val="0078FF"/></a:accent1><a:accent2><a:srgbClr val="575757"/></a:accent2><a:accent3><a:srgbClr
            val="12AA96"/></a:accent3><a:accent4><a:srgbClr val="15436B"/></a:accent4><a:accent5><a:srgbClr
            val="D44849"/></a:accent5><a:accent6><a:srgbClr val="7F7F7F"/></a:accent6><a:hlink><a:srgbClr
            val="0078FF"/></a:hlink><a:folHlink><a:srgbClr val="55CBFF"/></a:folHlink></a:clrScheme>'}

    Attributes:
        type_ (str): Data source item field type.
        data_source_field_id (int): Data source field identifier.
        xml_value (str): The value of the field based on the schema
            http://schemas.openxmlformats.org/drawingml/2006/main. Max length is 3500 characters.
    """

    type_: str
    data_source_field_id: int
    xml_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert the object to a dictionary."""
        type_ = self.type_

        data_source_field_id = self.data_source_field_id

        xml_value = self.xml_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "dataSourceFieldId": data_source_field_id,
                "xmlValue": xml_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create an instance from a dictionary."""
        d = dict(src_dict)
        type_ = d.pop("type")

        data_source_field_id = d.pop("dataSourceFieldId")

        xml_value = d.pop("xmlValue")

        create_color_theme_data_source_item_field_request = cls(
            type_=type_,
            data_source_field_id=data_source_field_id,
            xml_value=xml_value,
        )

        create_color_theme_data_source_item_field_request.additional_properties = d
        return create_color_theme_data_source_item_field_request

    @property
    def additional_keys(self) -> list[str]:
        """Return the list of additional property keys."""
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
