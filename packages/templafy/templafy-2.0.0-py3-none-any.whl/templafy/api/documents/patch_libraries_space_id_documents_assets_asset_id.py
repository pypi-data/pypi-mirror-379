from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.conflict_problem_details import ConflictProblemDetails
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.models.patch_libraries_space_id_documents_assets_asset_id_body import (
    PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody,
)
from templafy.models.validation_problem_details import ValidationProblemDetails
from templafy.types import Response


def _get_kwargs(
    space_id: int,
    asset_id: int,
    *,
    body: PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/libraries/{space_id}/documents/assets/{asset_id}",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ConflictProblemDetails
    | NotFoundProblemDetails
    | ValidationProblemDetails
    | None
):
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

    if response.status_code == 409:
        response_409 = ConflictProblemDetails.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | ConflictProblemDetails | NotFoundProblemDetails | ValidationProblemDetails
]:
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
    body: PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody,
) -> Response[
    Any | ConflictProblemDetails | NotFoundProblemDetails | ValidationProblemDetails
]:
    """Updates the document template.

     Only one file can be attached to the request body. The supported file format is .DOCX

    Args:
        space_id (int):
        asset_id (int):
        body (PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConflictProblemDetails, NotFoundProblemDetails, ValidationProblemDetails]]
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
    body: PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody,
) -> (
    Any
    | ConflictProblemDetails
    | NotFoundProblemDetails
    | ValidationProblemDetails
    | None
):
    """Updates the document template.

     Only one file can be attached to the request body. The supported file format is .DOCX

    Args:
        space_id (int):
        asset_id (int):
        body (PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConflictProblemDetails, NotFoundProblemDetails, ValidationProblemDetails]
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
    body: PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody,
) -> Response[
    Any | ConflictProblemDetails | NotFoundProblemDetails | ValidationProblemDetails
]:
    """Updates the document template.

     Only one file can be attached to the request body. The supported file format is .DOCX

    Args:
        space_id (int):
        asset_id (int):
        body (PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConflictProblemDetails, NotFoundProblemDetails, ValidationProblemDetails]]
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
    body: PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody,
) -> (
    Any
    | ConflictProblemDetails
    | NotFoundProblemDetails
    | ValidationProblemDetails
    | None
):
    """Updates the document template.

     Only one file can be attached to the request body. The supported file format is .DOCX

    Args:
        space_id (int):
        asset_id (int):
        body (PatchLibrariesSpaceIdDocumentsAssetsAssetIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConflictProblemDetails, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return (
        await asyncio_detailed(
            space_id=space_id,
            asset_id=asset_id,
            client=client,
            body=body,
        )
    ).parsed
