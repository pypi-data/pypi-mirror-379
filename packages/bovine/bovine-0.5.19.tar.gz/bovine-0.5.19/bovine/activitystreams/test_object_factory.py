# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

import pytest
from unittest.mock import AsyncMock

from .object_factory import ObjectFactory


def test_object_factory() -> None:
    object_factory = ObjectFactory({"id": "actor_id", "followers": "followers"})

    note = object_factory.note().as_public()
    note.content = "text"
    result = note.build()

    assert set(result.keys()) == {
        "@context",
        "attributedTo",
        "content",
        "type",
        "to",
        "cc",
        "published",
    }

    assert result["to"] == ["https://www.w3.org/ns/activitystreams#Public"]
    assert result["cc"] == ["followers"]


def test_object_factory_now() -> None:
    object_factory = ObjectFactory({"id": "actor_id", "followers": "followers"})

    note = object_factory.note(content="text").as_public().now()
    result = note.build()

    assert set(result.keys()) == {
        "@context",
        "attributedTo",
        "published",
        "content",
        "type",
        "to",
        "cc",
    }

    assert result["to"] == ["https://www.w3.org/ns/activitystreams#Public"]
    assert result["cc"] == ["followers"]


async def test_mention_for_actor_uri() -> None:
    mock_client = AsyncMock()
    remote_uri = "https://remote/alice"

    mock_client.proxy.return_value = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": remote_uri,
        "type": "Person",
        "preferredUsername": "alyssa",
    }

    object_factory = ObjectFactory(client=mock_client)

    mention_object = await object_factory.mention_for_actor_uri(remote_uri)
    mention = mention_object.build()

    assert set(mention.keys()) == {"@context", "type", "href", "name"}
    assert mention["type"] == "Mention"
    assert mention["href"] == remote_uri
    assert mention["name"] == "alyssa@remote"


async def test_mention_for_actor_uri_actor() -> None:
    mock_actor = AsyncMock()
    remote_uri = "https://remote/alice"

    mock_actor.get.return_value = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": remote_uri,
        "type": "Person",
        "preferredUsername": "alyssa",
    }

    object_factory = ObjectFactory(
        actor=mock_actor, actor_information={"id": "actor_id"}
    )

    mention_object = await object_factory.mention_for_actor_uri(remote_uri)
    mention = mention_object.build()

    assert set(mention.keys()) == {"@context", "type", "href", "name"}
    assert mention["type"] == "Mention"
    assert mention["href"] == remote_uri
    assert mention["name"] == "alyssa@remote"


@pytest.mark.parametrize(
    "remote_actor", ["remote_id", {"id": "remote_id", "type": "Person"}]
)
@pytest.mark.parametrize("cc", [["third_id"], "third_id"])
async def test_object_factory_reply(remote_actor, cc) -> None:
    object_factory = ObjectFactory({"id": "actor_id", "followers": "followers"})

    note = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "type": "Note",
        "id": "note_id",
        "attributedTo": remote_actor,
        "to": ["actor_id", "second_id"],
        "cc": cc,
    }

    reply = object_factory.reply(note).build()

    assert reply["attributedTo"] == "actor_id"
    assert reply["inReplyTo"] == "note_id"
    assert set(reply["to"]) == {"remote_id"}
    assert set(reply["cc"]) == {"second_id", "third_id"}
