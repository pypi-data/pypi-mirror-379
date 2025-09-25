from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.models.spreadsheet import Spreadsheet
from templafy.models.validation_problem_details import ValidationProblemDetails
from templafy.types import UNSET, Response, Unset


def _get_kwargs(
    space_id: int,
    folder_id: int,
    *,
    search_query: Unset | str = UNSET,
    page_number: Unset | int = UNSET,
    page_size: Unset | int = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["searchQuery"] = search_query

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/libraries/{space_id}/spreadsheets/folders/{folder_id}/assets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | NotFoundProblemDetails | ValidationProblemDetails | list["Spreadsheet"] | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Spreadsheet.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ValidationProblemDetails.from_dict(response.json())

        return response_400

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
) -> Response[
    Any | NotFoundProblemDetails | ValidationProblemDetails | list["Spreadsheet"]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    search_query: Unset | str = UNSET,
    page_number: Unset | int = UNSET,
    page_size: Unset | int = UNSET,
) -> Response[
    Any | NotFoundProblemDetails | ValidationProblemDetails | list["Spreadsheet"]
]:
    """Lists all spreadsheet templates in the folder.

     The result does not include spreadsheet templates from subfolders. When {searchQuery} is used the
    result includes spreadsheet templates from subfolders. The search mode enables pagination with 1000
    page size maximum.

    Args:
        space_id (int):
        folder_id (int):
        search_query (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails, list['Spreadsheet']]]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        folder_id=folder_id,
        search_query=search_query,
        page_number=page_number,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    search_query: Unset | str = UNSET,
    page_number: Unset | int = UNSET,
    page_size: Unset | int = UNSET,
) -> (
    Any | NotFoundProblemDetails | ValidationProblemDetails | list["Spreadsheet"] | None
):
    """Lists all spreadsheet templates in the folder.

     The result does not include spreadsheet templates from subfolders. When {searchQuery} is used the
    result includes spreadsheet templates from subfolders. The search mode enables pagination with 1000
    page size maximum.

    Args:
        space_id (int):
        folder_id (int):
        search_query (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, ValidationProblemDetails, list['Spreadsheet']]
    """

    return sync_detailed(
        space_id=space_id,
        folder_id=folder_id,
        client=client,
        search_query=search_query,
        page_number=page_number,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    space_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    search_query: Unset | str = UNSET,
    page_number: Unset | int = UNSET,
    page_size: Unset | int = UNSET,
) -> Response[
    Any | NotFoundProblemDetails | ValidationProblemDetails | list["Spreadsheet"]
]:
    """Lists all spreadsheet templates in the folder.

     The result does not include spreadsheet templates from subfolders. When {searchQuery} is used the
    result includes spreadsheet templates from subfolders. The search mode enables pagination with 1000
    page size maximum.

    Args:
        space_id (int):
        folder_id (int):
        search_query (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails, list['Spreadsheet']]]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        folder_id=folder_id,
        search_query=search_query,
        page_number=page_number,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: int,
    folder_id: int,
    *,
    client: AuthenticatedClient,
    search_query: Unset | str = UNSET,
    page_number: Unset | int = UNSET,
    page_size: Unset | int = UNSET,
) -> (
    Any | NotFoundProblemDetails | ValidationProblemDetails | list["Spreadsheet"] | None
):
    """Lists all spreadsheet templates in the folder.

     The result does not include spreadsheet templates from subfolders. When {searchQuery} is used the
    result includes spreadsheet templates from subfolders. The search mode enables pagination with 1000
    page size maximum.

    Args:
        space_id (int):
        folder_id (int):
        search_query (Union[Unset, str]):
        page_number (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, ValidationProblemDetails, list['Spreadsheet']]
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            folder_id=folder_id,
            client=client,
            search_query=search_query,
            page_number=page_number,
            page_size=page_size,
        )
    ).parsed
