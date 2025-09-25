from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="CreateReferenceFieldSchemaRequest")


@_attrs_define
class CreateReferenceFieldSchemaRequest:
    """Example:
        {'name': 'Country', 'type': 'reference', 'referenceDataSourceId': '637989101951089955',
            'defaultReferencedItemId': '638249311425155568', 'isRequired': True}

    Attributes:
        type_ (str): Data source field schema type.
        name (str): The name of the field. It must be unique within the data source.
        reference_data_source_id (int): The id of the data source that the field references.
        is_required (Union[Unset, bool]): Whether the field is required. If true, the field must be filled in when
            creating a data source item.
        default_referenced_item_id (Union[None, Unset, int]): The default value of the field. If specified, the field
            will be pre-filled with this value when creating a data source item.
    """

    type_: str
    name: str
    reference_data_source_id: int
    is_required: Unset | bool = UNSET
    default_referenced_item_id: None | Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        reference_data_source_id = self.reference_data_source_id

        is_required = self.is_required

        default_referenced_item_id: None | Unset | int
        if isinstance(self.default_referenced_item_id, Unset):
            default_referenced_item_id = UNSET
        else:
            default_referenced_item_id = self.default_referenced_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "referenceDataSourceId": reference_data_source_id,
            }
        )
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if default_referenced_item_id is not UNSET:
            field_dict["defaultReferencedItemId"] = default_referenced_item_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        reference_data_source_id = d.pop("referenceDataSourceId")

        is_required = d.pop("isRequired", UNSET)

        def _parse_default_referenced_item_id(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | int", data)

        default_referenced_item_id = _parse_default_referenced_item_id(
            d.pop("defaultReferencedItemId", UNSET)
        )

        create_reference_field_schema_request = cls(
            type_=type_,
            name=name,
            reference_data_source_id=reference_data_source_id,
            is_required=is_required,
            default_referenced_item_id=default_referenced_item_id,
        )

        create_reference_field_schema_request.additional_properties = d
        return create_reference_field_schema_request

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
