from httpx import codes

from templafy.api.libraries import get_libraries_space_id_library_type
from templafy.models.library_type import LibraryType


def test_get_library_by_space_and_type_returns_details(
    httpx_mock, templafy_client, sample_library_details_data
):
    # Mock httpx response
    httpx_mock.add_response(status_code=codes.OK, json=sample_library_details_data)

    result = get_libraries_space_id_library_type.sync(
        space_id=1, library_type=LibraryType.DOCUMENTS, client=templafy_client
    )

    assert result is not None
    assert result.root_folder_id == sample_library_details_data["rootFolderId"]
