"""Async request utilities."""

from __future__ import annotations

from typing import Any

import httpx

# Import from core
from pararamio_aio._core import PararamioHTTPRequestError, build_url

# Define BOT_KEY_PARAM locally if not in core
BOT_KEY_PARAM = 'key'

__all__ = ('async_api_request', 'async_bot_request')


async def async_api_request(
    client: httpx.AsyncClient,
    url: str,
    method: str = 'GET',
    data: dict | None = None,
    headers: dict | None = None,
) -> dict:
    """Make async API request.

    Args:
        client: httpx client
        url: API endpoint URL
        method: HTTP method
        data: Request data
        headers: Request headers

    Returns:
        JSON response as dict
    """
    full_url = build_url(url)

    response = await client.request(method, full_url, json=data, headers=headers or {})
    if response.status_code != 200:
        raise PararamioHTTPRequestError(
            full_url,
            response.status_code,
            f'HTTP {response.status_code}',
            dict(response.headers),
            response.text,
        )
    return response.json()


async def async_bot_request(
    url: str,
    key: str,
    method: str = 'GET',
    data: dict | None = None,
    headers: dict | None = None,
) -> dict[str, Any]:
    """Make an authenticated bot API request.

    Args:
        url: API endpoint
        key: Bot API key
        method: HTTP method
        data: Request data
        headers: Additional headers

    Returns:
        Response data as dictionary
    """
    # Add bot key to URL
    separator = '&' if '?' in url else '?'
    full_url = f'{url}{separator}{BOT_KEY_PARAM}={key}'

    async with httpx.AsyncClient() as client:
        return await async_api_request(client, full_url, method, data, headers)
