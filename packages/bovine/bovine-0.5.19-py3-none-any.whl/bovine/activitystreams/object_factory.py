# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT


"""

<!--
```
>>> bovine.utils.now_isoformat = lambda: '2024-09-26T18:35:42Z'

```
-->
"""

from dataclasses import dataclass, field
from typing import List, Optional, Set, Callable, Any

import bovine.utils

from .link import Link
from .utils import fediverse_handle_from_actor, id_for_object, property_for_key_as_set


@dataclass
class Object:
    """A dataclass representing an [ActivityStreams Object](https://www.w3.org/TR/activitystreams-vocabulary/#object-types)"""

    type: str
    attributed_to: Optional[str] = None
    followers: Optional[str] = None
    id: Optional[str] = None
    published: Optional[str] = None
    to: Set[str] = field(default_factory=set)
    cc: Set[str] = field(default_factory=set)

    name: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    source: Optional[dict] = None

    width: Optional[int] = None
    height: Optional[int] = None

    in_reply_to: Optional[str] = None
    url: Optional[str] = None
    tag: List[dict] = field(default_factory=list)
    attachment: List[dict] = field(default_factory=list)
    href: Optional[str] = None
    icon: Optional[dict] = None
    media_type: Optional[str] = None

    digest_multibase: str | None = None
    file_size: str | None = None
    duration: str | None = None

    def as_public(self):
        """makes the object public, i.e. public in to and followers in cc

        ```pycon
        >>> obj = Object(type="Note",
        ...     followers="http://actor.example/followers")
        >>> obj.as_public().build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Note',
            'to': ['https://www.w3.org/ns/activitystreams#Public'],
            'cc': ['http://actor.example/followers']}

        ```
        """
        self.to.add("https://www.w3.org/ns/activitystreams#Public")
        if self.followers:
            self.cc.add(self.followers)
        return self

    def as_followers(self):
        """addresses the object to followers, if they are set

        ```pycon
        >>> obj = Object(type="Note",
        ...     followers="http://actor.example/followers")
        >>> obj.as_followers().build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Note',
            'to': ['http://actor.example/followers']}

        ```
        """
        if self.followers:
            self.to.add(self.followers)
        return self

    def as_unlisted(self):
        """makes the object unlisted, i.e. public in cc and followers in to

        ```pycon
        >>> obj = Object(type="Note",
        ...     followers="http://actor.example/followers")
        >>> obj.as_unlisted().build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Note',
            'to': ['http://actor.example/followers'],
            'cc': ['https://www.w3.org/ns/activitystreams#Public']}

        ```
        """
        if self.followers:
            self.to.add(self.followers)
        self.cc.add("https://www.w3.org/ns/activitystreams#Public")
        return self

    def now(self):
        """Sets published to now in isoformat"""
        self.published = bovine.utils.now_isoformat()
        return self

    def build(self):
        """Returns the resulting object as a dictionary"""
        result = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "type": self.type,
        }

        if self.digest_multibase or self.file_size or isinstance(self.url, list):
            result["@context"] = [
                "https://www.w3.org/ns/activitystreams",
                "https://www.w3.org/ns/credentials/v2",
                {"size": "https://joinpeertube.org/ns#size"},
            ]

        extra_fields = {
            "attributedTo": self.attributed_to,
            "to": sorted(list(self.to)),
            "cc": sorted(list(self.cc - self.to)),
            "id": self.id,
            "inReplyTo": self.in_reply_to,
            "published": self.published,
            "source": self.source,
            "name": self.name,
            "url": self.url,
            "summary": self.summary,
            "content": self.content,
            "tag": self.tag,
            "attachment": self.attachment,
            "href": self.href,
            "width": self.width,
            "height": self.height,
            "icon": self.icon,
            "mediaType": self.media_type,
            "digestMultibase": self.digest_multibase,
            "size": self.file_size,
            "duration": self.duration,
        }

        for key, value in extra_fields.items():
            if value:
                result[key] = value

        if "to" in result and len(result["to"]) == 0:
            del result["to"]
        if "cc" in result and len(result["cc"]) == 0:
            del result["cc"]

        return result


