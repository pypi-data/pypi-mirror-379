from io import BytesIO

from httpx import codes

from templafy.api.documents import (
    post_libraries_space_id_documents_folders_folder_id_assets as api,
)
from templafy.models.post_libraries_space_id_documents_folders_folder_id_assets_body import (
    PostLibrariesSpaceIdDocumentsFoldersFolderIdAssetsBody,
)
from templafy.types import File


def test_create_document_returns_document(httpx_mock, templafy_client):
    # Create mock file
    mock_file = File(
        payload=BytesIO(b"mock file content"),
        file_name="test.docx",
        mime_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
    body = PostLibrariesSpaceIdDocumentsFoldersFolderIdAssetsBody(file=mock_file)

    httpx_mock.add_response(status_code=codes.CREATED, json=123)

    result = api.sync(space_id=1, folder_id=1, client=templafy_client, body=body)

    assert result == 123
