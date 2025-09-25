from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

if TYPE_CHECKING:
    from templafy.models.color_theme_field_schema import ColorThemeFieldSchema
    from templafy.models.font_field_schema import FontFieldSchema
    from templafy.models.image_field_schema import ImageFieldSchema
    from templafy.models.language_field_schema import LanguageFieldSchema
    from templafy.models.number_field_schema import NumberFieldSchema
    from templafy.models.reference_field_schema import ReferenceFieldSchema
    from templafy.models.text_field_schema import TextFieldSchema

# Top-level runtime imports to satisfy PLC0415
from templafy.models.color_theme_field_schema import ColorThemeFieldSchema
from templafy.models.font_field_schema import FontFieldSchema
from templafy.models.image_field_schema import ImageFieldSchema
from templafy.models.language_field_schema import LanguageFieldSchema
from templafy.models.number_field_schema import NumberFieldSchema
from templafy.models.reference_field_schema import ReferenceFieldSchema
from templafy.models.text_field_schema import TextFieldSchema

T = TypeVar("T", bound="DataSource")


@_attrs_define
class DataSource:
    """Example:
        {'id': '638247997499047080', 'name': 'Cities', 'description': 'Cities in which we have offices', 'fields':
            [{'id': 0, 'name': 'Name', 'type': 'text', 'isRequired': True, 'isLocked': True, 'isMultipleLines': False},
            {'id': 1, 'name': 'History', 'type': 'text', 'isRequired': False, 'isLocked': False, 'isMultipleLines': True,
            'defaultValue': 'The city was established in the year 1652 by Dutch explorers...'}, {'id': 2, 'name':
            'Population', 'type': 'number', 'isRequired': True, 'isLocked': False, 'defaultValue': 100222}, {'id': 3,
            'name': 'Country', 'type': 'reference', 'isRequired': True, 'isLocked': False, 'defaultValue':
            '638247997437572266', 'referenceDataSourceId': '638247997437572264'}, {'id': 4, 'name': 'Flag', 'type': 'image',
            'isRequired': False, 'isLocked': False}, {'id': 5, 'name': 'PreferredLanguage', 'type': 'language',
            'isRequired': False, 'isLocked': False, 'defaultValue': 'German'}, {'id': 6, 'name': 'PreferredFont', 'type':
            'font', 'isRequired': False, 'isLocked': False}, {'id': 7, 'name': 'PreferredColourTheme', 'type': 'colorTheme',
            'isRequired': False, 'isLocked': False}]}

    Attributes:
        id (int): Unique data source identifier.
        name (str): Data source name. It must be unique.
        fields (list[Union['ColorThemeFieldSchema', 'FontFieldSchema', 'ImageFieldSchema', 'LanguageFieldSchema',
            'NumberFieldSchema', 'ReferenceFieldSchema', 'TextFieldSchema']]):
        description (Union[None, Unset, str]): Data source description.
    """

    id: int
    name: str
    fields: list[
        Union[
            "ColorThemeFieldSchema",
            "FontFieldSchema",
            "ImageFieldSchema",
            "LanguageFieldSchema",
            "NumberFieldSchema",
            "ReferenceFieldSchema",
            "TextFieldSchema",
        ]
    ]
    description: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        """Convert the object to a dictionary."""
        # Top-level imports are used to avoid inline imports (PLC0415)

        id = self.id

        name = self.name

        fields = []
        for fields_item_data in self.fields:
            fields_item: dict[str, Any]
            if isinstance(
                fields_item_data,
                (
                    TextFieldSchema,
                    NumberFieldSchema,
                    ReferenceFieldSchema,
                    ImageFieldSchema,
                    LanguageFieldSchema,
                    FontFieldSchema,
                ),
            ):
                fields_item = fields_item_data.to_dict()
            else:
                fields_item = fields_item_data.to_dict()

            fields.append(fields_item)

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "fields": fields,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create an instance from a dictionary."""
        # Top-level imports are used to avoid inline imports (PLC0415)

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:

            def _parse_fields_item(
                data: object,
            ) -> Union[
                "ColorThemeFieldSchema",
                "FontFieldSchema",
                "ImageFieldSchema",
                "LanguageFieldSchema",
                "NumberFieldSchema",
                "ReferenceFieldSchema",
                "TextFieldSchema",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_0 = TextFieldSchema.from_dict(data)

                    return fields_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_1 = NumberFieldSchema.from_dict(data)

                    return fields_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_2 = ReferenceFieldSchema.from_dict(data)

                    return fields_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_3 = ImageFieldSchema.from_dict(data)

                    return fields_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_4 = LanguageFieldSchema.from_dict(data)

                    return fields_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError
                    fields_item_type_5 = FontFieldSchema.from_dict(data)

                    return fields_item_type_5
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError
                fields_item_type_6 = ColorThemeFieldSchema.from_dict(data)

                return fields_item_type_6

            fields_item = _parse_fields_item(fields_item_data)

            fields.append(fields_item)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        description = _parse_description(d.pop("description", UNSET))

        data_source = cls(
            id=id,
            name=name,
            fields=fields,
            description=description,
        )

        return data_source
