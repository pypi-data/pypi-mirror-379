# SPDX-FileCopyrightText: 2023 Helge
# SPDX-FileCopyrightText: 2024 helge
#
# SPDX-License-Identifier: MIT

import base64
import hashlib
import logging
import warnings
import jcs
from pyld import jsonld
from typing import Tuple, Union
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, padding, rsa, ec
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key,
)
import based58
from http_sf import ser
from urllib.parse import urlunsplit, urlsplit


from bovine.models import DataIntegrityProof
from bovine.utils import pydantic_to_json
from .multibase import (
    multibase_decode,
    encode_public_key_to_multibase,
    decode_multibase_public_key,
    MultiCodec,
)

logger = logging.getLogger(__name__)


def content_digest_sha256(content: str | bytes, prefix: str = "sha-256") -> str:
    """Computes the SHA256 digest of given content

    ```pycon
    >>> content_digest_sha256(b"moo")
    'sha-256=R9+ukoir89XSJSq/sL1qyWYmN9ZG5t+dXSdLwzbierw='

    >>> content_digest_sha256(b"moo", prefix="SHA-256")
    'SHA-256=R9+ukoir89XSJSq/sL1qyWYmN9ZG5t+dXSdLwzbierw='

    ```

    :param content: Content to be encoded
    :param prefix: Prefix to use should be either "SHA-256" or "sha-256" depending on taste
    """
    if isinstance(content, str):
        content = content.encode("utf-8")

    digest = base64.standard_b64encode(hashlib.sha256(content).digest()).decode("utf-8")
    return "=".join([prefix, digest])


def content_digest_sha256_rfc_9530(content: bytes) -> Tuple[str, str]:
    """Computes the content digest according to [RFC 9530](https://www.rfc-editor.org/authors/rfc9530.html)

    ```pycon
    >>> content_digest_sha256_rfc_9530(b'{"hello": "world"}\\n')
    ('content-digest', 'sha-256=:RK/0qy18MlBSVnWgjwz6lZEWjP/lF5HF9bvEF8FabDg=:')

    ```

    :param content: Usually the request body to compute the digest from
    :return: Tuple of header name, header value"""
    return "content-digest", ser({"sha-256": hashlib.sha256(content).digest()})


def sign_message(private_key, message):
    warnings.warn("Deprecated will be removed with bovine 0.6.0", DeprecationWarning)
    try:
        key = load_pem_private_key(private_key.encode("utf-8"), password=None)
        assert isinstance(key, rsa.RSAPrivateKey)
    except Exception as e:
        logger.error(e)
        logger.error(private_key)
        raise (e)

    return base64.standard_b64encode(
        key.sign(
            message.encode("utf-8"),
            padding.PKCS1v15(),
            hashes.SHA256(),
        )
    ).decode("utf-8")


def verify_signature(public_key, message, signature):
    public_key_loaded = load_pem_public_key(public_key.encode("utf-8"))

    assert isinstance(public_key_loaded, rsa.RSAPublicKey)

    try:
        public_key_loaded.verify(
            base64.standard_b64decode(signature),
            message.encode("utf-8"),
            padding.PKCS1v15(),
            hashes.SHA256(),
        )
    except InvalidSignature:
        logger.warning("invalid signature")
        return False

    return True


def public_key_to_did_key(
    public_key: Union[
        ed25519.Ed25519PublicKey, rsa.RSAPublicKey, ec.EllipticCurvePublicKey
    ],
) -> str:
    """Converts a public key to a [did:key](https://w3c-ccg.github.io/did-method-key/).

    :param public_key: The public key
    """
    return urlunsplit(
        ("did", "", "key:" + encode_public_key_to_multibase(public_key), "", "")
    )


def private_key_to_base58(private_key: ed25519.Ed25519PrivateKey) -> str:
    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption(),
    )
    encoded = based58.b58encode(MultiCodec.Ed25519Private.value + private_bytes)
    return "z" + encoded.decode("ascii")


def did_key_to_public_key(did: str) -> ed25519.Ed25519PublicKey:
    """Transform a did key to a public key

    ```pycon
    >>> did = "did:key:z6MkekwC6R9bj9ErToB7AiZJfyCSDhaZe1UxhDbCqJrhqpS5"
    >>> did_key_to_public_key(did)
    <cryptography.hazmat.bindings._rust.openssl.ed25519.Ed25519PublicKey object at ...>

    ```
    """
    scheme, _, path, _, _ = urlsplit(did)
    if scheme != "did":
        raise ValueError(f"Scheme should be did, got {scheme}, for {did}")
    if not path.startswith("key:"):
        raise ValueError(f"Path should start with key:, got {path}, for {did}")
    return decode_multibase_public_key(path[4:])


