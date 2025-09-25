from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.data_source_item import DataSourceItem
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.types import Response


def _get_kwargs(
    data_source_id: int,
    item_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/data-sources/{data_source_id}/items/{item_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DataSourceItem | NotFoundProblemDetails | None:
    if response.status_code == 200:
        response_200 = DataSourceItem.from_dict(response.json())

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
) -> Response[Any | DataSourceItem | NotFoundProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_source_id: int,
    item_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | DataSourceItem | NotFoundProblemDetails]:
    """Gets an existing data source item.

     Returns a single data source item from the specified data source.

    Args:
        data_source_id (int): The ID of the data source.
        item_id (int): The ID of the item.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSourceItem, NotFoundProblemDetails]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: int,
    item_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | DataSourceItem | NotFoundProblemDetails | None:
    """Gets an existing data source item.

     Returns a single data source item from the specified data source.

    Args:
        data_source_id (int): The ID of the data source.
        item_id (int): The ID of the item.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataSourceItem, NotFoundProblemDetails]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_source_id: int,
    item_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | DataSourceItem | NotFoundProblemDetails]:
    """Gets an existing data source item.

     Returns a single data source item from the specified data source.

    Args:
        data_source_id (int): The ID of the data source.
        item_id (int): The ID of the item.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSourceItem, NotFoundProblemDetails]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: int,
    item_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | DataSourceItem | NotFoundProblemDetails | None:
    """Gets an existing data source item.

     Returns a single data source item from the specified data source.

    Args:
        data_source_id (int): The ID of the data source.
        item_id (int): The ID of the item.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataSourceItem, NotFoundProblemDetails]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
