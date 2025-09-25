# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

from unittest.mock import AsyncMock, MagicMock

import aiohttp

from bovine.crypto.signature_checker import SignatureChecker
from bovine.testing import private_key, public_key
from bovine.crypto.types import CryptographicSecret, CryptographicIdentifier

from .signed_http_methods import signed_get


async def test_signed_get():
    url = "https://test_domain/test_path"
    public_key_url = "public_key_url"
    session = AsyncMock(aiohttp.ClientSession)
    session.get = AsyncMock()
    session.get.return_value = "value"

    key_retriever = AsyncMock()
    key_retriever.return_value = CryptographicIdentifier.from_pem(public_key, "owner")
    signature_checker = SignatureChecker(key_retriever)

    secret = CryptographicSecret.from_pem(public_key_url, private_key)

    response = await signed_get(session, secret, url)

    session.get.assert_awaited_once()

    assert response == "value"

    args = session.get.await_args

    assert args[0] == (url,)
    assert "headers" in args[1]
    headers = args[1]["headers"]

    assert headers.keys() == {"accept", "date", "host", "signature", "user-agent"}

    assert headers["accept"] == "application/activity+json"
    assert headers["host"] == "test_domain"

    request = MagicMock()
    request.headers = headers
    request.method = "get"
    request.url = url

    assert (await signature_checker.validate_signature_request(request)) == "owner"

    key_retriever.assert_awaited_once()
    assert key_retriever.await_args[0] == (public_key_url,)
