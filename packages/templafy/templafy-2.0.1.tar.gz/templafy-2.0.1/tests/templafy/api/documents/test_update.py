from httpx import codes

from templafy.api.documents import (
    patch_libraries_space_id_documents_assets_asset_id as api,
)
from templafy.models.patch_libraries_space_id_documents_assets_asset_id_body import (
    PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody,
)


def test_update_document_returns_none_on_204(httpx_mock, templafy_client):
    httpx_mock.add_response(status_code=codes.NO_CONTENT)

    body = PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody()
    result = api.sync(space_id=1, asset_id=123, client=templafy_client, body=body)

    assert result is None
