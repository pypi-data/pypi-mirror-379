from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="GeneratedFile")


@_attrs_define
class GeneratedFile:
    """The generated file response model.

    Attributes:
        download_url (str): Temporary access URL for generated file.
        file_size (int): File size in bytes.
        checksum (str): MD5 checksum of the bytes.
        mime_type (str): Mime type of the generated file.
        file_extension (str): Suffix to the name of the file.
        pdf_download_url (Union[None, Unset, str]): Temporary access URL for generated PDF file. Only available if the
            file was converted to PDF.
    """

    download_url: str
    file_size: int
    checksum: str
    mime_type: str
    file_extension: str
    pdf_download_url: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        download_url = self.download_url

        file_size = self.file_size

        checksum = self.checksum

        mime_type = self.mime_type

        file_extension = self.file_extension

        pdf_download_url: None | Unset | str
        if isinstance(self.pdf_download_url, Unset):
            pdf_download_url = UNSET
        else:
            pdf_download_url = self.pdf_download_url

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
        if pdf_download_url is not UNSET:
            field_dict["pdfDownloadUrl"] = pdf_download_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        download_url = d.pop("downloadUrl")

        file_size = d.pop("fileSize")

        checksum = d.pop("checksum")

        mime_type = d.pop("mimeType")

        file_extension = d.pop("fileExtension")

        def _parse_pdf_download_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        pdf_download_url = _parse_pdf_download_url(d.pop("pdfDownloadUrl", UNSET))

        generated_file = cls(
            download_url=download_url,
            file_size=file_size,
            checksum=checksum,
            mime_type=mime_type,
            file_extension=file_extension,
            pdf_download_url=pdf_download_url,
        )

        return generated_file