def jcs_sha256(doc: dict, context: dict | None = None) -> bytes:
    """Returns the sha256 digest of the representation
    of dict according to JCS. This assumes that `doc`
    is JSON serializable.

    JCS is defined in [RFC8785](https://www.rfc-editor.org/rfc/rfc8785).

    :param doc: The document
    :param context: ignored used in [rdfc_sha256][bovine.crypto.helper.rdfc_sha256]
    """
    return hashlib.sha256(jcs.canonicalize(doc)).digest()


def rdfc_sha256(doc: dict, context: dict = {}) -> bytes:
    """Returns the sha256 digest of the representation
    of dict according to [RDF-Canon](https://www.w3.org/TR/rdf-canon/)

    The algorithm used is URDNA2015 and the result are n-quads.

    :param doc: The document
    :param context: If doc has no `@context` property, it is set to this parameter
    """
    if "@context" not in doc:
        doc["@context"] = context

    normalized = jsonld.normalize(
        doc, {"algorithm": "URDNA2015", "format": "application/n-quads"}
    )
    return hashlib.sha256(normalized.encode("utf-8")).digest()


def jcs_sha384(doc: dict, context: dict | None = None) -> bytes:
    """Returns the sha384 digest of the representation
    of dict according to JCS. This assumes that `doc`
    is JSON serializable.

    JCS is defined in [RFC8785](https://www.rfc-editor.org/rfc/rfc8785).

    :param doc: The document
    :param context: ignored used in [rdfc_sha256][bovine.crypto.helper.rdfc_sha256]
    """
    return hashlib.sha384(jcs.canonicalize(doc)).digest()


def rdfc_sha384(doc: dict, context: dict = {}) -> bytes:
    """Returns the sha384 digest of the representation
    of dict according to [RDF-Canon](https://www.w3.org/TR/rdf-canon/)

    The algorithm used is URDNA2015 and the result are n-quads.

    :param doc: The document
    :param context: If doc has no `@context` property, it is set to this parameter
    """
    if "@context" not in doc:
        doc["@context"] = context

    normalized = jsonld.normalize(
        doc, {"algorithm": "URDNA2015", "format": "application/n-quads"}
    )
    logger.debug(normalized)
    return hashlib.sha384(normalized.encode("utf-8")).digest()


def ensure_data_integrity_context(doc: dict) -> dict:
    """Performs context injection according to
    [Verifiable Credentials: Data Integrity](https://w3c.github.io/vc-data-integrity/#context-injection). The data integrity
    context being added is `https://w3id.org/security/data-integrity/v2`.

    :param doc: Document
    :return: The same document with the data integrity context added.
    """
    integrity_context = "https://w3id.org/security/data-integrity/v2"
    alternate_context = "https://w3id.org/security/data-integrity/v1"
    context = doc.get("@context")
    if context is None:
        return {"@context": integrity_context, **doc}
    if isinstance(context, str):
        context: list = [context]
    if integrity_context in context or alternate_context in context:
        return doc
    return jsonld.compact(doc, context + [integrity_context])


def split_according_to_fep8b32(doc: dict) -> Tuple[dict, DataIntegrityProof, bytes]:
    pure_doc = {key: value for key, value in doc.items() if key != "proof"}
    proof_document = DataIntegrityProof.model_validate(doc["proof"])
    signature = multibase_decode(doc["proof"]["proofValue"])

    return pure_doc, proof_document, signature


def integrity_proof_to_pure_proof_dict(proof: DataIntegrityProof) -> dict:
    return {
        key: value
        for key, value in pydantic_to_json(proof).items()
        if key != "proofValue"
    }


def curve_to_hashing_algorithm_and_half_key_length(curve):
    if isinstance(curve, ec.SECP256R1):
        return ec.ECDSA(hashes.SHA256()), 32
    else:
        return ec.ECDSA(hashes.SHA384()), 48


def pem_private_key_to_pem_public_key(private_key):
    laoded_key = load_pem_private_key(private_key.encode("utf-8"), password=None)
    return (
        laoded_key.public_key()
        .public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        .decode()
    )
