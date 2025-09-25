# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

from urllib.parse import urlparse

uris_for_public = [
    "Public",
    "as:Public",
    "https://www.w3.org/ns/activitystreams#Public",
]
"""URIs used to represent the public collection. See [Section 5.6 of ActivityPub](https://www.w3.org/TR/activitypub/#public-addressing)."""


def actor_for_object(data: dict) -> str:
    """Look up for the actor id either from attributedTo or actor"""
    if "attributedTo" in data:
        actor = data.get("attributedTo")
    else:
        actor = data.get("actor")
    actor = id_for_object(actor)

    if actor:
        return actor

    return "__NO__ACTOR__"


def id_for_object(data: dict | str | None) -> str | None:
    """Determines the id of an object

    ```pycon
    >>> id_for_object("http://obj.example")
    'http://obj.example'

    >>> id_for_object({"id": "http://obj.example"})
    'http://obj.example'

    >>> id_for_object({"name": "alice"}) is None
    True

    ```
    """

    if data is None:
        return None
    if isinstance(data, str):
        return data
    return data.get("id", None)


def property_for_key_as_set(data, key):
    """Returns value as a set, useful for `to` and `cc`

    ```pycon
    >>> property_for_key_as_set({"to": "http://actor.example"}, "to")
    {'http://actor.example'}

    ```
    """
    if data is None:
        return set()
    result = data.get(key, [])
    if isinstance(result, str):
        return set([result])
    return set(result)


def recipients_for_object(data: dict) -> set:
    """Combines the recipients from to, cc, bto, bcc, audience into a set

    ```pycon
    >>> result = recipients_for_object({
    ...     "to": ["http://to.example"],
    ...     "cc": "http://cc.example",
    ...     "bcc": ["http://bcc.example"],
    ...     "audience": "http://audience.example"})
    >>> sorted(result)
    ['http://audience.example', 'http://bcc.example',
        'http://cc.example', 'http://to.example']


    ```

    !!! note
        treatment of audience might change.

    """
    return set.union(
        *[
            property_for_key_as_set(data, key)
            for key in ["to", "cc", "bto", "bcc", "audience"]
        ]
    )


def remove_public(recipients):
    """Given a list of Recipients removes public

    ```pycon
    >>> remove_public(["Public", "as:Public",
    ...     "https://www.w3.org/ns/activitystreams#Public",
    ...     "http://alice.example"])
    {'http://alice.example'}

    ```
    """

    return {x for x in recipients if x not in uris_for_public}


def contains_public(array: list[str]) -> bool:
    """Checks if the list contains public

    ```pycon
    >>> contains_public(["Public"])
    True

    >>> contains_public(["http://alice.example"])
    False

    ```
    """

    return any(x in uris_for_public for x in array)


def is_public(data: dict) -> bool:
    """Determines if the object should be considered public based on its recipients"""
    return contains_public(recipients_for_object(data))


def fediverse_handle_from_actor(actor: dict) -> str:
    """Given an actor object, i.e. a dict, determines the fediverse handle"""
    host = urlparse(actor["id"]).netloc
    username = urlparse(actor["id"]).path.split("/")[-1]

    if "preferredUsername" in actor:
        username = actor["preferredUsername"]

    return f"{username}@{host}"


def copy_to_and_cc(origin: dict, destination: dict) -> dict:
    """Copies the audience from the origin object to the destination object"""

    for key in ["to", "cc", "bto", "bcc", "audience"]:
        if key in origin:
            destination[key] = list(
                property_for_key_as_set(origin, key)
                | property_for_key_as_set(destination, key)
            )

    return destination


def as_list(value: dict | list | str) -> list:
    """Converts a value to a list by enclosing it

    ```pycon
    >>> as_list("http://example.com")
    ['http://example.com']

    >>> as_list(["http://example.com"])
    ['http://example.com']

    ```

    """

    if isinstance(value, list):
        return value

    return [value]


def combine_as_list(*values: list) -> list:
    """Combines the values into a list. Lists are combined,
    non list items are added as members

    ```pycon
    >>> combine_as_list("http://one.test", ["http://two.test"])
    ['http://one.test', 'http://two.test']

    ```
    """

    return sum((as_list(x) for x in values), [])
