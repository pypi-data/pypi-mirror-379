from http import HTTPStatus
from typing import Any, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.create_data_source_request import CreateDataSourceRequest
from templafy.models.data_source import DataSource
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.models.validation_problem_details import ValidationProblemDetails
from templafy.types import Response


def _get_kwargs(
    *,
    body: CreateDataSourceRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/data-sources",
    }

    if isinstance(body, CreateDataSourceRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, CreateDataSourceRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateDataSourceRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DataSource | NotFoundProblemDetails | ValidationProblemDetails | None:
    if response.status_code == 201:
        response_201 = DataSource.from_dict(response.json())

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
) -> Response[Any | DataSource | NotFoundProblemDetails | ValidationProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDataSourceRequest,
) -> Response[Any | DataSource | NotFoundProblemDetails | ValidationProblemDetails]:
    """Creates a new data source.

     Creates a new data source to contain data source items to represent your data.

    Args:
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSource, NotFoundProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateDataSourceRequest,
) -> Any | DataSource | NotFoundProblemDetails | ValidationProblemDetails | None:
    """Creates a new data source.

     Creates a new data source to contain data source items to represent your data.

    Args:
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataSource, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateDataSourceRequest,
) -> Response[Any | DataSource | NotFoundProblemDetails | ValidationProblemDetails]:
    """Creates a new data source.

     Creates a new data source to contain data source items to represent your data.

    Args:
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DataSource, NotFoundProblemDetails, ValidationProblemDetails]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateDataSourceRequest,
) -> Any | DataSource | NotFoundProblemDetails | ValidationProblemDetails | None:
    """Creates a new data source.

     Creates a new data source to contain data source items to represent your data.

    Args:
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.
        body (CreateDataSourceRequest):  Example: {'name': 'Cities', 'description': 'Cities in
            which we have offices', 'fields': [{'name': 'History', 'type': 'text', 'isMultipleLines':
            True, 'defaultValue': 'The city was established in the year 1652 by Dutch explorers...',
            'isRequired': False}, {'name': 'Population', 'type': 'number', 'defaultValue': 100222,
            'isRequired': True}, {'name': 'Country', 'type': 'reference', 'referenceDataSourceId':
            '637989101951089955', 'defaultReferencedItemId': '638249311425155568', 'isRequired':
            True}, {'name': 'Flag', 'type': 'image', 'isRequired': True}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DataSource, NotFoundProblemDetails, ValidationProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
