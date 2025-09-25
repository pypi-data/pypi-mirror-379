from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.document_details import DocumentDetails
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.types import Response


def _get_kwargs(
    space_id: int,
    asset_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/libraries/{space_id}/documents/assets/{asset_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | NotFoundProblemDetails | list["DocumentDetails"] | None:
    if response.status_code == 200:
        _response_200 = response.json()
        if isinstance(_response_200, dict):
            # Single object, wrap in list
            response_200 = [DocumentDetails.from_dict(_response_200)]
        elif isinstance(_response_200, list):
            # List of objects
            response_200 = [DocumentDetails.from_dict(item) for item in _response_200]
        else:
            response_200 = None
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
) -> Response[Any | NotFoundProblemDetails | list["DocumentDetails"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    space_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | NotFoundProblemDetails | list["DocumentDetails"]]:
    """Returns the document template by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, list['DocumentDetails']]]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        asset_id=asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    space_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | NotFoundProblemDetails | list["DocumentDetails"] | None:
    """Returns the document template by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, list['DocumentDetails']]
    """

    return sync_detailed(
        space_id=space_id,
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    space_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | NotFoundProblemDetails | list["DocumentDetails"]]:
    """Returns the document template by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, list['DocumentDetails']]]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        asset_id=asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | NotFoundProblemDetails | list["DocumentDetails"] | None:
    """Returns the document template by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, list['DocumentDetails']]
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            asset_id=asset_id,
            client=client,
        )
    ).parsed
