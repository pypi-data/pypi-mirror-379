# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

import json
import logging
from typing import Optional, Callable, Tuple
from urllib.parse import urlencode, urlparse
import warnings
import tomllib

from .activitystreams import Collection
from .activitystreams.activity_factory import ActivityFactory
from .activitystreams.collection_helper import CollectionHelper
from .activitystreams.object_factory import ObjectFactory, Object
from .clients.authorization_wrapper import AuthorizationWrapper
from .utils import activity_pub_object_id_from_html_body

logger = logging.getLogger(__name__)


class BovineClient(AuthorizationWrapper):
    """BovineClient is meant to serve as the basis of building ActivityPub Clients.
    It defines methods for interacting with the endpoints defined by the corresponding
    ActivityPub Actor: inbox, outbox, and proxyUrl.

    Usage is either:

    ```pycon
    async with BovineClient(**config) as actor:
        pass
    ```

    or

    ```python
    actor = BovineClient(**config)
    await actor.init()
    await do_something(actor)
    ```

    I still call the variable actor as it represents the ActivityPub Actor through
    a client.

    :param domain: Specifies the domain the actor is on, used for Moo-Auth-1
    :param host: Alias for domain
    :param actor_id: URI of the actor, used for Bearer Auth and HTTP Signatures
    :param account_url: Alias for actor_id
    :param secret: The private key material for Moo-Auth-1 and HTTP Signatures
    :param access_token: The access token for Bearer auth
    :param public_key_url: The URI of the public key.
    """

    def __init__(
        self,
        domain: str | None = None,
        host: str | None = None,
        actor_id: str | None = None,
        account_url: str | None = None,
        secret: str | None = None,
        public_key_url: str | None = None,
        access_token: str | None = None,
        **kwargs,
    ):
        if host:
            warnings.warn(
                "Parameter host will be deprecated with bovine 0.6.0 use domain instead",
                DeprecationWarning,
            )
        if account_url:
            warnings.warn(
                "Parameter account_url will be deprecated with bovine 0.6.0 use actor_id instead",
                DeprecationWarning,
            )
        super().__init__(
            domain=domain if domain else host,
            secret=secret,
            actor_id=actor_id if actor_id else account_url,
            public_key_url=public_key_url,
            access_token=access_token,
        )

        self.information: Optional[dict] = None
        self._activity_factory = None
        self._object_factory = None

    async def get(self, target):
        assert self.client

        response = await self.client.get(target)
        response.raise_for_status()
        return json.loads(await response.text())

    async def init(self, session=None):
        """Manually initializes the BovineClient for cases when
        not used within async with. Also loads the actor information.

        :param session:
            can be used to specify an existing aiohttp.ClientSession. Otherwise a new
            one is created.
        """

        await super().init_session(session=session)

        if self.client is None:
            raise Exception("Client not set in BovineClient")
        self.information = await self.get(self.actor_id)

        logger.debug("Retrieved information %s", self.information)

        if any(required not in self.information for required in ["inbox", "outbox"]):
            raise Exception("Retrieved incomplete actor data")

    async def send_to_outbox(self, data: dict):
        """sends data to outbox of actor

        :param data: The data to send as python dict

        :return:
            The aiohttp.ClientResponse object. This means
            return_value.headers["location"] will contain the id of the
            posted activity.
        """
        if self.information is None:
            await self.init()

        assert self.client

        return await self.client.post(self.information["outbox"], json.dumps(data))

    async def proxy(self, target: str):
        """Retrieve's an element through the actors' proxyUrl endpoint
        as specified in ActivityPub.

        :param target: The URL of the object to retrieve


        FIXME: Support for non-json stuff"""
        response = await self.client.post(
            self.information["endpoints"]["proxyUrl"],
            urlencode({"id": target}),
            content_type="application/x-www-form-urlencoded",
        )
        response.raise_for_status()
        return await response.json()

    async def event_source(self):
        """Returns an EventSource corresponding to the actor's

        The syntax for this will probably change"""
        if self.information is None:
            await self.load()

        event_source_url = self.information["endpoints"]["eventSource"]
        return self.client.event_source(event_source_url)

    async def simplify_collection(self, collection):
        """Returns a Collection containing all items from the passed collection
        or collection id"""
        # items = await all_collection_elements(self, collection)

        items = []

        if isinstance(collection, str):
            collection_id = collection
        else:
            collection_id = collection.get("id")
        return Collection(id=collection_id, items=items).build()

    @property
    def activity_factory(self):
        """Returns an ActivityFactory for objects corresponding to the client's actor"""
        if self._activity_factory is None:
            self._activity_factory = ActivityFactory(self.information)
        return self._activity_factory

    @property
    def object_factory(self):
        """Returns an ObjectFactory for objects corresponding to the client's actor"""
        if self._object_factory is None:
            self._object_factory = ObjectFactory(client=self)
        return self._object_factory

    @property
    def factories(self):
        return self.activity_factory, self.object_factory

    @property
    def host(self):
        """The host the actor is on"""
        return urlparse(self.actor_id).netloc

    @property
    def followers(self) -> str:
        """The id of the follows collection"""
        return self.information["followers"]

    def inbox(self, resolve=True):
        """Provides a CollectionHelper for the Actors inbox"""
        inbox_collection = CollectionHelper(
            self.information["inbox"], self, resolve=resolve
        )
        return inbox_collection

    def outbox(self, resolve=True):
        """Provides a CollectionHelper for the Actors outbox"""
        outbox_collection = CollectionHelper(
            self.information["outbox"], self, resolve=resolve
        )
        return outbox_collection

    def collection_helper(self, collection, resolve=False):
        """Returns a CollectionHelper for the collection provided. Usage:

        ```python
        async for x in client.collection_helper(uri_of_collection):
            await do_something(x)
        ```

        :param collection: Uri of the collection to irater over
        :param resolve: If true objects are automatically fetched"""

        return CollectionHelper(collection, self, resolve=resolve)

    @staticmethod
    def from_file(config_file: str):
        """Initializes the BovineClient from a toml config file"""
        with open(config_file, "rb") as fp:
            config = tomllib.load(fp)

        return BovineClient(**config)


