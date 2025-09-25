from httpx import codes

from templafy.api.documents import (
    post_libraries_space_id_documents_assets_asset_id_generate as api,
)
from templafy.models.generate_file_request import GenerateFileRequest


def test_generate_document_returns_expected_payload(httpx_mock, templafy_client):
    body = GenerateFileRequest(email="test@example.com")
    payload = {
        "downloadUrl": "https://example.com/generated.docx",
        "fileSize": 1024,
        "checksum": "abc123",
        "mimeType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "fileExtension": "docx",
    }
    httpx_mock.add_response(status_code=codes.OK, json=payload)

    result = api.sync(space_id=1, asset_id=123, client=templafy_client, body=body)

    assert result is not None
    assert result.download_url == payload["downloadUrl"]
