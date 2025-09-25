from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="GenerateFileRequest")


@_attrs_define
class GenerateFileRequest:
    """The request model to generate a file.

    Example:
        {'email': 'templafy@templafy.com', 'data': {'Language': 'en-us'}, 'includePdf': True}

    Attributes:
        email (str): Email to be used for identification.
        data (Union[Unset, Any]): Data to be used during the file generation.
        include_pdf (Union[Unset, bool]): Specifies whether a PDF export of the file should be included in the response.
    """

    email: str
    data: Unset | Any = UNSET
    include_pdf: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        data = self.data

        include_pdf = self.include_pdf

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if include_pdf is not UNSET:
            field_dict["includePdf"] = include_pdf

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        data = d.pop("data", UNSET)

        include_pdf = d.pop("includePdf", UNSET)

        generate_file_request = cls(
            email=email,
            data=data,
            include_pdf=include_pdf,
        )

        return generate_file_request
