# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "AuthConfigUpdateParams",
    "Variant0",
    "Variant0Credentials",
    "Variant0ProxyConfig",
    "Variant0ToolAccessConfig",
    "Variant1",
    "Variant1ToolAccessConfig",
]


class Variant0(TypedDict, total=False):
    credentials: Required[Variant0Credentials]

    type: Required[Literal["custom"]]

    proxy_config: Variant0ProxyConfig

    tool_access_config: Variant0ToolAccessConfig


class Variant0Credentials(TypedDict, total=False):
    scopes: Union[str, SequenceNotStr[str]]

    user_scopes: Union[str, SequenceNotStr[str]]


class Variant0ProxyConfig(TypedDict, total=False):
    proxy_url: Required[str]
    """The url of the auth proxy"""

    proxy_auth_key: str
    """The auth key for the auth proxy"""


class Variant0ToolAccessConfig(TypedDict, total=False):
    tools_available_for_execution: SequenceNotStr[str]
    """The actions that the user can perform on the auth config.

    If passed, this will update the actions that the user can perform on the auth
    config.
    """

    tools_for_connected_account_creation: SequenceNotStr[str]
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


class Variant1(TypedDict, total=False):
    type: Required[Literal["default"]]

    scopes: Union[str, SequenceNotStr[str]]

    tool_access_config: Variant1ToolAccessConfig


class Variant1ToolAccessConfig(TypedDict, total=False):
    tools_available_for_execution: SequenceNotStr[str]
    """The actions that the user can perform on the auth config.

    If passed, this will update the actions that the user can perform on the auth
    config.
    """

    tools_for_connected_account_creation: SequenceNotStr[str]
    """
    Tools used to generate the minimum required scopes for the auth config (only
    valid for OAuth). If passed, this will update the scopes.
    """


AuthConfigUpdateParams: TypeAlias = Union[Variant0, Variant1]
