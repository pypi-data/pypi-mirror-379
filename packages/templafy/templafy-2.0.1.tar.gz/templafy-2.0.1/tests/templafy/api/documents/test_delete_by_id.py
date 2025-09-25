from httpx import codes

from templafy.api.documents import (
    delete_libraries_space_id_documents_assets_asset_id as api,
)


def test_delete_document_by_id_returns_none_on_204(httpx_mock, templafy_client):
    httpx_mock.add_response(status_code=codes.NO_CONTENT)

    result = api.sync(space_id=1, asset_id=123, client=templafy_client)

    assert result is None
