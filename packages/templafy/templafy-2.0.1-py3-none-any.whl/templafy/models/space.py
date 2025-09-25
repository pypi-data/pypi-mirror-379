from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Space")


@_attrs_define
class Space:
    """Example:
        {'id': 541244332157142140, 'name': 'Global Brand'}

    Attributes:
        id (int): Unique Space identifier
        name (str): Space name
    """

    id: int
    name: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        space = cls(
            id=id,
            name=name,
        )

        return space
