"""
This module provides routines to create PropertyValue objects
as used by [Mastodon](https://docs.joinmastodon.org/spec/activitypub/#schema).
We try to implement json-ld as we understand it.

We use PropertyValue as defined by schema.org [here](https://schema.org/PropertyValue).
"""

property_value_context = {
    "PropertyValue": {
        "@id": "https://schema.org/PropertyValue",
        "@context": {
            "value": "https://schema.org/value",
            "name": "https://schema.org/name",
        },
    }
}
"""If using PropertyValue object, include this in `@context`"""


def from_key_value(key, value):
    """Creates a PropertyValue object from a key and a value

    ```pycon
    >>> from_key_value("name", "Alice")
    {'type': 'PropertyValue', 'name': 'name', 'value': 'Alice'}

    ```
    """

    return {
        "type": "PropertyValue",
        "name": key,
        "value": value,
    }


def from_dictionary(values: dict) -> list[dict]:
    """Creates a list of PropertyValue objects from a dictionary

    ```pycon
    >>> from_dictionary({"name": "Alice", "job": "Sending secret messages"})
    [{'type': 'PropertyValue', 'name': 'name', 'value': 'Alice'},
    {'type': 'PropertyValue', 'name': 'job', 'value': 'Sending secret messages'}]

    ```
    """

    return [from_key_value(key, value) for key, value in values.items()]


def dictionary_to_actor_attachment(values: dict) -> dict:
    """Creates a stub actor with the property values corresponding
    to `values` as attachment

    ```pycon
    >>> dictionary_to_actor_attachment({"name": "Alice"})
    {'@context': ['https://www.w3.org/ns/activitystreams',
        {'PropertyValue': {'@id': 'https://schema.org/PropertyValue',
            '@context': {'value': 'https://schema.org/value',
                'name': 'https://schema.org/name'}}}],
        'attachment': [{'type': 'PropertyValue',
            'name': 'name',
            'value': 'Alice'}]}

    ```

    """
    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            property_value_context,
        ],
        "attachment": from_dictionary(values),
    }
