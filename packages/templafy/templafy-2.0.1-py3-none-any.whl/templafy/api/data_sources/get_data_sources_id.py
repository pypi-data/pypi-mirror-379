from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.data_source import DataSource
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.types import Response


def _get_kwargs(
    id_: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/data-sources/{id_}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DataSource | NotFoundProblemDetails | None:
    if response.status_code == 200:
        response_200 = DataSource.from_dict(response.json())

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
) -> Response[Any | DataSource | NotFoundProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | DataSource | NotFoundProblemDetails]:
    """Gets an existing data source.

     Returns a single data source and the schema of its fields.

    Args:
        id_ (int): The ID of the data source to retrieve.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSource, NotFoundProblemDetails]]
    """

    kwargs = _get_kwargs(
        id_=id_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id_: int,
    *,
    client: AuthenticatedClient,
) -> Any | DataSource | NotFoundProblemDetails | None:
    """Gets an existing data source.

     Returns a single data source and the schema of its fields.

    Args:
        id_ (int): The ID of the data source to retrieve.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataSource, NotFoundProblemDetails]
    """

    return sync_detailed(
        id_=id_,
        client=client,
    ).parsed


async def asyncio_detailed(
    id_: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | DataSource | NotFoundProblemDetails]:
    """Gets an existing data source.

     Returns a single data source and the schema of its fields.

    Args:
        id_ (int): The ID of the data source to retrieve.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSource, NotFoundProblemDetails]]
    """

    kwargs = _get_kwargs(
        id_=id_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id_: int,
    *,
    client: AuthenticatedClient,
) -> Any | DataSource | NotFoundProblemDetails | None:
    """Gets an existing data source.

     Returns a single data source and the schema of its fields.

    Args:
        id_ (int): The ID of the data source to retrieve.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataSource, NotFoundProblemDetails]
    """

    return (
        await asyncio_detailed(
            id_=id_,
            client=client,
        )
    ).parsed
