from http import HTTPStatus
from typing import Any, Union, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.models.slide_details_base import SlideDetailsBase
from templafy.types import Response


def _get_kwargs(
    space_id: int,
    asset_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/libraries/{space_id}/slides/assets/{asset_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Union["SlideDetailsBase", Any, NotFoundProblemDetails] | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> "SlideDetailsBase":
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_200_type_0 = SlideDetailsBase.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError
            response_200_type_1 = SlideDetailsBase.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[Union["SlideDetailsBase", Any, NotFoundProblemDetails]]:
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
) -> Response[Union["SlideDetailsBase", Any, NotFoundProblemDetails]]:
    """Returns the slide deck or slide by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['SlideDetailsBase', Any, NotFoundProblemDetails]]
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
) -> Union["SlideDetailsBase", Any, NotFoundProblemDetails] | None:
    """Returns the slide deck or slide by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['SlideDetailsBase', Any, NotFoundProblemDetails]
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
) -> Response[Union["SlideDetailsBase", Any, NotFoundProblemDetails]]:
    """Returns the slide deck or slide by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['SlideDetailsBase', Any, NotFoundProblemDetails]]
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
) -> Union["SlideDetailsBase", Any, NotFoundProblemDetails] | None:
    """Returns the slide deck or slide by the identifier.

    Args:
        space_id (int):
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['SlideDetailsBase', Any, NotFoundProblemDetails]
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            asset_id=asset_id,
            client=client,
        )
    ).parsed
