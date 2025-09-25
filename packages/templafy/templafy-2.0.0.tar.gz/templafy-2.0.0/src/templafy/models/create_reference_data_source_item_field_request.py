from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="CreateReferenceDataSourceItemFieldRequest")


@_attrs_define
class CreateReferenceDataSourceItemFieldRequest:
    """Example:
        {'dataSourceFieldId': 2, 'type': 'reference', 'dataSourceItemId': '638247997437572264'}

    Attributes:
        type_ (str): Data source item field type.
        data_source_field_id (int): Data source field identifier.
        data_source_item_id (int): The identifier of the data source item to be referenced.
    """

    type_: str
    data_source_field_id: int
    data_source_item_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        data_source_field_id = self.data_source_field_id

        data_source_item_id = self.data_source_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "dataSourceFieldId": data_source_field_id,
                "dataSourceItemId": data_source_item_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        data_source_field_id = d.pop("dataSourceFieldId")

        data_source_item_id = d.pop("dataSourceItemId")

        create_reference_data_source_item_field_request = cls(
            type_=type_,
            data_source_field_id=data_source_field_id,
            data_source_item_id=data_source_item_id,
        )

        create_reference_data_source_item_field_request.additional_properties = d
        return create_reference_data_source_item_field_request

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
