from httpx import codes

from templafy.api.documents import (
    get_libraries_space_id_documents_assets_asset_id as api,
)


def test_get_document_by_id_returns_parsed_list(
    httpx_mock, templafy_client, sample_document
):
    # stub httpx response
    httpx_mock.add_response(status_code=codes.OK, json=[sample_document])

    result = api.sync(space_id=1, asset_id=123, client=templafy_client)

    assert isinstance(result, list)
    assert result[0].id == sample_document["id"]
