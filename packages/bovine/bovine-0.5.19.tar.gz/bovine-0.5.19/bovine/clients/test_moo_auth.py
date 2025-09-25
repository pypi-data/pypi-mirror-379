# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

from unittest.mock import AsyncMock

import aiohttp

from bovine.testing import did_key, ed25519_key

from .moo_auth import MooAuthClient


async def test_moo_auth_client_get():
    session = AsyncMock(aiohttp.ClientSession)
    url = "https://test_domain/test_path"
    session = AsyncMock(aiohttp.ClientSession)
    session.get = AsyncMock()

    client = MooAuthClient(session, did_key, ed25519_key)

    await client.get(url)

    session.get.assert_awaited_once()

    args = session.get.await_args

    assert args[0] == (url,)
    assert "headers" in args[1]
    headers = args[1]["headers"]

    assert headers.keys() == {
        "accept",
        "date",
        "host",
        "authorization",
        "x-moo-signature",
        "user-agent",
    }
