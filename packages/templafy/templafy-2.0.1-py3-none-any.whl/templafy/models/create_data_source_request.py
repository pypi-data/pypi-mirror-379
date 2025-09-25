from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

if TYPE_CHECKING:
    from templafy.models.create_image_field_schema_request import (
        CreateImageFieldSchemaRequest,
    )
    from templafy.models.create_number_field_schema_request import (
        CreateNumberFieldSchemaRequest,
    )
    from templafy.models.create_reference_field_schema_request import (
        CreateReferenceFieldSchemaRequest,
    )
    from templafy.models.create_text_field_schema_request import (
        CreateTextFieldSchemaRequest,
    )

# Runtime imports moved to top-level to satisfy PLC0415
from templafy.models.create_image_field_schema_request import (
    CreateImageFieldSchemaRequest,
)
from templafy.models.create_number_field_schema_request import (
    CreateNumberFieldSchemaRequest,
)
from templafy.models.create_reference_field_schema_request import (
    CreateReferenceFieldSchemaRequest,
)
from templafy.models.create_text_field_schema_request import (
    CreateTextFieldSchemaRequest,
)

T = TypeVar("T", bound="CreateDataSourceRequest")


@_attrs_define
class CreateDataSourceRequest:
    """Example:
        {'name': 'Cities', 'description': 'Cities in which we have offices', 'fields': [{'name': 'History', 'type':
            'text', 'isMultipleLines': True, 'defaultValue': 'The city was established in the year 1652 by Dutch
            explorers...', 'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId': '637989101951089955',
            'defaultReferencedItemId': '638249311425155568', 'isRequired': True}, {'name': 'Flag', 'type': 'image',
            'isRequired': True}]}

    Attributes:
        name (str): The name of the data source. It must be unique. Max length is 100 characters.
        description (Union[None, Unset, str]): The description of the data source.
        fields (Union[None, Unset, list[Union['CreateImageFieldSchemaRequest', 'CreateNumberFieldSchemaRequest',
            'CreateReferenceFieldSchemaRequest', 'CreateTextFieldSchemaRequest']]]): The fields of the data source. If not
            specified, the data source will be created without fields.
    """

    name: str
    description: None | Unset | str = UNSET
    fields: (
        None
        | Unset
        | list[
            Union[
                "CreateImageFieldSchemaRequest",
                "CreateNumberFieldSchemaRequest",
                "CreateReferenceFieldSchemaRequest",
                "CreateTextFieldSchemaRequest",
            ]
        ]
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        """Convert the object to a dictionary."""
        # Imports moved to module top-level to satisfy linter PLC0415

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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
                        CreateTextFieldSchemaRequest,
                        CreateNumberFieldSchemaRequest,
                        CreateImageFieldSchemaRequest,
                    ),
                ):
                    fields_type_0_item = fields_type_0_item_data.to_dict()
                else:
                    fields_type_0_item = fields_type_0_item_data.to_dict()

                fields.append(fields_type_0_item)

        else:
            fields = self.fields

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create an instance from a dictionary."""
        # Imports moved to module top-level to satisfy linter PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_fields(
            data: object,
        ) -> (
            None
            | Unset
            | list[
                Union[
                    "CreateImageFieldSchemaRequest",
                    "CreateNumberFieldSchemaRequest",
                    "CreateReferenceFieldSchemaRequest",
                    "CreateTextFieldSchemaRequest",
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
                        "CreateImageFieldSchemaRequest",
                        "CreateNumberFieldSchemaRequest",
                        "CreateReferenceFieldSchemaRequest",
                        "CreateTextFieldSchemaRequest",
                    ]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_0 = (
                                CreateTextFieldSchemaRequest.from_dict(data)
                            )

                            return fields_type_0_item_type_0
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_1 = (
                                CreateNumberFieldSchemaRequest.from_dict(data)
                            )

                            return fields_type_0_item_type_1
                        except:  # noqa: E722
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError
                            fields_type_0_item_type_2 = (
                                CreateImageFieldSchemaRequest.from_dict(data)
                            )

                            return fields_type_0_item_type_2
                        except:  # noqa: E722
                            pass
                        if not isinstance(data, dict):
                            raise TypeError
                        fields_type_0_item_type_3 = (
                            CreateReferenceFieldSchemaRequest.from_dict(data)
                        )

                        return fields_type_0_item_type_3

                    fields_type_0_item = _parse_fields_type_0_item(
                        fields_type_0_item_data
                    )

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except:  # noqa: E722
                pass
            return cast(
                "None | Unset | list[CreateImageFieldSchemaRequest | CreateNumberFieldSchemaRequest | CreateReferenceFieldSchemaRequest | CreateTextFieldSchemaRequest]",
                data,
            )

        fields = _parse_fields(d.pop("fields", UNSET))

        create_data_source_request = cls(
            name=name,
            description=description,
            fields=fields,
        )

        return create_data_source_request
