from typing import Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class JrdLink(BaseModel):
    """
    See [RFC 7033](https://www.rfc-editor.org/rfc/rfc7033.html).

    ```pycon
    >>> JrdLink(rel="self", href="http://test.example/actor").model_dump(exclude_none=True)
    {'rel': 'self', 'href': 'http://test.example/actor'}

    ```
    """

    model_config = ConfigDict(
        extra="allow",
    )
    rel: str | None = Field(default=None, examples=["self"], description="rel")
    type: str | None = Field(default=None, examples=["application/activity+json"])
    href: str | None = Field(
        default=None,
        examples=["http://test.example/actor"],
        description="""
    when used with the 'href' attribute, conveys a link relation between the host described by the document and a common target URI
    """,
    )
    titles: dict[str, Any] | None = Field(
        default=None,
        description="titles",
    )
    properties: dict[str, Any] | None = Field(
        default=None,
        description="properties",
    )
    template: str | None = Field(
        default=None,
        description="template attribute conveys a relation whose context is an individual resource within the host-meta document scope,",
    )


class JrdData(BaseModel):
    """
    See [RFC 6415](https://www.packetizer.com/rfc/rfc6415/)

    ```pycon
    >>> JrdData(subject="acct:actor@test.example").model_dump(exclude_none=True)
    {'subject': 'acct:actor@test.example'}

    ```
    """

    model_config = ConfigDict(
        extra="allow",
    )
    subject: str | None = Field(None, examples=["acct:actor@test.example"])
    expires: datetime | None = Field(
        default=None,
        description="expiration date time",
    )
    aliases: list[str] | None = Field(
        default=None,
        description="value a string array containing the values of each element in order",
    )
    properties: dict[str, Any] | None = Field(
        default=None,
        description="value an object with each element included as a name/value pair with the value of the type attribute as name, and element value included as a string value.",
    )
    links: list[JrdLink] | None = Field(
        default=None,
        description="a single name/value pair with the name 'links', and value an array with each element included as an object",
    )