@dataclass
class ObjectFactory:
    """ObjectFactory usually created through a BovineClient


    The property `id_generator` can also be supplied similarly to
    [ActivityFactory][bovine.activitystreams.activity_factory.ActivityFactory].
    """

    actor_information: dict | None = None
    actor: Any | None = field(
        default=None,
        metadata={
            "description": "set to BovineActor to retrieve actor when creating mentions"
        },
    )
    client: Any | None = field(
        default=None,
        metadata={
            "description": "set to BovineClient to retrieve actor when creating mentions"
        },
    )
    information: dict | None = None
    id_generator: Callable[[], str] | None = None

    def __post_init__(self):
        if self.client:
            self.information = self.client.information
        elif self.actor_information:
            self.client = None
            self.information = self.actor_information
        else:
            raise TypeError(
                "You need to either specify actor_information or a BovineClient"
            )

    def _defaults(self):
        result = dict(
            attributed_to=self.information["id"],
            published=bovine.utils.now_isoformat(),
        )
        if self.id_generator:
            result["id"] = self.id_generator()
        return result

    def note(self, **kwargs):
        """Creates a Note Object

        ```pycon
        >>> object_factory = ObjectFactory({"id": "http://actor.example"})
        >>> object_factory.note(content="Hello World!").build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Note',
            'attributedTo': 'http://actor.example',
            'published': '2024-09-26T18:35:42Z',
            'content': 'Hello World!'}

        ```

        For automatic addressing use for example [as_public][bovine.activitystreams.object_factory.Object.as_public]

        ```pycon
        >>> object_factory = ObjectFactory({"id": "http://actor.example",
        ...     "followers": "http://actor.example/followers"})
        >>> object_factory.note(content="Hello World!").as_public().build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Note',
            'attributedTo': 'http://actor.example',
            'to': ['https://www.w3.org/ns/activitystreams#Public'],
            'cc': ['http://actor.example/followers'],
            'published': '2024-09-26T18:35:42Z',
            'content': 'Hello World!'}

        ```

        """
        return Object(
            **self._defaults(),
            type="Note",
            followers=self.information.get("followers"),
            **kwargs,
        )

    def reply(self, obj: dict, **kwargs):
        """Creates a reply for an object. Reply is addressed
        to the author of object. Other recipients are set as
        cc.

        ```pycon
        >>> obj = Object(type="Note", attributed_to="http://other.example",
        ...     to={"http://other.example/followers"},
        ...     cc={"http://alice.example", "http://actor.example"}).build()
        >>> obj
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Note',
            'attributedTo': 'http://other.example',
            'to': ['http://other.example/followers'],
            'cc': ['http://actor.example', 'http://alice.example']}

        >>> object_factory = ObjectFactory({"id": "http://actor.example"})
        >>> object_factory.reply(obj, content="A message").build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Note',
            'attributedTo': 'http://actor.example',
            'to': ['http://other.example'],
            'cc': ['http://alice.example', 'http://other.example/followers'],
            'published': '2024-09-26T18:35:42Z',
            'content': 'A message'}

        ```
        :param obj: Object being replied to"""
        cc = (
            property_for_key_as_set(obj, "to") | property_for_key_as_set(obj, "cc")
        ) - {self.information["id"]}
        return Object(
            **self._defaults(),
            type=obj.get("type", "Note"),
            in_reply_to=obj.get("id"),
            followers=self.information.get("followers"),
            to={id_for_object(obj.get("attributedTo"))},
            cc=cc,
            **kwargs,
        )

    def article(self, **kwargs):
        """Creates an Article Object

        ```pycon
        >>> object_factory = ObjectFactory({"id": "http://actor.example"})
        >>> object_factory.article(content="Hello World!").build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Article',
            'attributedTo': 'http://actor.example',
            'published': '2024-09-26T18:35:42Z',
            'content': 'Hello World!'}

        ```
        """
        return Object(
            **self._defaults(),
            type="Article",
            followers=self.information.get("followers"),
            **kwargs,
        )

    def event(self, **kwargs):
        """Creates an Event Object

        ```pycon
        >>> object_factory = ObjectFactory({"id": "http://actor.example"})
        >>> object_factory.event(content="Hello World!").build()
        {'@context': 'https://www.w3.org/ns/activitystreams',
            'type': 'Event',
            'attributedTo': 'http://actor.example',
            'published': '2024-09-26T18:35:42Z',
            'content': 'Hello World!'}

        ```
        """
        return Object(
            **self._defaults(),
            type="Event",
            followers=self.information.get("followers"),
            **kwargs,
        )

    async def mention_for_actor_uri(self, actor_to_mention: str) -> Link:
        """Creates a mention object for another actor. Requires actor or client to be set.

        :param actor_to_mention: The URI of the actor to mention"""

        if self.client:
            remote_actor = await self.client.proxy(actor_to_mention)
        elif self.actor:
            remote_actor = await self.actor.get(actor_to_mention)
        else:
            raise TypeError("client or actor needs to be set at construction")

        return Link(
            type="Mention",
            href=actor_to_mention,
            name=fediverse_handle_from_actor(remote_actor),
        )

    async def reply_with_mention(self, obj: dict, **kwargs):
        """Creates a reply for an object, mentioning the author of the original
        post. This is necessary for compatibility with Mastodon

        :param obj: Object being replied to"""
        cc = (
            property_for_key_as_set(obj, "to") | property_for_key_as_set(obj, "cc")
        ) - {self.information["id"]}
        original_author = id_for_object(obj.get("attributedTo"))
        mention = (await self.mention_for_actor_uri(original_author)).build()
        return Object(
            **self._defaults(),
            type=obj.get("type", "Note"),
            in_reply_to=obj.get("id"),
            followers=self.information.get("followers"),
            to={original_author},
            cc=cc,
            tag=[mention],
            **kwargs,
        )
