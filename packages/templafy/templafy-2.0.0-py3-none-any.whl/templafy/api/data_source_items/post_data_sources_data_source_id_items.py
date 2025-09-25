from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.create_data_source_item_request import CreateDataSourceItemRequest
from templafy.models.data_source_item import DataSourceItem
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.models.validation_problem_details import ValidationProblemDetails
from templafy.types import Response


def _get_kwargs(
    data_source_id: int,
    *,
    body: CreateDataSourceItemRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/data-sources/{data_source_id}/items",
    }

    if isinstance(body, CreateDataSourceItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, CreateDataSourceItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateDataSourceItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DataSourceItem | NotFoundProblemDetails | ValidationProblemDetails | None:
    if response.status_code == 201:
        response_201 = DataSourceItem.from_dict(response.json())

        return response_201

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
) -> Response[Any | DataSourceItem | NotFoundProblemDetails | ValidationProblemDetails]:
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
    body: CreateDataSourceItemRequest,
) -> Response[Any | DataSourceItem | NotFoundProblemDetails | ValidationProblemDetails]:
    """Creates a new data source item.

     Creates a new data source item in the specified data source.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        body (CreateDataSourceItemRequest): The request body. Example: {'fields': [{'dataSourceFieldId': 0, 'type': 'text', 'value': 'Sample text'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSourceItem, NotFoundProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    data_source_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateDataSourceItemRequest,
) -> Any | DataSourceItem | NotFoundProblemDetails | ValidationProblemDetails | None:
    """Creates a new data source item.

     Creates a new data source item in the specified data source.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        body (CreateDataSourceItemRequest): The request body. Example: {'fields': [{'dataSourceFieldId': 0, 'type': 'text', 'value': 'Sample text'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataSourceItem, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    data_source_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateDataSourceItemRequest,
) -> Response[Any | DataSourceItem | NotFoundProblemDetails | ValidationProblemDetails]:
    """Creates a new data source item.

     Creates a new data source item in the specified data source.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        body (CreateDataSourceItemRequest):  Example: {'fields': [{'dataSourceFieldId': 0, 'type':
            'text', 'value': 'Sample text'}, {'dataSourceFieldId': 1, 'type': 'number', 'value':
            123.45}, {'dataSourceFieldId': 2, 'type': 'reference', 'dataSourceItemId':
            '638247997437572264'}, {'dataSourceFieldId': 3, 'type': 'image', 'fileName': 'Cat',
            'fileUrl': 'https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg'},
            {'dataSourceFieldId': 4, 'type': 'font', 'fileName': 'best-font', 'fileUrl':
            'https://allfonts.com/best-font'}, {'dataSourceFieldId': 5, 'type': 'colorTheme',
            'xmlValue': '<a:clrScheme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
            name="Templafy_New"><a:dk1><a:srgbClr val="0078FF"/></a:dk1><a:lt1><a:sysClr val="window"
            lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="000000"/></a:dk2><a:lt2><a:srgbClr
            val="E5E5E5"/></a:lt2><a:accent1><a:srgbClr
            val="0078FF"/></a:accent1><a:accent2><a:srgbClr
            val="575757"/></a:accent2><a:accent3><a:srgbClr
            val="12AA96"/></a:accent3><a:accent4><a:srgbClr
            val="15436B"/></a:accent4><a:accent5><a:srgbClr
            val="D44849"/></a:accent5><a:accent6><a:srgbClr
            val="7F7F7F"/></a:accent6><a:hlink><a:srgbClr
            val="0078FF"/></a:hlink><a:folHlink><a:srgbClr
            val="55CBFF"/></a:folHlink></a:clrScheme>'}]}.
        client (AuthenticatedClient): The authenticated client instance.
        body (CreateDataSourceItemRequest):  Example: {'fields': [{'dataSourceFieldId': 0, 'type':
            'text', 'value': 'Sample text'}, {'dataSourceFieldId': 1, 'type': 'number', 'value':
            123.45}, {'dataSourceFieldId': 2, 'type': 'reference', 'dataSourceItemId':
            '638247997437572264'}, {'dataSourceFieldId': 3, 'type': 'image', 'fileName': 'Cat',
            'fileUrl': 'https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg'},
            {'dataSourceFieldId': 4, 'type': 'font', 'fileName': 'best-font', 'fileUrl':
            'https://allfonts.com/best-font'}, {'dataSourceFieldId': 5, 'type': 'colorTheme',
            'xmlValue': '<a:clrScheme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
            name="Templafy_New"><a:dk1><a:srgbClr val="0078FF"/></a:dk1><a:lt1><a:sysClr val="window"
            lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="000000"/></a:dk2><a:lt2><a:srgbClr
            val="E5E5E5"/></a:lt2><a:accent1><a:srgbClr
            val="0078FF"/></a:accent1><a:accent2><a:srgbClr
            val="575757"/></a:accent2><a:accent3><a:srgbClr
            val="12AA96"/></a:accent3><a:accent4><a:srgbClr
            val="15436B"/></a:accent4><a:accent5><a:srgbClr
            val="D44849"/></a:accent5><a:accent6><a:srgbClr
            val="7F7F7F"/></a:accent6><a:hlink><a:srgbClr
            val="0078FF"/></a:hlink><a:folHlink><a:srgbClr
            val="55CBFF"/></a:folHlink></a:clrScheme>'}]}.
        body (CreateDataSourceItemRequest):  Example: {'fields': [{'dataSourceFieldId': 0, 'type':
            'text', 'value': 'Sample text'}, {'dataSourceFieldId': 1, 'type': 'number', 'value':
            123.45}, {'dataSourceFieldId': 2, 'type': 'reference', 'dataSourceItemId':
            '638247997437572264'}, {'dataSourceFieldId': 3, 'type': 'image', 'fileName': 'Cat',
            'fileUrl': 'https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg'},
            {'dataSourceFieldId': 4, 'type': 'font', 'fileName': 'best-font', 'fileUrl':
            'https://allfonts.com/best-font'}, {'dataSourceFieldId': 5, 'type': 'colorTheme',
            'xmlValue': '<a:clrScheme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
            name="Templafy_New"><a:dk1><a:srgbClr val="0078FF"/></a:dk1><a:lt1><a:sysClr val="window"
            lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="000000"/></a:dk2><a:lt2><a:srgbClr
            val="E5E5E5"/></a:lt2><a:accent1><a:srgbClr
            val="0078FF"/></a:accent1><a:accent2><a:srgbClr
            val="575757"/></a:accent2><a:accent3><a:srgbClr
            val="12AA96"/></a:accent3><a:accent4><a:srgbClr
            val="15436B"/></a:accent4><a:accent5><a:srgbClr
            val="D44849"/></a:accent5><a:accent6><a:srgbClr
            val="7F7F7F"/></a:accent6><a:hlink><a:srgbClr
            val="0078FF"/></a:hlink><a:folHlink><a:srgbClr
            val="55CBFF"/></a:folHlink></a:clrScheme>'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSourceItem, NotFoundProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateDataSourceItemRequest,
) -> Any | DataSourceItem | NotFoundProblemDetails | ValidationProblemDetails | None:
    """Creates a new data source item.

     Creates a new data source item in the specified data source.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        body (CreateDataSourceItemRequest):  Example: {'fields': [{'dataSourceFieldId': 0, 'type':
            'text', 'value': 'Sample text'}, {'dataSourceFieldId': 1, 'type': 'number', 'value':
            123.45}, {'dataSourceFieldId': 2, 'type': 'reference', 'dataSourceItemId':
            '638247997437572264'}, {'dataSourceFieldId': 3, 'type': 'image', 'fileName': 'Cat',
            'fileUrl': 'https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg'},
            {'dataSourceFieldId': 4, 'type': 'font', 'fileName': 'best-font', 'fileUrl':
            'https://allfonts.com/best-font'}, {'dataSourceFieldId': 5, 'type': 'colorTheme',
            'xmlValue': '<a:clrScheme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
            name="Templafy_New"><a:dk1><a:srgbClr val="0078FF"/></a:dk1><a:lt1><a:sysClr val="window"
            lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="000000"/></a:dk2><a:lt2><a:srgbClr
            val="E5E5E5"/></a:lt2><a:accent1><a:srgbClr
            val="0078FF"/></a:accent1><a:accent2><a:srgbClr
            val="575757"/></a:accent2><a:accent3><a:srgbClr
            val="12AA96"/></a:accent3><a:accent4><a:srgbClr
            val="15436B"/></a:accent4><a:accent5><a:srgbClr
            val="D44849"/></a:accent5><a:accent6><a:srgbClr
            val="7F7F7F"/></a:accent6><a:hlink><a:srgbClr
            val="0078FF"/></a:hlink><a:folHlink><a:srgbClr
            val="55CBFF"/></a:folHlink></a:clrScheme>'}]}.
        body (CreateDataSourceItemRequest):  Example: {'fields': [{'dataSourceFieldId': 0, 'type':
            'text', 'value': 'Sample text'}, {'dataSourceFieldId': 1, 'type': 'number', 'value':
            123.45}, {'dataSourceFieldId': 2, 'type': 'reference', 'dataSourceItemId':
            '638247997437572264'}, {'dataSourceFieldId': 3, 'type': 'image', 'fileName': 'Cat',
            'fileUrl': 'https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg'},
            {'dataSourceFieldId': 4, 'type': 'font', 'fileName': 'best-font', 'fileUrl':
            'https://allfonts.com/best-font'}, {'dataSourceFieldId': 5, 'type': 'colorTheme',
            'xmlValue': '<a:clrScheme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
            name="Templafy_New"><a:dk1><a:srgbClr val="0078FF"/></a:dk1><a:lt1><a:sysClr val="window"
            lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="000000"/></a:dk2><a:lt2><a:srgbClr
            val="E5E5E5"/></a:lt2><a:accent1><a:srgbClr
            val="0078FF"/></a:accent1><a:accent2><a:srgbClr
            val="575757"/></a:accent2><a:accent3><a:srgbClr
            val="12AA96"/></a:accent3><a:accent4><a:srgbClr
            val="15436B"/></a:accent4><a:accent5><a:srgbClr
            val="D44849"/></a:accent5><a:accent6><a:srgbClr
            val="7F7F7F"/></a:accent6><a:hlink><a:srgbClr
            val="0078FF"/></a:hlink><a:folHlink><a:srgbClr
            val="55CBFF"/></a:folHlink></a:clrScheme>'}]}.
        body (CreateDataSourceItemRequest):  Example: {'fields': [{'dataSourceFieldId': 0, 'type':
            'text', 'value': 'Sample text'}, {'dataSourceFieldId': 1, 'type': 'number', 'value':
            123.45}, {'dataSourceFieldId': 2, 'type': 'reference', 'dataSourceItemId':
            '638247997437572264'}, {'dataSourceFieldId': 3, 'type': 'image', 'fileName': 'Cat',
            'fileUrl': 'https://en.wikipedia.org/wiki/Cat#/media/File:Cat_August_2010-4.jpg'},
            {'dataSourceFieldId': 4, 'type': 'font', 'fileName': 'best-font', 'fileUrl':
            'https://allfonts.com/best-font'}, {'dataSourceFieldId': 5, 'type': 'colorTheme',
            'xmlValue': '<a:clrScheme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
            name="Templafy_New"><a:dk1><a:srgbClr val="0078FF"/></a:dk1><a:lt1><a:sysClr val="window"
            lastClr="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="000000"/></a:dk2><a:lt2><a:srgbClr
            val="E5E5E5"/></a:lt2><a:accent1><a:srgbClr
            val="0078FF"/></a:accent1><a:accent2><a:srgbClr
            val="575757"/></a:accent2><a:accent3><a:srgbClr
            val="12AA96"/></a:accent3><a:accent4><a:srgbClr
            val="15436B"/></a:accent4><a:accent5><a:srgbClr
            val="D44849"/></a:accent5><a:accent6><a:srgbClr
            val="7F7F7F"/></a:accent6><a:hlink><a:srgbClr
            val="0078FF"/></a:hlink><a:folHlink><a:srgbClr
            val="55CBFF"/></a:folHlink></a:clrScheme>'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataSourceItem, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
            body=body,
        )
    ).parsed
