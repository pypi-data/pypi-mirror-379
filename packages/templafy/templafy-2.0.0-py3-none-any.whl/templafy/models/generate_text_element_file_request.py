from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="GenerateTextElementFileRequest")


@_attrs_define
class GenerateTextElementFileRequest:
    """The request model to generate a text element file.

    Example:
        {'email': 'templafy@templafy.com', 'data': {'Language': 'en-us'}}

    Attributes:
        email (str): Email to be used for identification.
        data (Union[Unset, Any]): Data to be used during the file generation.
    """

    email: str
    data: Unset | Any = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        data = d.pop("data", UNSET)

        generate_text_element_file_request = cls(
            email=email,
            data=data,
        )

        return generate_text_element_file_request
