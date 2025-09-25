from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.folder import Folder
from templafy.models.library_type import LibraryType
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.types import Response


def _get_kwargs(
    space_id: int,
    library_type: LibraryType,
    folder_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/libraries/{space_id}/{library_type}/folders/{folder_id}/folders",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | NotFoundProblemDetails | list["Folder"] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Folder.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = cast("Any", None)
        return response_401

    if response.status_code == 403:
        response_403 = cast("Any", None)
        return response_403

    if response.status_code == 404:
        response_404 = NotFoundProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | NotFoundProblemDetails | list["Folder"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: int,
    library_type: LibraryType,
    folder_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | NotFoundProblemDetails | list["Folder"]]:
    """Lists all direct folders in the folder. The result does not include subfolders.

     The folders from the library can be retrieved by using the root folder identifier.

    Args:
        space_id (int):
        library_type (LibraryType): Type of the assets that can be stored in the library
        folder_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, list['Folder']]]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        library_type=library_type,
        folder_id=folder_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: int,
    library_type: LibraryType,
    folder_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | NotFoundProblemDetails | list["Folder"] | None:
    """Lists all direct folders in the folder. The result does not include subfolders.

     The folders from the library can be retrieved by using the root folder identifier.

    Args:
        space_id (int):
        library_type (LibraryType): Type of the assets that can be stored in the library
        folder_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, list['Folder']]
    """

    return sync_detailed(
        space_id=space_id,
        library_type=library_type,
        folder_id=folder_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    space_id: int,
    library_type: LibraryType,
    folder_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | NotFoundProblemDetails | list["Folder"]]:
    """Lists all direct folders in the folder. The result does not include subfolders.

     The folders from the library can be retrieved by using the root folder identifier.

    Args:
        space_id (int):
        library_type (LibraryType): Type of the assets that can be stored in the library
        folder_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, list['Folder']]]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        library_type=library_type,
        folder_id=folder_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: int,
    library_type: LibraryType,
    folder_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | NotFoundProblemDetails | list["Folder"] | None:
    """Lists all direct folders in the folder. The result does not include subfolders.

     The folders from the library can be retrieved by using the root folder identifier.

    Args:
        space_id (int):
        library_type (LibraryType): Type of the assets that can be stored in the library
        folder_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, list['Folder']]
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            library_type=library_type,
            folder_id=folder_id,
            client=client,
        )
    ).parsed
