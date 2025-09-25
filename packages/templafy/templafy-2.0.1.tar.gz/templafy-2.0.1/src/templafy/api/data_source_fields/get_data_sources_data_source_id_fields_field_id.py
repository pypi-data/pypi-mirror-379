# ruff: noqa: E722
from http import HTTPStatus
from typing import Any, Union, cast

import httpx

from templafy import errors
from templafy.client import AuthenticatedClient, Client
from templafy.models.color_theme_field_schema import ColorThemeFieldSchema
from templafy.models.font_field_schema import FontFieldSchema
from templafy.models.image_field_schema import ImageFieldSchema
from templafy.models.language_field_schema import LanguageFieldSchema
from templafy.models.not_found_problem_details import NotFoundProblemDetails
from templafy.models.number_field_schema import NumberFieldSchema
from templafy.models.reference_field_schema import ReferenceFieldSchema
from templafy.models.text_field_schema import TextFieldSchema
from templafy.types import Response


def _get_kwargs(
    data_source_id: int,
    field_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/data-sources/{data_source_id}/fields/{field_id}",
    }

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
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
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
                response_200_type_0 = TextFieldSchema.from_dict(data)

                return response_200_type_0
            except:
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_200_type_1 = NumberFieldSchema.from_dict(data)

                return response_200_type_1
            except:
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_200_type_2 = ReferenceFieldSchema.from_dict(data)

                return response_200_type_2
            except:
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_200_type_3 = ImageFieldSchema.from_dict(data)

                return response_200_type_3
            except:
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_200_type_4 = LanguageFieldSchema.from_dict(data)

                return response_200_type_4
            except:
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError
                response_200_type_5 = FontFieldSchema.from_dict(data)

                return response_200_type_5
            except:
                pass
            if not isinstance(data, dict):
                raise TypeError
            response_200_type_6 = ColorThemeFieldSchema.from_dict(data)

            return response_200_type_6

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
]:
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
]:
    """Gets an existing data source field.

     Returns a data source field that represents the schema of a single field of a data source.

    Args:
        data_source_id (int): The ID of the data source.
        field_id (int): The ID of the field.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, Union['ColorThemeFieldSchema', 'FontFieldSchema', 'ImageFieldSchema', 'LanguageFieldSchema', 'NumberFieldSchema', 'ReferenceFieldSchema', 'TextFieldSchema']]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        field_id=field_id,
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
    | None
):
    """Gets an existing data source field.

     Returns a data source field that represents the schema of a single field of a data source.

    Args:
        data_source_id (int): The ID of the data source.
        field_id (int): The ID of the field.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, Union['ColorThemeFieldSchema', 'FontFieldSchema', 'ImageFieldSchema', 'LanguageFieldSchema', 'NumberFieldSchema', 'ReferenceFieldSchema', 'TextFieldSchema']]
    """

    return sync_detailed(
        data_source_id=data_source_id,
        field_id=field_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    data_source_id: int,
    field_id: int,
    *,
    client: AuthenticatedClient,
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
]:
    """Gets an existing data source field.

     Returns a data source field that represents the schema of a single field of a data source.

    Args:
        data_source_id (int): The ID of the data source.
        field_id (int): The ID of the field.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NotFoundProblemDetails, Union['ColorThemeFieldSchema', 'FontFieldSchema', 'ImageFieldSchema', 'LanguageFieldSchema', 'NumberFieldSchema', 'ReferenceFieldSchema', 'TextFieldSchema']]]
    """

    kwargs = _get_kwargs(
        data_source_id=data_source_id,
        field_id=field_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    data_source_id: int,
    field_id: int,
    *,
    client: AuthenticatedClient,
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
    | None
):
    """Gets an existing data source field.

     Returns a data source field that represents the schema of a single field of a data source.

    Args:
        data_source_id (int): The ID of the data source.
        field_id (int): The ID of the field.
        client (AuthenticatedClient): The authenticated client instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NotFoundProblemDetails, Union['ColorThemeFieldSchema', 'FontFieldSchema', 'ImageFieldSchema', 'LanguageFieldSchema', 'NumberFieldSchema', 'ReferenceFieldSchema', 'TextFieldSchema']]
    """

    return (
        await asyncio_detailed(
            data_source_id=data_source_id,
            field_id=field_id,
            client=client,
        )
    ).parsed
