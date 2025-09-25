from http import HTTPStatus
from typing import Any, Union, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.color_theme_field_schema import ColorThemeFieldSchema
from templafy.models.create_image_field_schema_request import (
    CreateImageFieldSchemaRequest,
)
from templafy.models.create_number_field_schema_request import (
    CreateNumberFieldSchemaRequest,
)
from templafy.models.create_reference_field_schema_request import (
    CreateReferenceFieldSchemaRequest,
)
from templafy.models.create_text_field_schema_request import (
    CreateTextFieldSchemaRequest,
)
from templafy.models.font_field_schema import FontFieldSchema
from templafy.models.image_field_schema import ImageFieldSchema
from templafy.models.language_field_schema import LanguageFieldSchema
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.models.number_field_schema import NumberFieldSchema
from templafy.models.reference_field_schema import ReferenceFieldSchema
from templafy.models.text_field_schema import TextFieldSchema
from templafy.models.validation_problem_details import ValidationProblemDetails
from templafy.types import Response


def _get_kwargs(
    data_source_id: int,
    *,
    body: Union[
        "CreateImageFieldSchemaRequest",
        "CreateNumberFieldSchemaRequest",
        "CreateReferenceFieldSchemaRequest",
        "CreateTextFieldSchemaRequest",
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/data-sources/{data_source_id}/fields",
    }

    if isinstance(
        body,
        Union[
            "CreateImageFieldSchemaRequest",
            "CreateNumberFieldSchemaRequest",
            "CreateReferenceFieldSchemaRequest",
            "CreateTextFieldSchemaRequest",
        ],
    ):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(
        body,
        Union[
            "CreateImageFieldSchemaRequest",
            "CreateNumberFieldSchemaRequest",
            "CreateReferenceFieldSchemaRequest",
            "CreateTextFieldSchemaRequest",
        ],
    ):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(
        body,
        Union[
            "CreateImageFieldSchemaRequest",
            "CreateNumberFieldSchemaRequest",
            "CreateReferenceFieldSchemaRequest",
            "CreateTextFieldSchemaRequest",
        ],
    ):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | NotFoundProblemDetails
    | Union[
        "ColorThemeFieldSchema",
        "FontFieldSchema",
        "ImageFieldSchema",
        "LanguageFieldSchema",
        "NumberFieldSchema",
        "ReferenceFieldSchema",
        "TextFieldSchema",
    ]
    | ValidationProblemDetails
    | None
):
    if response.status_code == 201:

        def _parse_response_201(
            data: object,
        ) -> Union[
            "ColorThemeFieldSchema",
            "FontFieldSchema",
            "ImageFieldSchema",
            "LanguageFieldSchema",
            "NumberFieldSchema",
            "ReferenceFieldSchema",
            "TextFieldSchema",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_201_type_0 = TextFieldSchema.from_dict(data)

                return response_201_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_201_type_1 = NumberFieldSchema.from_dict(data)

                return response_201_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_201_type_2 = ReferenceFieldSchema.from_dict(data)

                return response_201_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_201_type_3 = ImageFieldSchema.from_dict(data)

                return response_201_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_201_type_4 = LanguageFieldSchema.from_dict(data)

                return response_201_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_201_type_5 = FontFieldSchema.from_dict(data)

                return response_201_type_5
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError
            response_201_type_6 = ColorThemeFieldSchema.from_dict(data)

            return response_201_type_6

        response_201 = _parse_response_201(response.json())

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
) -> Response[
    Any
    | NotFoundProblemDetails
    | Union[
        "ColorThemeFieldSchema",
        "FontFieldSchema",
        "ImageFieldSchema",
        "LanguageFieldSchema",
        "NumberFieldSchema",
        "ReferenceFieldSchema",
        "TextFieldSchema",
    ]
    | ValidationProblemDetails
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
    body: Union[
        "CreateImageFieldSchemaRequest",
        "CreateNumberFieldSchemaRequest",
        "CreateReferenceFieldSchemaRequest",
        "CreateTextFieldSchemaRequest",
    ],
) -> Response[
    Any
    | NotFoundProblemDetails
    | Union[
        "ColorThemeFieldSchema",
        "FontFieldSchema",
        "ImageFieldSchema",
        "LanguageFieldSchema",
        "NumberFieldSchema",
        "ReferenceFieldSchema",
        "TextFieldSchema",
    ]
    | ValidationProblemDetails
]:
    """Creates a new data source field.

     Extends a data source by adding a new field.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        body (Union['CreateImageFieldSchemaRequest', 'CreateNumberFieldSchemaRequest',
            'CreateReferenceFieldSchemaRequest', 'CreateTextFieldSchemaRequest']):  Example: {'name':
            'History', 'type': 'text', 'isMultipleLines': True, 'defaultValue': 'The city was
            established in the year 1652 by Dutch explorers...', 'isRequired': False}.

    Note:
            body may be one of several concrete create request types depending on the field
            schema being created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, Union['ColorThemeFieldSchema', 'FontFieldSchema', 'ImageFieldSchema', 'LanguageFieldSchema', 'NumberFieldSchema', 'ReferenceFieldSchema', 'TextFieldSchema'], ValidationProblemDetails]]
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
    body: Union[
        "CreateImageFieldSchemaRequest",
        "CreateNumberFieldSchemaRequest",
        "CreateReferenceFieldSchemaRequest",
        "CreateTextFieldSchemaRequest",
    ],
) -> (
    Any
    | NotFoundProblemDetails
    | Union[
        "ColorThemeFieldSchema",
        "FontFieldSchema",
        "ImageFieldSchema",
        "LanguageFieldSchema",
        "NumberFieldSchema",
        "ReferenceFieldSchema",
        "TextFieldSchema",
    ]
    | ValidationProblemDetails
    | None
):
    """Creates a new data source field.

     Extends a data source by adding a new field.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        body (Union['CreateImageFieldSchemaRequest', 'CreateNumberFieldSchemaRequest',
            'CreateReferenceFieldSchemaRequest', 'CreateTextFieldSchemaRequest']):  Example: {'name':
            'History', 'type': 'text', 'isMultipleLines': True, 'defaultValue': 'The city was
            established in the year 1652 by Dutch explorers...', 'isRequired': False}.

    Note:
            body may be one of several concrete create request types depending on the field
            schema being created.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, Union['ColorThemeFieldSchema', 'FontFieldSchema', 'ImageFieldSchema', 'LanguageFieldSchema', 'NumberFieldSchema', 'ReferenceFieldSchema', 'TextFieldSchema'], ValidationProblemDetails]
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
    body: Union[
        "CreateImageFieldSchemaRequest",
        "CreateNumberFieldSchemaRequest",
        "CreateReferenceFieldSchemaRequest",
        "CreateTextFieldSchemaRequest",
    ],
) -> Response[
    Any
    | NotFoundProblemDetails
    | Union[
        "ColorThemeFieldSchema",
        "FontFieldSchema",
        "ImageFieldSchema",
        "LanguageFieldSchema",
        "NumberFieldSchema",
        "ReferenceFieldSchema",
        "TextFieldSchema",
    ]
    | ValidationProblemDetails
]:
    """Creates a new data source field.

     Extends a data source by adding a new field.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        body (Union['CreateImageFieldSchemaRequest', 'CreateNumberFieldSchemaRequest',
            'CreateReferenceFieldSchemaRequest', 'CreateTextFieldSchemaRequest']):  Example: {'name':
            'History', 'type': 'text', 'isMultipleLines': True, 'defaultValue': 'The city was
            established in the year 1652 by Dutch explorers...', 'isRequired': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, Union['ColorThemeFieldSchema', 'FontFieldSchema', 'ImageFieldSchema', 'LanguageFieldSchema', 'NumberFieldSchema', 'ReferenceFieldSchema', 'TextFieldSchema'], ValidationProblemDetails]]
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
    body: Union[
        "CreateImageFieldSchemaRequest",
        "CreateNumberFieldSchemaRequest",
        "CreateReferenceFieldSchemaRequest",
        "CreateTextFieldSchemaRequest",
    ],
) -> (
    Any
    | NotFoundProblemDetails
    | Union[
        "ColorThemeFieldSchema",
        "FontFieldSchema",
        "ImageFieldSchema",
        "LanguageFieldSchema",
        "NumberFieldSchema",
        "ReferenceFieldSchema",
        "TextFieldSchema",
    ]
    | ValidationProblemDetails
    | None
):
    """Creates a new data source field.

     Extends a data source by adding a new field.

    Args:
        data_source_id (int): The ID of the data source.
        client (AuthenticatedClient): The authenticated client instance.
        body (Union['CreateImageFieldSchemaRequest', 'CreateNumberFieldSchemaRequest',
            'CreateReferenceFieldSchemaRequest', 'CreateTextFieldSchemaRequest']):  Example: {'name':
            'History', 'type': 'text', 'isMultipleLines': True, 'defaultValue': 'The city was
            established in the year 1652 by Dutch explorers...', 'isRequired': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, Union['ColorThemeFieldSchema', 'FontFieldSchema', 'ImageFieldSchema', 'LanguageFieldSchema', 'NumberFieldSchema', 'ReferenceFieldSchema', 'TextFieldSchema'], ValidationProblemDetails]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            client=client,
            body=body,
        )
    ).parsed
