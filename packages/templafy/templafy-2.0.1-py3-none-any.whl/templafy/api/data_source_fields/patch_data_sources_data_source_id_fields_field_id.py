from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.models.patch_data_source_field_request import PatchDataSourceFieldRequest
from templafy.models.validation_problem_details import ValidationProblemDetails
from templafy.types import Response


def _get_kwargs(
    data_source_id: int,
    field_id: int,
    *,
    body: PatchDataSourceFieldRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/data-sources/{data_source_id}/fields/{field_id}",
    }

    if isinstance(body, PatchDataSourceFieldRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, PatchDataSourceFieldRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchDataSourceFieldRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | NotFoundProblemDetails | ValidationProblemDetails | None:
    if response.status_code == 204:
        response_204 = cast("Any", None)
        return response_204

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
) -> Response[Any | NotFoundProblemDetails | ValidationProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    data_source_id: int,
    field_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchDataSourceFieldRequest,
) -> Response[Any | NotFoundProblemDetails | ValidationProblemDetails]:
    """Updates an existing data source field.

     This is a PATCH operation. Any fields not included in the request will remain unchanged on the
    server.

    Args:
        data_source_id (int): The ID of the data source.
        field_id (int): The ID of the field.
        client (AuthenticatedClient): The authenticated client instance.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        field_id=field_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: int,
    field_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchDataSourceFieldRequest,
) -> Any | NotFoundProblemDetails | ValidationProblemDetails | None:
    """Updates an existing data source field.

     This is a PATCH operation. Any fields not included in the request will remain unchanged on the
    server.

    Args:
        data_source_id (int): The ID of the data source.
        field_id (int): The ID of the field.
        client (AuthenticatedClient): The authenticated client instance.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        field_id=field_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    data_source_id: int,
    field_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchDataSourceFieldRequest,
) -> Response[Any | NotFoundProblemDetails | ValidationProblemDetails]:
    """Updates an existing data source field.

     This is a PATCH operation. Any fields not included in the request will remain unchanged on the
    server.

    Args:
        data_source_id (int): The ID of the data source.
        field_id (int): The ID of the field.
        client (AuthenticatedClient): The authenticated client instance.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        field_id=field_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: int,
    field_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchDataSourceFieldRequest,
) -> Any | NotFoundProblemDetails | ValidationProblemDetails | None:
    """Updates an existing data source field.

     This is a PATCH operation. Any fields not included in the request will remain unchanged on the
    server.

    Args:
        data_source_id (int): The ID of the data source.
        field_id (int): The ID of the field.
        client (AuthenticatedClient): The authenticated client instance.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.
        body (PatchDataSourceFieldRequest):  Example: {'name': 'Population', 'isRequired': True,
            'defaultValue': 130000}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            field_id=field_id,
            client=client,
            body=body,
        )
    ).parsed
