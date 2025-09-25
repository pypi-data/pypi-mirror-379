from httpx import codes

from templafy.api.documents import (
    get_libraries_space_id_documents_folders_folder_id_assets as api,
)


def test_list_documents_in_folder_returns_document_list(
    httpx_mock, templafy_client, sample_document
):
    httpx_mock.add_response(status_code=codes.OK, json=[sample_document])

    result = api.sync(space_id=1, folder_id=1, client=templafy_client)

    assert isinstance(result, list)
    assert result[0].id == sample_document["id"]
