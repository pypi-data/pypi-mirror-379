# SPDX-FileCopyrightText: 2023-2024 Helge
#
# SPDX-License-Identifier: MIT

from dataclasses import dataclass, field
from typing import Optional, Tuple, Dict, Any, Callable

import logging

from bovine.types import Visibility

from .activity_factory import ActivityFactory
from .object_factory import ObjectFactory
from .controller import Controller
from .utils import combine_as_list

logger = logging.getLogger(__name__)


def factories_for_actor_object(
    actor_profile: dict, id_generator: Callable[[], str] | None = None
) -> Tuple[ActivityFactory, ObjectFactory]:
    """Builds activity and object factories from actor object

    :param actor_profile: The actor profile as a dictionary
    :param id_generator: A function returning an id for objects
    :return: Activity- and object factory
    """
    return ActivityFactory(actor_profile, id_generator=id_generator), ObjectFactory(
        actor_information=actor_profile, id_generator=id_generator
    )


@dataclass
class WithPublicKey:
    """Represents an object having a legacy public key specified under the `publicKey` key"""

    public_key: Optional[str] = None
    public_key_name: Optional[str] = None

    def build_public_key(self, id) -> dict | None:
        if self.public_key:
            return {
                "@context": "https://w3id.org/security/v1",
                "publicKey": {
                    "id": f"{id}#{self.public_key_name}",
                    "owner": id,
                    "publicKeyPem": self.public_key,
                },
            }
        return None


@dataclass
class Actor(WithPublicKey, Controller):
    """Actor class represents the basic ActivityStreams actor.

    ```pycon
    >>> actor = Actor(id="http://actor.example",
    ...     inbox="http://actor.example/inbox",
    ...     outbox="http://actor.example/outbox")
    >>> actor.build()
    {'@context': 'https://www.w3.org/ns/activitystreams',
        'id': 'http://actor.example',
        'type': 'Person',
        'inbox': 'http://actor.example/inbox',
        'outbox': 'http://actor.example/outbox'}

    ```

    By using properties, one can specify additional information, e.g.

    ```pycon
    >>> actor = Actor(id="http://actor.example",
    ...     properties={"@context": {"PropertyValue": "https://schema.org/PropertyValue",
    ...         "value": "https://schema.org/value"},
    ...         "attachment": [{"type": "PropertyValue",
    ...             "name": "key", "value": "value"}]})
    >>> actor.build()
    {'@context': ['https://www.w3.org/ns/activitystreams',
        {'PropertyValue': 'https://schema.org/PropertyValue', 'value': 'https://schema.org/value'}],
        'attachment': [{'type': 'PropertyValue',
            'name': 'key',
            'value': 'value'}],
        'id': 'http://actor.example',
        'type': 'Person',
        'inbox': 'http://actor.example',
        'outbox': 'http://actor.example'}

    ```

    """

    id: str | None = None
    type: str = "Person"
    name: str | None = field(
        default=None, metadata={"description": "Display name used fro the actor."}
    )
    preferred_username: Optional[str] = None
    inbox: str | None = field(
        default=None, metadata={"description": "URI of the inbox"}
    )
    outbox: str | None = field(
        default=None, metadata={"description": "URI of the outbox"}
    )
    followers: str | None = field(
        default=None, metadata={"description": "URI of the followers collection"}
    )
    following: str | None = field(
        default=None, metadata={"description": "URI of the following collection"}
    )
    event_source: Optional[str] = None
    proxy_url: Optional[str] = None

    summary: str | None = field(
        default=None, metadata={"description": "Short description of the actor"}
    )
    icon: Optional[dict] = None
    url: str | None = field(default=None, metadata={"description": "URL of the actor"})

    properties: Dict[str, Any] = field(
        default_factory=dict,
        metadata={
            "description": "Additional properties that can be added to the actor"
        },
    )

    def combine_with_public_key(self, result):
        public_key = self.build_public_key(self.id)

        if public_key:
            result["@context"] = combine_as_list(
                result["@context"], public_key["@context"]
            )
            return {**public_key, **result}

        return result

    def combine_with_controller(self, result):
        controller = super().build()

        if "@context" in controller:
            result["@context"] = combine_as_list(
                result["@context"], controller["@context"]
            )
            return {**controller, **result}

        return result

    def combine_with_properties(self, result):
        if (
            "@context" in self.properties
            and self.properties["@context"] != "about:bovine"
        ):
            result["@context"] = combine_as_list(
                result["@context"], self.properties["@context"]
            )
        return {**self.properties, **result}

    def build(self, visibility: Visibility = Visibility.PUBLIC) -> dict:
        """Creates the json-ld representation of the actor.

        ```pycon
        >>> actor = Actor(id="http://actor.example",
        ...     inbox="http://actor.example/inbox",
        ...     outbox="http://actor.example/outbox",
        ...     followers="http://actor.example/followers",
        ...     public_key="PEM", public_key_name="name")
        >>> actor.build(visibility=Visibility.WEB)
        {'@context': ['https://www.w3.org/ns/activitystreams',
                'https://w3id.org/security/v1'],
            'publicKey': {'id': 'http://actor.example#name',
                'owner': 'http://actor.example',
                'publicKeyPem': 'PEM'},
            'id': 'http://actor.example',
            'type': 'Person'}

        >>> actor.build(visibility=Visibility.PUBLIC)
        {'@context': ['https://www.w3.org/ns/activitystreams',
                'https://w3id.org/security/v1'],
            'publicKey': {'id': 'http://actor.example#name',
                'owner': 'http://actor.example',
                'publicKeyPem': 'PEM'},
            'id': 'http://actor.example',
            'type': 'Person',
            'inbox': 'http://actor.example/inbox',
            'outbox': 'http://actor.example/outbox'}


        >>> actor.build(visibility=Visibility.OWNER)
        {'@context': ['https://www.w3.org/ns/activitystreams',
                'https://w3id.org/security/v1'],
            'publicKey': {'id': 'http://actor.example#name',
                'owner': 'http://actor.example',
                'publicKeyPem': 'PEM'},
            'id': 'http://actor.example',
            'type': 'Person',
            'inbox': 'http://actor.example/inbox',
            'outbox': 'http://actor.example/outbox',
            'followers': 'http://actor.example/followers'}


        ```

        !!! note
            The visibility parameter might change if the community decides on best practices.

        :param visibility: Determines which properties of the actor to show
        """
        result = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": self.id,
            "type": self.type,
            **self._build_endpoints(visibility=visibility),
        }
        result = self.combine_with_public_key(result)
        result = self.combine_with_controller(result)
        result = self.combine_with_properties(result)

        if self.preferred_username:
            result["preferredUsername"] = self.preferred_username

        if visibility == Visibility.WEB:
            return result

        if self.name:
            result["name"] = self.name
        elif self.preferred_username:
            result["name"] = self.preferred_username

        for key, value in {
            "summary": self.summary,
            "icon": self.icon,
            "url": self.url,
        }.items():
            if value is not None:
                result[key] = value

        return result

    def _build_endpoints(self, visibility):
        result = {}

        if visibility == Visibility.WEB:
            return result

        if self.inbox:
            result["inbox"] = self.inbox
        else:
            result["inbox"] = self.id

        if self.outbox:
            result["outbox"] = self.outbox
        else:
            result["outbox"] = self.id

        if visibility != Visibility.OWNER:
            return result

        endpoints = self._build_user_endpoints()
        if endpoints:
            result["endpoints"] = endpoints

        if self.followers:
            result["followers"] = self.followers
        if self.following:
            result["following"] = self.following

        return result

    def _build_user_endpoints(self):
        endpoints = {}
        if self.event_source:
            endpoints["eventSource"] = self.event_source
        if self.proxy_url:
            endpoints["proxyUrl"] = self.proxy_url
        return endpoints


