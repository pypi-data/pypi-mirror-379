from httpx import codes

from templafy.api.libraries import get_libraries


def test_get_libraries_returns_list(httpx_mock, templafy_client, sample_library_data):
    # Mock httpx response
    httpx_mock.add_response(status_code=codes.OK, json=sample_library_data)

    result = get_libraries.sync(client=templafy_client)

    assert isinstance(result, list)
