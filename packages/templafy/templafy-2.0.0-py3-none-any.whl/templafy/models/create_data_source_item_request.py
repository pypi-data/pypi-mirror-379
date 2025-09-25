from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

if TYPE_CHECKING:
    from templafy.models.create_color_theme_data_source_item_field_request import (
        CreateColorThemeDataSourceItemFieldRequest,
    )
    from templafy.models.create_font_data_source_item_field_request import (
        CreateFontDataSourceItemFieldRequest,
    )
    from templafy.models.create_image_data_source_item_field_request import (
        CreateImageDataSourceItemFieldRequest,
    )
    from templafy.models.create_number_data_source_item_field_request import (
        CreateNumberDataSourceItemFieldRequest,
    )
    from templafy.models.create_reference_data_source_item_field_request import (
        CreateReferenceDataSourceItemFieldRequest,
    )
    from templafy.models.create_text_data_source_item_field_request import (
        CreateTextDataSourceItemFieldRequest,
    )
from templafy.models.create_color_theme_data_source_item_field_request import (
    CreateColorThemeDataSourceItemFieldRequest,
)
from templafy.models.create_font_data_source_item_field_request import (
    CreateFontDataSourceItemFieldRequest,
)
from templafy.models.create_image_data_source_item_field_request import (
    CreateImageDataSourceItemFieldRequest,
)
from templafy.models.create_number_data_source_item_field_request import (
    CreateNumberDataSourceItemFieldRequest,
)
from templafy.models.create_reference_data_source_item_field_request import (
    CreateReferenceDataSourceItemFieldRequest,
)
from templafy.models.create_text_data_source_item_field_request import (
    CreateTextDataSourceItemFieldRequest,
)

T = TypeVar("T", bound="CreateDataSourceItemRequest")


@_attrs_define
class CreateDataSourceItemRequest:
    """Example:
        {'fields': [{'dataSourceFieldId': 0, 'type': 'text', 'value': 'Sample text'}, {'dataSourceFieldId': 1, 'type':
            'number', 'value': 123.45}, {'dataSourceFieldId': 2, 'type': 'reference', 'dataSourceItemId':
            '638247997437572264'}, {'dataSourceFieldId': 3, 'type': 'image', 'fileName': 'Cat', 'fileUrl':
            'https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg'}, {'dataSourceFieldId': 4, 'type': 'font',
            'fileName': 'best-font', 'fileUrl': 'https://allfonts.com/best-font'}, {'dataSourceFieldId': 5, 'type':
            'colorTheme', 'xmlValue': '<a:clrScheme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
            name="Templafy_New"><a:dk1><a:srgbClr val="0078FF"/></a:dk1><a:lt1><a:sysClr val="window"
            lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="000000"/></a:dk2><a:lt2><a:srgbClr
            val="E5E5E5"/></a:lt2><a:accent1><a:srgbClr val="0078FF"/></a:accent1><a:accent2><a:srgbClr
            val="575757"/></a:accent2><a:accent3><a:srgbClr val="12AA96"/></a:accent3><a:accent4><a:srgbClr
            val="15436B"/></a:accent4><a:accent5><a:srgbClr val="D44849"/></a:accent5><a:accent6><a:srgbClr
            val="7F7F7F"/></a:accent6><a:hlink><a:srgbClr val="0078FF"/></a:hlink><a:folHlink><a:srgbClr
            val="55CBFF"/></a:folHlink></a:clrScheme>'}]}

    Attributes:
        fields (Union[None, Unset, list[Union['CreateColorThemeDataSourceItemFieldRequest',
            'CreateFontDataSourceItemFieldRequest', 'CreateImageDataSourceItemFieldRequest',
            'CreateNumberDataSourceItemFieldRequest', 'CreateReferenceDataSourceItemFieldRequest',
            'CreateTextDataSourceItemFieldRequest']]]): The fields of the data source item.
    """

    fields: (
        None
        | Unset
        | list[
            Union[
                "CreateColorThemeDataSourceItemFieldRequest",
                "CreateFontDataSourceItemFieldRequest",
                "CreateImageDataSourceItemFieldRequest",
                "CreateNumberDataSourceItemFieldRequest",
                "CreateReferenceDataSourceItemFieldRequest",
                "CreateTextDataSourceItemFieldRequest",
            ]
        ]
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        """Convert the object to a dictionary."""
        # Top-level imports are used to avoid inline imports (PLC0415)

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
                        CreateTextDataSourceItemFieldRequest,
                        CreateNumberDataSourceItemFieldRequest,
                        CreateReferenceDataSourceItemFieldRequest,
                        CreateImageDataSourceItemFieldRequest,
                        CreateFontDataSourceItemFieldRequest,
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
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create an instance from a dictionary."""
        # Top-level imports are used to avoid inline imports (PLC0415)

        d = dict(src_dict)

        def _parse_fields(
            data: object,
        ) -> (
            None
            | Unset
            | list[
                Union[
                    "CreateColorThemeDataSourceItemFieldRequest",
                    "CreateFontDataSourceItemFieldRequest",
                    "CreateImageDataSourceItemFieldRequest",
                    "CreateNumberDataSourceItemFieldRequest",
                    "CreateReferenceDataSourceItemFieldRequest",
                    "CreateTextDataSourceItemFieldRequest",
                ]
            ]
        ):
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
                        "CreateColorThemeDataSourceItemFieldRequest",
                        "CreateFontDataSourceItemFieldRequest",
                        "CreateImageDataSourceItemFieldRequest",
                        "CreateNumberDataSourceItemFieldRequest",
                        "CreateReferenceDataSourceItemFieldRequest",
                        "CreateTextDataSourceItemFieldRequest",
                    ]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_0 = (
                                CreateTextDataSourceItemFieldRequest.from_dict(data)
                            )

                            return fields_type_0_item_type_0
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_1 = (
                                CreateNumberDataSourceItemFieldRequest.from_dict(data)
                            )

                            return fields_type_0_item_type_1
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_2 = (
                                CreateReferenceDataSourceItemFieldRequest.from_dict(
                                    data
                                )
                            )

                            return fields_type_0_item_type_2
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_3 = (
                                CreateImageDataSourceItemFieldRequest.from_dict(data)
                            )

                            return fields_type_0_item_type_3
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_4 = (
                                CreateFontDataSourceItemFieldRequest.from_dict(data)
                            )

                            return fields_type_0_item_type_4
                        except:  # noqa: E722
                            pass
                        if not isinstance(data, dict):
                            raise TypeError
                        fields_type_0_item_type_5 = (
                            CreateColorThemeDataSourceItemFieldRequest.from_dict(data)
                        )

                        return fields_type_0_item_type_5

                    fields_type_0_item = _parse_fields_type_0_item(
                        fields_type_0_item_data
                    )

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except:  # noqa: E722
                pass
            return cast(
                "None | Unset | list[CreateColorThemeDataSourceItemFieldRequest | CreateFontDataSourceItemFieldRequest | CreateImageDataSourceItemFieldRequest | CreateNumberDataSourceItemFieldRequest | CreateReferenceDataSourceItemFieldRequest | CreateTextDataSourceItemFieldRequest]",
                data,
            )

        fields = _parse_fields(d.pop("fields", UNSET))

        create_data_source_item_request = cls(
            fields=fields,
        )

        return create_data_source_item_request
