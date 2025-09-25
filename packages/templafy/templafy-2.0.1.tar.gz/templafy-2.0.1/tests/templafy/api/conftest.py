import pytest


@pytest.fixture
def sample_library_data():
    """Sample library data for testing get_libraries."""
    return [
        {
            "id": 1,
            "name": "Test Library",
            "libraryType": "documents",
            "spaceId": 1,
            "rootFolderId": 1,
        }
    ]


@pytest.fixture
def sample_library_details_data():
    """Sample library details data for testing get_libraries_space_id_library_type."""
    return {
        "id": 1,
        "name": "Test Library Details",
        "libraryType": "documents",
        "spaceId": 1,
        "rootFolderId": 1,
    }
