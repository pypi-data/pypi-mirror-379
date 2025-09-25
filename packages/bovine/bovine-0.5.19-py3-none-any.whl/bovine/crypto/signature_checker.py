# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

import logging
import json
import warnings


from urllib.parse import urlparse
from dataclasses import dataclass, field
from typing import Callable, Awaitable, Tuple
import bovine.utils
from bovine.utils import parse_gmt

from .http_signature import HttpSignature
from .signature import Signature, RFC9421Signature
from .types import CryptographicIdentifier

from .digest import validate_digest

logger = logging.getLogger(__name__)


@dataclass
class SignatureChecker:
    """Dataclass to encapsulate the logic of checking a HTTP signature"""

    key_retriever: Callable[
        [str], Awaitable[Tuple[str | None, str | None] | CryptographicIdentifier | None]
    ] = field(
        metadata={
            "description": "used to resolve the keyId to the cryptographic information"
        }
    )
    skip_digest_check: bool = field(
        default=False, metadata={"description": "Set to true to skip digest check"}
    )

    async def handle_rfc9421_signature(
        self,
        method: str,
        url: str,
        headers: dict,
        body: Callable[[], Awaitable[str | bytes]],
    ) -> str | None:
        parsed_signature = RFC9421Signature.from_headers(
            headers["signature-input"], headers["signature"]
        )
        key_result = await self.key_retriever(parsed_signature.key_id)

        if key_result is None:
            logger.info(f"Could not retrieve key from {parsed_signature.key_id}")
            return None

        http_signature = self.build_rfc9421_http_signature(
            parsed_signature, method, url, headers
        )
        return http_signature.verify_with_identity_quoted(
            key_result, parsed_signature.signature
        )

    async def validate_signature(
        self,
        method: str,
        url: str,
        headers: dict,
        body: Callable[[], Awaitable[str | bytes]] | None,
    ) -> str | None:
        """Valids a given signature

        :param method: The http method either get or post
        :param url: The url being queried
        :param headers: The request headers
        :param body: A coroutine resolving the the request body. Used for post requests to check the digest.

        :returns:
        """
        if "signature" not in headers:
            logger.debug("Signature not present on request for %s", url)
            logger.debug(json.dumps(dict(headers)))
            return None

        if method.lower() == "post" and not self.skip_digest_check:
            if not self.validate_digest(headers, await body()):
                logger.warning("Validating digest failed")
                return None

        if "signature-input" in headers:
            logger.info("RFC 9421 Signature")
            return await self.handle_rfc9421_signature(method, url, headers, body)

        try:
            parsed_signature = Signature.from_signature_header(headers["signature"])
            signature_fields = parsed_signature.fields

            if (
                "(request-target)" not in signature_fields
                or "date" not in signature_fields
            ):
                logger.warning("Required field not present in signature")
                return None

            if method.lower() == "post" and all(
                field not in signature_fields for field in ["digest", "content-digest"]
            ):
                logger.warning("Digest not present, but computable")
                return None

            http_date = parse_gmt(headers["date"])
            if not bovine.utils.check_max_offset_now(http_date):
                logger.warning(f"Encountered invalid http date {headers['date']}")
                return None

            key_result = await self.key_retriever(parsed_signature.key_id)
            if isinstance(key_result, tuple):
                warnings.warn(
                    "Returning a tuple from key_retriever is deprecated, return a CryptographicIdentifier instead, will be remove in bovine 0.6.0",
                    DeprecationWarning,
                )
                logger.warn(
                    "Returning a tuple from key_retriever is deprecated, return a CryptographicIdentifier instead, will be remove in bovine 0.6.0"
                )
                key_result = CryptographicIdentifier.from_pem(*key_result)

            if key_result is None:
                logger.debug(f"Could not retrieve key from {parsed_signature.key_id}")
                return None

            http_signature = self.build_http_signature(
                signature_fields, method, url, parsed_signature, headers
            )

            return http_signature.verify_with_identity(
                key_result, parsed_signature.signature
            )

        except Exception as e:
            logger.exception(str(e))
            logger.error(headers)
            return None

        return None

    def build_http_signature(
        self, signature_fields, method, url, parsed_signature, headers
    ):
        http_signature = HttpSignature()
        for parsed_field in signature_fields:
            match parsed_field:
                case "(request-target)":
                    method = method.lower()
                    parsed_url = urlparse(url)
                    path = parsed_url.path
                    http_signature.with_field(parsed_field, f"{method} {path}")
                case "(expires)":
                    http_signature.with_field(parsed_field, parsed_signature.expires)
                case "(created)":
                    http_signature.with_field(parsed_field, parsed_signature.created)
                case _:
                    http_signature.with_field(parsed_field, headers[parsed_field])
        return http_signature

    def build_rfc9421_http_signature(self, parsed_signature, method, url, headers):
        http_signature = HttpSignature()
        for parsed_field in parsed_signature.fields:
            match parsed_field:
                case "@method":
                    http_signature.with_field(parsed_field, method.upper())
                case "@path":
                    parsed_url = urlparse(url)
                    path = parsed_url.path
                    http_signature.with_field(parsed_field, path)
                case "@authority":
                    http_signature.with_field(parsed_field, headers["host"])
                case _:
                    try:
                        http_signature.with_field(parsed_field, headers[parsed_field])
                    except Exception as error:
                        logger.exception(error)

        http_signature.with_field(
            "@signature-params", parsed_signature.signature_params
        )

        return http_signature

    async def validate_signature_request(self, request) -> str | None:
        """Validates a given signature

        :param request: The request object"""
        return await self.validate_signature(
            request.method, request.url, request.headers, request.get_data
        )

    def validate_digest(self, headers: dict, body: bytes) -> bool:
        if isinstance(body, str):
            warnings.warn("Got body of type str expected bytes")
            body = body.encode("utf-8")

        return validate_digest(headers, body)
