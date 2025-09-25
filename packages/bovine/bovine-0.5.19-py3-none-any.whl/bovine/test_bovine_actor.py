# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

import pytest
import json
from unittest.mock import AsyncMock, MagicMock

import aiohttp

from bovine import BovineActor
from .clients.moo_auth import MooAuthClient
from .clients.signed_http import SignedHttpClient
from bovine.activitystreams import OrderedCollection, OrderedCollectionPage
from bovine.testing import private_key


async def test_activity_pub_client_get_collection_no_pages():
    session = AsyncMock(aiohttp.ClientSession)
    url = "https://test_domain/test_path"
    public_key_url = "public_key_url"
    session = AsyncMock(aiohttp.ClientSession)
    session.get = AsyncMock()

    actor = BovineActor(
        actor_id="actor_id",
        public_key_url=public_key_url,
        secret=private_key,
    )
    await actor.init_session(session)

    text_mock = AsyncMock()
    session.get.return_value = MagicMock(aiohttp.ClientResponse)
    session.get.return_value.text = text_mock

    items = [{"id": j} for j in range(7)]

    builder = OrderedCollection(id="url", count=7, items=items)
    text_mock.return_value = json.dumps(builder.build())

    result = await actor.get_ordered_collection(url)
    session.get.assert_awaited_once()

    assert result["total_items"] == 7
    assert result["items"] == items


async def test_activity_pub_client_get_collection_pages():
    session = AsyncMock(aiohttp.ClientSession)
    url = "https://test_domain/test_path"
    public_key_url = "public_key_url"
    session = AsyncMock(aiohttp.ClientSession)
    session.get = AsyncMock()

    actor = BovineActor(
        actor_id="actor_id",
        public_key_url=public_key_url,
        secret=private_key,
    )
    await actor.init_session(session)

    text_mock = AsyncMock()
    session.get.return_value = MagicMock(aiohttp.ClientResponse)
    session.get.return_value.text = text_mock
    session.get.return_value.status = 200

    items = [{"id": j} for j in range(23)]

    builder = OrderedCollection(id="url", count=23, first="first", last="last")
    page_1 = OrderedCollectionPage(
        id="page_1", items=items[:13], part_of="url_1", next="next_1"
    )
    page_2 = OrderedCollectionPage(
        id="page_2", items=items[13:20], part_of="url_1", next="next_2"
    )
    page_3 = OrderedCollectionPage(id="page_3", items=items[20:], part_of="url_1")

    text_mock.side_effect = [
        json.dumps(builder.build()),
        json.dumps(page_1.build()),
        json.dumps(page_2.build()),
        json.dumps(page_3.build()),
    ]

    result = await actor.get_ordered_collection(url)

    assert result["total_items"] == 23
    assert result["items"] == items

    text_mock.side_effect = [
        json.dumps(builder.build()),
        json.dumps(page_1.build()),
        json.dumps(page_2.build()),
        json.dumps(page_3.build()),
    ]

    result = await actor.get_ordered_collection(url, max_items=17)

    assert result["total_items"] == 23
    assert result["items"] == items[:20]


async def test_bovine_actor_get_tombstone():
    actor = BovineActor(
        actor_id="actor_id",
        public_key_url="public_key_url",
        secret=private_key,
    )

    actor.client = AsyncMock(MooAuthClient)
    result = AsyncMock()
    result.status = 410
    actor.client.get.return_value = result

    result = await actor.get("https://tombstone.example")

    assert isinstance(result, dict)
    assert result["type"] == "Tombstone"


async def test_bovine_actor_get_forbidden():
    actor = BovineActor(
        actor_id="actor_id",
        public_key_url="public_key_url",
        secret=private_key,
    )

    actor.client = AsyncMock(SignedHttpClient)
    result = AsyncMock()
    result.status = 403
    result.raise_for_status = MagicMock(
        side_effect=aiohttp.ClientResponseError(
            MagicMock(request_info="test"), [], status=403, message="Error"
        )
    )
    actor.client.get.return_value = result

    with pytest.raises(aiohttp.ClientResponseError):
        await actor.get("https://tombstone.example")


async def test_bovine_actor_get_gone_not_ignored():
    actor = BovineActor(
        actor_id="actor_id",
        public_key_url="public_key_url",
        secret=private_key,
    )

    actor.client = AsyncMock(SignedHttpClient)
    result = AsyncMock()
    result.status = 403
    result.raise_for_status = MagicMock(
        side_effect=aiohttp.ClientResponseError(
            MagicMock(request_info="test"), [], status=403, message="Error"
        )
    )
    actor.client.get.return_value = result

    with pytest.raises(aiohttp.ClientResponseError):
        await actor.get("https://tombstone.example", create_tombstone=False)
