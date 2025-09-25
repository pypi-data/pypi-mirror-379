from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="GeneratedTextElementFile")


@_attrs_define
class GeneratedTextElementFile:
    """The generated text element file response model.

    Attributes:
        download_url (str): Temporary access URL for generated file.
        file_size (int): File size in bytes.
        checksum (str): MD5 checksum of the bytes.
        mime_type (str): Mime type of the generated file.
        file_extension (str): Suffix to the name of the file.
    """

    download_url: str
    file_size: int
    checksum: str
    mime_type: str
    file_extension: str

    def to_dict(self) -> dict[str, Any]:
        download_url = self.download_url

        file_size = self.file_size

        checksum = self.checksum

        mime_type = self.mime_type

        file_extension = self.file_extension

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "downloadUrl": download_url,
                "fileSize": file_size,
                "checksum": checksum,
                "mimeType": mime_type,
                "fileExtension": file_extension,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        download_url = d.pop("downloadUrl")

        file_size = d.pop("fileSize")

        checksum = d.pop("checksum")

        mime_type = d.pop("mimeType")

        file_extension = d.pop("fileExtension")

        generated_text_element_file = cls(
            download_url=download_url,
            file_size=file_size,
            checksum=checksum,
            mime_type=mime_type,
            file_extension=file_extension,
        )

        return generated_text_element_file
