# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

from .activity_factory import ActivityFactory
from .object_factory import Object


def test_activity_factory_like() -> None:
    activity_factory = ActivityFactory({"id": "actor_id", "followers": "followers"})

    like = activity_factory.like("target")
    like.to.add("target")
    like.cc.add("other")
    like.content = "🐮"

    result = like.build()

    assert result["@context"] == "https://www.w3.org/ns/activitystreams"

    assert result["to"] == ["target"]
    assert result["cc"] == ["other"]

    assert result["type"] == "Like"

    assert result.get("published")


def test_activity_factory_accept() -> None:
    activity_factory = ActivityFactory({"id": "actor_id", "followers": "followers"})

    accept = activity_factory.accept({"id": "obj"}, include_activity=True)
    result = accept.build()

    assert result["@context"] == "https://www.w3.org/ns/activitystreams"
    assert result["type"] == "Accept"
    assert result["actor"] == "actor_id"
    assert result["object"]["id"] == "obj"


def test_activity_factory_create():
    activity_factory = ActivityFactory({"id": "actor_id", "followers": "followers"})
    note = (
        Object(type="Note", attributed_to="actor_id", followers="account/followers")
        .as_public()
        .build()
    )

    result = activity_factory.create(note).build()

    assert result["cc"] == ["account/followers"]
    assert result["to"] == ["https://www.w3.org/ns/activitystreams#Public"]
    assert result["actor"] == "actor_id"


def test_activity_factory_update_for_actor():
    actor_profile = {"id": "actor_id", "followers": "followers"}
    activity_factory = ActivityFactory(actor_profile)

    result = activity_factory.update(actor_profile).as_public().build()

    assert result["cc"] == ["followers"]
    assert result["to"] == ["https://www.w3.org/ns/activitystreams#Public"]
    assert result["actor"] == "actor_id"


def test_activity_factory_create_two_attributed_to():
    activity_factory = ActivityFactory({"id": "actor_id", "followers": "followers"})
    note = (
        Object(
            type="Note",
            attributed_to=["actor_id", "other_actor"],
            followers="account/followers",
        )
        .as_public()
        .build()
    )

    result = activity_factory.create(note).build()

    assert result["cc"] == ["account/followers"]
    assert result["to"] == ["https://www.w3.org/ns/activitystreams#Public"]
    assert result["actor"] == "actor_id"


def test_activity_factory_create_no_cc() -> None:
    activity_factory = ActivityFactory({"id": "actor_id", "followers": "followers"})
    remote_actor = "https://abel/alice"
    note = Object(
        type="Note",
        attributed_to="actor_id",
        followers="account/followers",
        to={remote_actor},
    ).build()

    result = activity_factory.create(note).build()

    assert "cc" not in result
    assert result["to"] == [remote_actor]
    assert result["actor"] == "actor_id"


def test_activity_no_empty_to_cc() -> None:
    activity_factory = ActivityFactory({"id": "actor_id", "followers": "followers"})

    result = activity_factory.delete("target").build()

    assert set(result.keys()) == {"@context", "type", "object", "actor", "published"}


def test_activity_undo() -> None:
    activity_factory = ActivityFactory({"id": "actor_id", "followers": "followers"})

    result = activity_factory.undo("target").build()

    assert result["object"] == "target"
