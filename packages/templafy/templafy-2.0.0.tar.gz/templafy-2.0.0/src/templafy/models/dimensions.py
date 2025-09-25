from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="Dimensions")


@_attrs_define
class Dimensions:
    """Asset dimensions

    Attributes:
        height (int): Height of the asset in pixels
        width (int): Width of the asset in pixels
        aspect_ratio (Union[None, Unset, str]):
    """

    height: int
    width: int
    aspect_ratio: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        width = self.width

        aspect_ratio: None | Unset | str
        if isinstance(self.aspect_ratio, Unset):
            aspect_ratio = UNSET
        else:
            aspect_ratio = self.aspect_ratio

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "height": height,
                "width": width,
            }
        )
        if aspect_ratio is not UNSET:
            field_dict["aspectRatio"] = aspect_ratio

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        height = d.pop("height")

        width = d.pop("width")

        def _parse_aspect_ratio(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        aspect_ratio = _parse_aspect_ratio(d.pop("aspectRatio", UNSET))

        dimensions = cls(
            height=height,
            width=width,
            aspect_ratio=aspect_ratio,
        )

        return dimensions