class BovineActor(AuthorizationWrapper):
    r"""Defines the Bovine version of an ActivityPub Actor. This class is meant
    to be used when implementing an ActivityPub Server in order to handle the
    HTTP requests to another server.

    Currently most of these interactions use HTTP Signatures.

    Usage is either:

    ```python
    async with BovineActor(**config) as actor:
        await do_something(actor)
    ```

    or

    ```python
    actor = BovineActor(**config)
    await actor.init()
    await do_something(actor)
    ```

    Details of the `**config` parameter can be found in the documentation
    of [AuthorizationWrapper][bovine.clients.authorization_wrapper.AuthorizationWrapper]


    :param domain: Specifies the domain the actor is on, used for Moo-Auth-1
    :param host: Alias for domain
    :param actor_id: URI of the actor, used for Bearer Auth and HTTP Signatures
    :param account_url: Alias for actor_id
    :param secret: The private key material for Moo-Auth-1 and HTTP Signatures
    :param access_token: The access token for Bearer auth
    :param digest_method: Set to [content_digest_sha256_rfc_9530][bovine.crypto.helper.content_digest_sha256_rfc_9530] to use Content-Digest according to  RFC 9530. Set to [legacy_digest_method_uppercase][bovine.clients.signed_http.legacy_digest_method_uppercase] for `SHA-256`.
    :param public_key_url: The URI of the public key.
    """

    def __init__(
        self,
        domain: str | None = None,
        host: str | None = None,
        actor_id: str | None = None,
        account_url: str | None = None,
        secret: str | None = None,
        public_key_url: str | None = None,
        access_token: str | None = None,
        digest_method: Callable[[bytes], Tuple[str, str]] | None = None,
        **kwargs,
    ):
        if host:
            warnings.warn(
                "Parameter host will be deprecated with bovine 0.6.0 use domain instead",
                DeprecationWarning,
            )
        if account_url:
            warnings.warn(
                "Parameter account_url will be deprecated with bovine 0.6.0 use actor_id instead",
                DeprecationWarning,
            )
        super().__init__(
            domain=domain if domain else host,
            secret=secret,
            actor_id=actor_id if actor_id else account_url,
            public_key_url=public_key_url,
            access_token=access_token,
            digest_method=digest_method,
        )

    async def init(self, session=None):
        """Manually initializes the BovineActor for cases when not used
        within async with

        :param session:
            can be used to specify an existing aiohttp.ClientSession. Otherwise a new
            one is created.
        """

        await super().init_session(session=session)

    async def post(self, target: str, data: dict):
        """Send a signed post with data to target

        :param target: The URL to send the request to
        :param data: Data to send
        """
        response = await self.client.post(target, json.dumps(data))
        logger.debug("POST to %s got %d", target, response.status)
        response.raise_for_status()

        return response

    async def get(
        self, target: str, fail_silently: bool = False, create_tombstone: bool = True
    ):
        """Retrieve target with a get. An exception is raised if the request fails

        :param target: The URL of the object to retrieve
        :param fail_silently: do not raise an exception if the request fails
        :param create_tombstone: Return a tombstone for status code 404 and 410.
        """
        response = await self.client.get(target)
        logger.debug("GET for %s got status code %d", target, response.status)

        if response.status >= 300 and response.status < 400:
            if "Location" in response.headers:
                location = response.headers["Location"]
                logger.debug("GET for %s redirected to %s", target, location)
                return await self.get(location)
            return None

        if create_tombstone and response.status in [404, 410]:
            try:
                body = await response.text()
                result = json.loads(body)
                if result["type"] == "Tombstone":
                    return result
            except Exception:
                ...

            return Object(type="Tombstone", id=target).build()
        if fail_silently and response.status >= 400:
            return None

        response.raise_for_status()

        body = await response.text()

        try:
            return json.loads(body)
        except Exception:
            # if "json" not in response.headers.get("Content-Type"):
            if "alternate" in response.links:
                link_header = response.links["alternate"]
                if "json" in link_header.get("type", ""):
                    location = str(link_header["url"])
                    logger.debug(
                        "GET for %s redirected to %s due to Link Header",
                        target,
                        location,
                    )

                    return await self.get(location, fail_silently=fail_silently)

            object_id = activity_pub_object_id_from_html_body(body)

            if object_id:
                logger.debug(
                    "GET for %s redirected to %s due to HTML parsing", target, object_id
                )

                return await self.get(object_id, fail_silently=fail_silently)
            else:
                return None

    async def get_ordered_collection(self, url: str, max_items: Optional[int] = None):
        """Retrieve target ordered collection

        :param url: url of the ordered collection
        :param max_items: maximal number of items to retrieve, use None for all
        """
        result = await self.client.get(url)
        result.raise_for_status()

        data = json.loads(await result.text())

        total_number_of_items = data["totalItems"]
        items = []

        if "orderedItems" in data:
            items = data["orderedItems"]

        if len(items) == total_number_of_items:
            return {"total_items": total_number_of_items, "items": items}

        if "first" in data:
            page_data = await self.get(data["first"])

            items = page_data["orderedItems"]

            while "next" in page_data and len(page_data["orderedItems"]) > 0:
                if max_items and len(items) > max_items:
                    return {"total_items": total_number_of_items, "items": items}

                page_data = await self.get(page_data["next"])

                items += page_data["orderedItems"]

        return {"total_items": total_number_of_items, "items": items}

    @staticmethod
    def from_file(config_file: str):
        with open(config_file, "rb") as fp:
            config = tomllib.load(fp)

        return BovineActor(**config)
