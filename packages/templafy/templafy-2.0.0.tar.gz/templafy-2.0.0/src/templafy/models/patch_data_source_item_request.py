from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.models.patch_color_theme_data_source_item_field_request import (
    PatchColorThemeDataSourceItemFieldRequest,
)
from templafy.models.patch_font_data_source_item_field_request import (
    PatchFontDataSourceItemFieldRequest,
)
from templafy.models.patch_image_data_source_item_field_request import (
    PatchImageDataSourceItemFieldRequest,
)
from templafy.models.patch_number_data_source_item_field_request import (
    PatchNumberDataSourceItemFieldRequest,
)
from templafy.models.patch_reference_data_source_item_field_request import (
    PatchReferenceDataSourceItemFieldRequest,
)
from templafy.models.patch_text_data_source_item_field_request import (
    PatchTextDataSourceItemFieldRequest,
)

T = TypeVar("T", bound="PatchDataSourceItemRequest")


@_attrs_define
class PatchDataSourceItemRequest:
    """Attributes:
    fields (list[Union['PatchColorThemeDataSourceItemFieldRequest', 'PatchFontDataSourceItemFieldRequest',
        'PatchImageDataSourceItemFieldRequest', 'PatchNumberDataSourceItemFieldRequest',
        'PatchReferenceDataSourceItemFieldRequest', 'PatchTextDataSourceItemFieldRequest']]): The fields of the data
        source item.
    """

    fields: list[
        Union[
            "PatchColorThemeDataSourceItemFieldRequest",
            "PatchFontDataSourceItemFieldRequest",
            "PatchImageDataSourceItemFieldRequest",
            "PatchNumberDataSourceItemFieldRequest",
            "PatchReferenceDataSourceItemFieldRequest",
            "PatchTextDataSourceItemFieldRequest",
        ]
    ]

    def to_dict(self) -> dict[str, Any]:
        """Return a dictionary representation of the model."""
        fields = []
        for fields_item_data in self.fields:
            fields_item: dict[str, Any]
            if isinstance(
                fields_item_data,
                (
                    PatchTextDataSourceItemFieldRequest,
                    PatchNumberDataSourceItemFieldRequest,
                    PatchImageDataSourceItemFieldRequest,
                    PatchReferenceDataSourceItemFieldRequest,
                    PatchFontDataSourceItemFieldRequest,
                ),
            ):
                fields_item = fields_item_data.to_dict()
            else:
                fields_item = fields_item_data.to_dict()

            fields.append(fields_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        # model classes are imported at module level to satisfy linter PLC0415
        """Create a PatchDataSourceItemRequest instance from a mapping/dict.

        Args:
            src_dict: Mapping representation of the model.

        Returns:
            An instantiated PatchDataSourceItemRequest.
        """

        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:

            def _parse_fields_item(
                data: object,
            ) -> Union[
                "PatchColorThemeDataSourceItemFieldRequest",
                "PatchFontDataSourceItemFieldRequest",
                "PatchImageDataSourceItemFieldRequest",
                "PatchNumberDataSourceItemFieldRequest",
                "PatchReferenceDataSourceItemFieldRequest",
                "PatchTextDataSourceItemFieldRequest",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_0 = PatchTextDataSourceItemFieldRequest.from_dict(
                        data
                    )

                    return fields_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_1 = (
                        PatchNumberDataSourceItemFieldRequest.from_dict(data)
                    )

                    return fields_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_2 = PatchImageDataSourceItemFieldRequest.from_dict(
                        data
                    )

                    return fields_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_3 = (
                        PatchReferenceDataSourceItemFieldRequest.from_dict(data)
                    )

                    return fields_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_4 = PatchFontDataSourceItemFieldRequest.from_dict(
                        data
                    )

                    return fields_item_type_4
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError
                fields_item_type_5 = (
                    PatchColorThemeDataSourceItemFieldRequest.from_dict(data)
                )

                return fields_item_type_5

            fields_item = _parse_fields_item(fields_item_data)

            fields.append(fields_item)

        patch_data_source_item_request = cls(
            fields=fields,
        )

        return patch_data_source_item_request
