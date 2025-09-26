from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.circuit import Circuit
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    circuit_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/circuits/{circuit_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Circuit | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = Circuit.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Circuit | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    circuit_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Circuit | HTTPValidationError]:
    """Get Circuit State

    Args:
        circuit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Circuit, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        circuit_id=circuit_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    circuit_id: str,
    *,
    client: AuthenticatedClient,
) -> Circuit | HTTPValidationError | None:
    """Get Circuit State

    Args:
        circuit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Circuit, HTTPValidationError]
    """

    return sync_detailed(
        circuit_id=circuit_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    circuit_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Circuit | HTTPValidationError]:
    """Get Circuit State

    Args:
        circuit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Circuit, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        circuit_id=circuit_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    circuit_id: str,
    *,
    client: AuthenticatedClient,
) -> Circuit | HTTPValidationError | None:
    """Get Circuit State

    Args:
        circuit_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Circuit, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            circuit_id=circuit_id,
            client=client,
        )
    ).parsed