@dataclass
class Collection:
    """Represents a Collection

    See [Collection](https://www.w3.org/TR/activitystreams-core/#collections)


    ```pycon
    >>> Collection("http://list.example",
    ...     items=["http://item.example"]).build()
    {'@context': 'https://www.w3.org/ns/activitystreams',
        'id': 'http://list.example',
        'type': 'Collection',
        'items': ['http://item.example']}

    ```

    """

    id: str
    items: list

    def build(self) -> dict:
        return {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": self.id,
            "type": "Collection",
            "items": self.items,
        }


@dataclass
class OrderedCollection:
    """Represents an OrderedCollection

    See [Collection](https://www.w3.org/TR/activitystreams-core/#collections)

    ```pycon
    >>> OrderedCollection("http://list.example").build()
    {'@context': 'https://www.w3.org/ns/activitystreams',
        'id': 'http://list.example',
        'type': 'OrderedCollection'}

    ```

    One can set `totalItems` via `count`

    ```pycon
    >>> OrderedCollection("http://list.example", count=0).build()
    {'@context': 'https://www.w3.org/ns/activitystreams',
        'id': 'http://list.example',
        'type': 'OrderedCollection',
        'totalItems': 0}

    ```


    If items is set, count is automatically updated

    ```pycon
    >>> OrderedCollection("http://list.example",
    ...     items=["http://item.example"]).build()
    {'@context': 'https://www.w3.org/ns/activitystreams',
        'id': 'http://list.example',
        'type': 'OrderedCollection',
        'totalItems': 1,
        'orderedItems': ['http://item.example']}

    ```

    Finally, one can use this as
    ```pycon
    >>> OrderedCollection("http://list.example",
    ...     first="http://list.example/first",
    ...     last="http://list.example/last").build()
    {'@context': 'https://www.w3.org/ns/activitystreams',
        'id': 'http://list.example',
        'type': 'OrderedCollection',
        'first': 'http://list.example/first',
        'last': 'http://list.example/last'}

    ```
    """

    id: str
    items: list | None = None
    count: int | None = None
    first: str | None = None
    last: str | None = None

    def build(self) -> dict:
        if self.items:
            self.count = len(self.items)

        result = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": self.id,
            "type": "OrderedCollection",
        }

        if self.count is not None:
            result["totalItems"] = self.count

        if self.items:
            result["orderedItems"] = self.items

        if self.first:
            result["first"] = self.first

        if self.last:
            result["last"] = self.last

        return result


@dataclass
class OrderedCollectionPage:
    """Represents an OrderedCollectionPage"""

    id: str
    items: list
    part_of: str
    next: str | None = None
    prev: str | None = None

    def build(self) -> dict:
        result = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": self.id,
            "partOf": self.part_of,
            "orderedItems": self.items,
            "type": "OrderedCollectionPage",
        }

        if self.next:
            result["next"] = self.next

        if self.prev:
            result["prev"] = self.prev

        return result
