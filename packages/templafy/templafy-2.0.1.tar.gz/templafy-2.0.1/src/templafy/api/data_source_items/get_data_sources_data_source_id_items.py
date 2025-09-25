from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.data_source_item import DataSourceItem
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.models.validation_problem_details import ValidationProblemDetails
from templafy.types import UNSET, Response, Unset


def _get_kwargs(
    data_source_id: int,
    *,
    page_number: Unset | int = 1,
    page_size: Unset | int = 100,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/data-sources/{data_source_id}/items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | NotFoundProblemDetails
    | ValidationProblemDetails
    | list["DataSourceItem"]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DataSourceItem.from_dict(response_200_item_data)

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
    Any | NotFoundProblemDetails | ValidationProblemDetails | list["DataSourceItem"]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_source_id: int,
    *,
    client: AuthenticatedClient,
    page_number: Unset | int = 1,
    page_size: Unset | int = 100,
) -> Response[
    Any | NotFoundProblemDetails | ValidationProblemDetails | list["DataSourceItem"]
]:
    """Lists all existing data source items.

     Returns a list of all data source items contained within a data source. Results are paged, starting
    at page 1.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        page_number (Union[Unset, int]): The page number to retrieve. Default: 1.
        page_size (Union[Unset, int]): The number of items per page. Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails, list['DataSourceItem']]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        page_number=page_number,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: int,
    *,
    client: AuthenticatedClient,
    page_number: Unset | int = 1,
    page_size: Unset | int = 100,
) -> (
    Any
    | NotFoundProblemDetails
    | ValidationProblemDetails
    | list["DataSourceItem"]
    | None
):
    """Lists all existing data source items.

     Returns a list of all data source items contained within a data source. Results are paged, starting
    at page 1.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        page_number (Union[Unset, int]): The page number to retrieve. Default: 1.
        page_size (Union[Unset, int]): The number of items per page. Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, ValidationProblemDetails, list['DataSourceItem']]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        client=client,
        page_number=page_number,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    data_source_id: int,
    *,
    client: AuthenticatedClient,
    page_number: Unset | int = 1,
    page_size: Unset | int = 100,
) -> Response[
    Any | NotFoundProblemDetails | ValidationProblemDetails | list["DataSourceItem"]
]:
    """Lists all existing data source items.

     Returns a list of all data source items contained within a data source. Results are paged, starting
    at page 1.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        page_number (Union[Unset, int]): The page number to retrieve. Default: 1.
        page_size (Union[Unset, int]): The number of items per page. Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails, list['DataSourceItem']]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        page_number=page_number,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: int,
    *,
    client: AuthenticatedClient,
    page_number: Unset | int = 1,
    page_size: Unset | int = 100,
) -> (
    Any
    | NotFoundProblemDetails
    | ValidationProblemDetails
    | list["DataSourceItem"]
    | None
):
    """Lists all existing data source items.

     Returns a list of all data source items contained within a data source. Results are paged, starting
    at page 1.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        page_number (Union[Unset, int]): The page number to retrieve. Default: 1.
        page_size (Union[Unset, int]): The number of items per page. Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, ValidationProblemDetails, list['DataSourceItem']]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
            page_number=page_number,
            page_size=page_size,
        )
    ).parsed
