from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.generate_file_request import GenerateFileRequest
from templafy.models.generated_file import GeneratedFile
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.models.validation_problem_details import ValidationProblemDetails
from templafy.types import Response


def _get_kwargs(
    space_id: int,
    asset_id: int,
    *,
    body: GenerateFileRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/libraries/{space_id}/presentations/assets/{asset_id}/generate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GeneratedFile | NotFoundProblemDetails | ValidationProblemDetails | None:
    if response.status_code == 200:
        response_200 = GeneratedFile.from_dict(response.json())

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
) -> Response[Any | GeneratedFile | NotFoundProblemDetails | ValidationProblemDetails]:
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
    body: GenerateFileRequest,
) -> Response[Any | GeneratedFile | NotFoundProblemDetails | ValidationProblemDetails]:
    """Generates a presentation from a template and returns information about the file, which includes the
    download url.

     Creates a file from the template in a pptx format. The file will have bindings replaced using
    various data sources. The url will only be valid for a short amount of time.

    Args:
        space_id (int):
        asset_id (int):
        body (GenerateFileRequest): The request model to generate a file. Example: {'email':
            'templafy@templafy.com', 'data': {'Language': 'en-us'}, 'includePdf': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GeneratedFile, NotFoundProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        asset_id=asset_id,
        body=body,
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
    body: GenerateFileRequest,
) -> Any | GeneratedFile | NotFoundProblemDetails | ValidationProblemDetails | None:
    """Generates a presentation from a template and returns information about the file, which includes the
    download url.

     Creates a file from the template in a pptx format. The file will have bindings replaced using
    various data sources. The url will only be valid for a short amount of time.

    Args:
        space_id (int):
        asset_id (int):
        body (GenerateFileRequest): The request model to generate a file. Example: {'email':
            'templafy@templafy.com', 'data': {'Language': 'en-us'}, 'includePdf': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GeneratedFile, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return sync_detailed(
        space_id=space_id,
        asset_id=asset_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    space_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
    body: GenerateFileRequest,
) -> Response[Any | GeneratedFile | NotFoundProblemDetails | ValidationProblemDetails]:
    """Generates a presentation from a template and returns information about the file, which includes the
    download url.

     Creates a file from the template in a pptx format. The file will have bindings replaced using
    various data sources. The url will only be valid for a short amount of time.

    Args:
        space_id (int):
        asset_id (int):
        body (GenerateFileRequest): The request model to generate a file. Example: {'email':
            'templafy@templafy.com', 'data': {'Language': 'en-us'}, 'includePdf': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GeneratedFile, NotFoundProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        space_id=space_id,
        asset_id=asset_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    space_id: int,
    asset_id: int,
    *,
    client: AuthenticatedClient,
    body: GenerateFileRequest,
) -> Any | GeneratedFile | NotFoundProblemDetails | ValidationProblemDetails | None:
    """Generates a presentation from a template and returns information about the file, which includes the
    download url.

     Creates a file from the template in a pptx format. The file will have bindings replaced using
    various data sources. The url will only be valid for a short amount of time.

    Args:
        space_id (int):
        asset_id (int):
        body (GenerateFileRequest): The request model to generate a file. Example: {'email':
            'templafy@templafy.com', 'data': {'Language': 'en-us'}, 'includePdf': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GeneratedFile, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            asset_id=asset_id,
            client=client,
            body=body,
        )
    ).parsed
