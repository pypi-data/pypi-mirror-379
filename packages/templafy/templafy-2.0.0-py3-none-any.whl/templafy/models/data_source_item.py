from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

if TYPE_CHECKING:
    from templafy.models.data_source_color_theme_item_field import (
        DataSourceColorThemeItemField,
    )
    from templafy.models.data_source_font_item_field import DataSourceFontItemField
    from templafy.models.data_source_image_item_field import DataSourceImageItemField
    from templafy.models.data_source_language_item_field import (
        DataSourceLanguageItemField,
    )
    from templafy.models.data_source_number_item_field import DataSourceNumberItemField
    from templafy.models.data_source_reference_item_field import (
        DataSourceReferenceItemField,
    )
    from templafy.models.data_source_text_item_field import DataSourceTextItemField

# Top-level runtime imports to satisfy PLC0415
from templafy.models.data_source_color_theme_item_field import (
    DataSourceColorThemeItemField,
)
from templafy.models.data_source_font_item_field import DataSourceFontItemField
from templafy.models.data_source_image_item_field import DataSourceImageItemField
from templafy.models.data_source_language_item_field import (
    DataSourceLanguageItemField,
)
from templafy.models.data_source_number_item_field import DataSourceNumberItemField
from templafy.models.data_source_reference_item_field import (
    DataSourceReferenceItemField,
)
from templafy.models.data_source_text_item_field import DataSourceTextItemField

T = TypeVar("T", bound="DataSourceItem")


@_attrs_define
class DataSourceItem:
    """Example:
        {'id': 638247997470215700, 'fields': [{'type': 'text', 'dataSourceFieldId': 0, 'value': 'Sample text'}, {'type':
            'number', 'dataSourceFieldId': 1, 'value': 123.4}, {'type': 'reference', 'dataSourceFieldId': 2, 'value':
            '638248473165588903'}, {'type': 'image', 'dataSourceFieldId': 3, 'fileName': 'Cat', 'fileUrl':
            'https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg'}, {'type': 'font', 'dataSourceFieldId': 4,
            'fileName': 'best-font', 'fileUrl': 'https://allfonts.com/best-font'}, {'type': 'colorTheme',
            'dataSourceFieldId': 5, 'xmlValue': '<a:clrScheme
            xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Templafy_New"><a:dk1><a:srgbClr
            val="0078FF"/></a:dk1><a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr
            val="000000"/></a:dk2><a:lt2><a:srgbClr val="E5E5E5"/></a:lt2><a:accent1><a:srgbClr
            val="0078FF"/></a:accent1><a:accent2><a:srgbClr val="575757"/></a:accent2><a:accent3><a:srgbClr
            val="12AA96"/></a:accent3><a:accent4><a:srgbClr val="15436B"/></a:accent4><a:accent5><a:srgbClr
            val="D44849"/></a:accent5><a:accent6><a:srgbClr val="7F7F7F"/></a:accent6><a:hlink><a:srgbClr
            val="0078FF"/></a:hlink><a:folHlink><a:srgbClr val="55CBFF"/></a:folHlink></a:clrScheme>'}, {'type': 'language',
            'dataSourceFieldId': 6, 'cultureName': 'en-GB'}]}

    Attributes:
        id (Union[Unset, int]): Unique data source item identifier.
        fields (Union[None, Unset, list[Union['DataSourceColorThemeItemField', 'DataSourceFontItemField',
            'DataSourceImageItemField', 'DataSourceLanguageItemField', 'DataSourceNumberItemField',
            'DataSourceReferenceItemField', 'DataSourceTextItemField']]]): The fields of the data source item.
    """

    id: Unset | int = UNSET
    fields: (
        None
        | Unset
        | list[
            Union[
                "DataSourceColorThemeItemField",
                "DataSourceFontItemField",
                "DataSourceImageItemField",
                "DataSourceLanguageItemField",
                "DataSourceNumberItemField",
                "DataSourceReferenceItemField",
                "DataSourceTextItemField",
            ]
        ]
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        # Top-level imports are used to avoid inline imports (PLC0415)

        id = self.id

        fields: None | Unset | list[dict[str, Any]]
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item: dict[str, Any]
                if isinstance(
                    fields_type_0_item_data,
                    (
                        DataSourceTextItemField,
                        DataSourceNumberItemField,
                        DataSourceReferenceItemField,
                        DataSourceImageItemField,
                        DataSourceLanguageItemField,
                        DataSourceFontItemField,
                    ),
                ):
                    fields_type_0_item = fields_type_0_item_data.to_dict()
                else:
                    fields_type_0_item = fields_type_0_item_data.to_dict()

                fields.append(fields_type_0_item)

        else:
            fields = self.fields

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        # Top-level imports are used to avoid inline imports (PLC0415)

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_fields(
            data: object,
        ) -> (
            None
            | Unset
            | list[
                Union[
                    "DataSourceColorThemeItemField",
                    "DataSourceFontItemField",
                    "DataSourceImageItemField",
                    "DataSourceLanguageItemField",
                    "DataSourceNumberItemField",
                    "DataSourceReferenceItemField",
                    "DataSourceTextItemField",
                ]
            ]
        ):
            """Create an instance from a dictionary."""
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in _fields_type_0:

                    def _parse_fields_type_0_item(
                        data: object,
                    ) -> Union[
                        "DataSourceColorThemeItemField",
                        "DataSourceFontItemField",
                        "DataSourceImageItemField",
                        "DataSourceLanguageItemField",
                        "DataSourceNumberItemField",
                        "DataSourceReferenceItemField",
                        "DataSourceTextItemField",
                    ]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_0 = (
                                DataSourceTextItemField.from_dict(data)
                            )

                            return fields_type_0_item_type_0
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_1 = (
                                DataSourceNumberItemField.from_dict(data)
                            )

                            return fields_type_0_item_type_1
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_2 = (
                                DataSourceReferenceItemField.from_dict(data)
                            )

                            return fields_type_0_item_type_2
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_3 = (
                                DataSourceImageItemField.from_dict(data)
                            )

                            return fields_type_0_item_type_3
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_4 = (
                                DataSourceLanguageItemField.from_dict(data)
                            )

                            return fields_type_0_item_type_4
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_5 = (
                                DataSourceFontItemField.from_dict(data)
                            )

                            return fields_type_0_item_type_5
                        except:  # noqa: E722
                            pass
                        if not isinstance(data, dict):
                            raise TypeError
                        fields_type_0_item_type_6 = (
                            DataSourceColorThemeItemField.from_dict(data)
                        )

                        return fields_type_0_item_type_6

                    fields_type_0_item = _parse_fields_type_0_item(
                        fields_type_0_item_data
                    )

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except:  # noqa: E722
                pass
            return cast(
                "None | Unset | list[DataSourceColorThemeItemField | DataSourceFontItemField | DataSourceImageItemField | DataSourceLanguageItemField | DataSourceNumberItemField | DataSourceReferenceItemField | DataSourceTextItemField]",
                data,
            )

        fields = _parse_fields(d.pop("fields", UNSET))

        data_source_item = cls(
            id=id,
            fields=fields,
        )

        return data_source_item
