from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.models.source_entity_type import SourceEntityType
from templafy.types import UNSET, Unset

T = TypeVar("T", bound="Dependency")


@_attrs_define
class Dependency:
    """The model describing a dependency.

    Attributes:
        source_entity_type (Union[Unset, SourceEntityType]):
        source_entity_id (Union[None, Unset, str]): The id of the dependency source.
        description (Union[None, Unset, str]): Human readable description of the source type.
    """

    source_entity_type: Unset | SourceEntityType = UNSET
    source_entity_id: None | Unset | str = UNSET
    description: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        source_entity_type: Unset | str = UNSET
        if not isinstance(self.source_entity_type, Unset):
            source_entity_type = self.source_entity_type.value

        source_entity_id: None | Unset | str
        if isinstance(self.source_entity_id, Unset):
            source_entity_id = UNSET
        else:
            source_entity_id = self.source_entity_id

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if source_entity_type is not UNSET:
            field_dict["sourceEntityType"] = source_entity_type
        if source_entity_id is not UNSET:
            field_dict["sourceEntityId"] = source_entity_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _source_entity_type = d.pop("sourceEntityType", UNSET)
        source_entity_type: Unset | SourceEntityType
        if isinstance(_source_entity_type, Unset):
            source_entity_type = UNSET
        else:
            source_entity_type = SourceEntityType(_source_entity_type)

        def _parse_source_entity_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        source_entity_id = _parse_source_entity_id(d.pop("sourceEntityId", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        description = _parse_description(d.pop("description", UNSET))

        dependency = cls(
            source_entity_type=source_entity_type,
            source_entity_id=source_entity_id,
            description=description,
        )

        return dependency
