<!--
SPDX-FileCopyrightText: 2023-2025 Helge

SPDX-License-Identifier: MIT
-->

# Changes to Bovine

## bovine 0.5.19 ([Milestone](https://codeberg.org/bovine/bovine/milestone/9771))

- use key_id argument [bovine#303](https://codeberg.org/bovine/bovine/issues/303)
- improve jrd models [bovine#277](https://codeberg.org/bovine/bovine/issues/277)
- repair data uri [bovine#276](https://codeberg.org/bovine/bovine/issues/276)
- replace bleach with nh3 [bovine#272](https://codeberg.org/bovine/bovine/issues/272)

## bovine 0.5.18 ([Milestone](https://codeberg.org/bovine/bovine/milestone/9699))

- convert `ObjectFactory` into a dataclass.
- Enable setting actor in `ObjectFactory` and using it to create mention. This resolves [bovine#241](https://codeberg.org/bovine/bovine/issues/241)
- Update to use Controlled Identifiers [bovine#261](https://codeberg.org/bovine/bovine/issues/261)

## bovine 0.5.17 ([Milestone](https://codeberg.org/bovine/bovine/milestone/9695))

- Means to create PropertyValue objects [bovine#262](https://codeberg.org/bovine/bovine/issues/262)
- Add content to example usage of `bovine.activitystreams.object_factory.ObjectFactory.reply` [bovine#255](https://codeberg.org/bovine/bovine/issues/255)
- Add `bovine.activitystreams.media.create_image_inline`, inlining the image [bovine#257](https://codeberg.org/bovine/bovine/issues/257)

## bovine 0.5.16 ([Milestone](https://codeberg.org/bovine/bovine/milestone/9694))

- Add `bovine.activitystreams.utils.uris_for_public`, [bovine#253](https://codeberg.org/bovine/bovine/issues/253)

## bovine 0.5.15

- Allow string as argument for `ActivityFactory.undo` [bovine#251](https://codeberg.org/bovine/bovine/issues/251)
- Add examples for JrdLink, JrdData [bovine#247](https://codeberg.org/bovine/bovine/issues/247)
- Add NodeInfo object [bovine#248](https://codeberg.org/bovine/bovine/issues/248)
- Add feature tests for things obeying schemas
- Add `bovine.activitystreams.media`
- Use [fediverse-features](https://pypi.org/project/fediverse-features/) to manage BDD tests
- Add `bovine.crypto.digest.digest_multibase`.

## bovine 0.5.14

- Document `bovine.activitystreams.utils.property_for_key_as_set` and ensure reply works if to or cc is string [bovine#243](https://codeberg.org/bovine/bovine/issues/243)
- Improve the server in `bovine.testing`. In particular, new README.md and a cow as icon [bovine#242](https://codeberg.org/bovine/bovine/issues/242)
- Add `create_tombstone` to `BovineActor.get` resolving [bovine#236](https://codeberg.org/bovine/bovine/issues/236)
- Add `ActivityFactory.block`. [bovine#237](https://codeberg.org/bovine/bovine/issues/237)
- Add `bovine.utils.webfinger_response`. [bovine#238](https://codeberg.org/bovine/bovine/issues/238)
- Remove validation on URLs to be compatible with pydantic 2.10
- Ensured update activities also have followers set. [bovine#234](https://codeberg.org/bovine/bovine/issues/234)

## bovine 0.5.13

- Adapted documentation to use CryptographicIdentifier.fromPublicKey instead of deprecated tuple [bovine#198](https://codeberg.org/bovine/bovine/issues/198)
- Added bovine.crypto.digest to separate the digest checks. [cattle_grid#20](https://codeberg.org/bovine/cattle_grid/issues/20)
- Ability to use SHA-256 [bovine#227](https://codeberg.org/bovine/bovine/issues/227)
- Ability to skip digest checks. [bovine#224](https://codeberg.org/bovine/bovine/issues/224)

## bovine 0.5.12

- Add testing module [Issue 219](https://codeberg.org/bovine/bovine/issues/219)
- Add new tutorial on using fediverse-pasture [Issue 208](https://codeberg.org/bovine/bovine/issues/208)
- Use urllib to parse did:keys, [Issue 196](https://codeberg.org/bovine/bovine/issues/196)
- Add support for checking [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421.html) signatures, [Pull request 218](https://codeberg.org/bovine/bovine/pulls/218)
- Add support for (created), (expires) in http signature [Issue 217](https://codeberg.org/bovine/bovine/issues/217)
- Repair server tutorial [Issue 207](https://codeberg.org/bovine/bovine/issues/207)
- `OrderedCollection` now doesn't have `totalItems` set by default, but updated when `items` is set. [Issue 205](https://codeberg.org/bovine/bovine/issues/205)
- Add `ActivityFactory.custom`. [Issue 203](https://codeberg.org/bovine/bovine/issues/203)
- Improved `BovineActor` and `BovineClient`. Added doctests. [Issue 202](https://codeberg.org/bovine/bovine/issues/202)

## bovine 0.5.11

- `actor` is now populated from actor information not the object. [Issue 199](https://codeberg.org/bovine/bovine/issues/199)
- `published` is now set by default on activities and objects. [Issue 190](https://codeberg.org/bovine/bovine/issues/190)

## bovine 0.5.10

- `bovine.activitystreams.Actor` can now contain `assertionMethods`. [Issue 151](https://codeberg.org/bovine/bovine/issues/151)
- Started using DocTests
- Allow `properties` in `bovine.activitystreams.Actor` to add a lot of properties. [Issue 150](https://codeberg.org/bovine/bovine/issues/150)

## bovine 0.5.9

- Support RFC 9530 by allowing the `digest_method` to be set in actor. Furthermore, one may replace `digest` with `content-digest` and bovine will still consider the requests valid.
- Embedded objects of type `DataIntegrity` can now have their own context [Issue 180](https://codeberg.org/bovine/bovine/issues/180)

## bovine 0.5.8

- Add containers
- Begin work on [Issue 151](https://codeberg.org/bovine/bovine/issues/151).

## bovine 0.5.7

- `bovine.parse.Actor.cryptographic_identiers` now also extracts Multikeys [Issue 112](https://codeberg.org/bovine/bovine/issues/112)
- Replace `request-cache` with own `bovine.jsonld.cache` [Issue 48](https://codeberg.org/bovine/bovine/issues/48)
- `JrdData` and `JrdLink` are now members of `bovine.models` and generated. [Issue 145](https://codeberg.org/bovine/bovine/issues/145)
- Better debug logging for `BovineActor.get` and `BovineActor.post`. [Issue 143](https://codeberg.org/bovine/bovine/issues/143)
- Finish all the stuff related to Verifiable Credentials [Issue 132](https://codeberg.org/bovine/bovine/issues/132)
- Add reuse headers [Issue 133](https://codeberg.org/bovine/bovine/issues/133)

## bovine 0.5.6

- Request headers can now be properly set in clients [Issue 136](https://codeberg.org/bovine/bovine/issues/136)

## bovine 0.5.5

- `bovine.utils.date` absorbed into `bovine.utils` and documented
- New method `CryptographicIdentifier.from_did_key`
- `object_factory.reply` now works if attributedTo is a dictionary, see [Pull Request 123](https://codeberg.org/bovine/bovine/pulls/123)

## bovine 0.5.4

- Add implementation for FEP-8b32, see [Issue 7](https://codeberg.org/bovine/bovine/issues/7)
- Add deprecation warnings for bovine 0.6.0
- Add `bovine.types.CryptographicSecret` and `bovine.types.CryptographicIdentifier` and start using them.

## bovine 0.5.3

- Begin implementing support for Multikey.
- Python 3.12 should now be supported.
- Add support for [FEP-e232](https://codeberg.org/fediverse/fep/src/branch/main/fep/e232/fep-e232.md), [Issue 91](https://codeberg.org/bovine/bovine/issues/91)

## Version 0.5.2

- Add ability to follow links to parse json-ld [Issue 80](https://codeberg.org/bovine/bovine/issues/80)
- replaces multiformats with based58 see [Issue 85](https://codeberg.org/bovine/bovine/issues/85)
- `parse_fediverse_handle` can now handles uris starting with `acct:`, [Issue 84](https://codeberg.org/bovine/bovine/issues/84)

## Version 0.5.1

- `BovineActor.get` returns a Tombstone for 404 and 410 errors
- `Object` now supports icon and mediaType
- Add `bovine.clients.web`
- Add `bovine.utils.JrdData` and `.JrdLink`

## Version 0.4.0

- Changed signatures of `BovineClient` and `BovineActor` to take keyword arguments
- Document internals of `bovine.crypto`
- Add `bovine.parse`
- `BovineClient.proxy_element` renamed to just `proxy`
- `activity_factory` now has a method to create `Undo` activities
- `activity_factory` now sets `to` to the actor of a follow request for `accept`, `reject`
- Make dev, test, doc dependencies optional
- Add `bovine.crypto.build_validate_http_signature_raw`

## Version 0.3.1

- BovineClient.inbox / outbox are no longer coroutines
- BovineActor improved getting of resources
- Environment flag `BUTCHER_ALLOW_HTTP` that enables usage of http for webfinger lookup in BovineClient creation

## Version 0.3.0

- Force "items" to a `@container` of type `@set` in the `about:bovine` context
- Repair to CollectionHelper. Add collection_helper to BovineClient.

## Version 0.2.6

- Signature of `webfinger_response_json` changed (__breaking__)
- Improve addressing of object and activities. Add `as_followers` method.
- ServerSentEvent.id is now a str (was int)
- Improved CollectionHelper to be able iterate over Collection and OrderedCollection type of ActivityStreams objects.

## Version 0.2.3

- Improved REPL functionality

## Version 0.2.2

- Add command `python -mbovine.repl`.

## Version 0.2.1

- Repair jsonld request resolver

## Version 0.2.0

- Support [fep-4adb](https://codeberg.org/fediverse/fep/src/branch/main/feps/fep-4adb.md)
- Add jsonld functionality

## Version 0.1.4

- Bugfix: ObjectFactor.actor_for_mention didn't proxy the requested actor_id.

## Version 0.1.3

- Tutorial on hashtag announce bot
- Implement fep-612d
- Make `validate_moo_auth_signature` also return the domain
- Document how to get the activity id from location header after send_to_outbox

## Version 0.1.2

- Add reject to activity_factory
- Add url property to Actor
- Add python -m bovine.msg and python -m bovine.ed25519_key features

## Version 0.1.1

- Improved tutorial

## Version 0.1.0

- 2023-04-13 Added bovine.crypto module with all crypto routines, previously in bovine. Added documentation, added test cases for http signatures
- 2023-04-11 Added attachment, width, height to Object
- 2023-04-10 Activities and Objects should no longer contain empty to, cc properties
- 2023-04-09 Include sphinx.ext.viewcode in documentation

## Version 0.0.13

- 2023-04-08: Add ability to create Mention based on actor uri
- 2023-04-08: Add documentation for bovine.activitystreams.utils
- 2023-04-02: EventSource no longer returns ServerSentEvent with empty data
