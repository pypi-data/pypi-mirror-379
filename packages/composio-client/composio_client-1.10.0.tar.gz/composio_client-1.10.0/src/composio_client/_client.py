# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Dict, Mapping, cast
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    cli,
    link,
    files,
    tools,
    toolkits,
    migration,
    tool_router,
    auth_configs,
    triggers_types,
    connected_accounts,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.mcp import mcp
from .resources.trigger_instances import trigger_instances

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Composio",
    "AsyncComposio",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://backend.composio.dev",
    "staging": "https://staging-backend.composio.dev",
    "local": "http://localhost:9900",
}


class Composio(SyncAPIClient):
    auth_configs: auth_configs.AuthConfigsResource
    connected_accounts: connected_accounts.ConnectedAccountsResource
    link: link.LinkResource
    toolkits: toolkits.ToolkitsResource
    tools: tools.ToolsResource
    trigger_instances: trigger_instances.TriggerInstancesResource
    triggers_types: triggers_types.TriggersTypesResource
    mcp: mcp.McpResource
    files: files.FilesResource
    migration: migration.MigrationResource
    cli: cli.CliResource
    tool_router: tool_router.ToolRouterResource
    with_raw_response: ComposioWithRawResponse
    with_streaming_response: ComposioWithStreamedResponse

    # client options
    api_key: str | None

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Composio client instance.

        This automatically infers the `api_key` argument from the `COMPOSIO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COMPOSIO_API_KEY")
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("COMPOSIO_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `COMPOSIO_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.auth_configs = auth_configs.AuthConfigsResource(self)
        self.connected_accounts = connected_accounts.ConnectedAccountsResource(self)
        self.link = link.LinkResource(self)
        self.toolkits = toolkits.ToolkitsResource(self)
        self.tools = tools.ToolsResource(self)
        self.trigger_instances = trigger_instances.TriggerInstancesResource(self)
        self.triggers_types = triggers_types.TriggersTypesResource(self)
        self.mcp = mcp.McpResource(self)
        self.files = files.FilesResource(self)
        self.migration = migration.MigrationResource(self)
        self.cli = cli.CliResource(self)
        self.tool_router = tool_router.ToolRouterResource(self)
        self.with_raw_response = ComposioWithRawResponse(self)
        self.with_streaming_response = ComposioWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncComposio(AsyncAPIClient):
    auth_configs: auth_configs.AsyncAuthConfigsResource
    connected_accounts: connected_accounts.AsyncConnectedAccountsResource
    link: link.AsyncLinkResource
    toolkits: toolkits.AsyncToolkitsResource
    tools: tools.AsyncToolsResource
    trigger_instances: trigger_instances.AsyncTriggerInstancesResource
    triggers_types: triggers_types.AsyncTriggersTypesResource
    mcp: mcp.AsyncMcpResource
    files: files.AsyncFilesResource
    migration: migration.AsyncMigrationResource
    cli: cli.AsyncCliResource
    tool_router: tool_router.AsyncToolRouterResource
    with_raw_response: AsyncComposioWithRawResponse
    with_streaming_response: AsyncComposioWithStreamedResponse

    # client options
    api_key: str | None

    _environment: Literal["production", "staging", "local"] | NotGiven

    def __init__(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | NotGiven = not_given,
        base_url: str | httpx.URL | None | NotGiven = not_given,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncComposio client instance.

        This automatically infers the `api_key` argument from the `COMPOSIO_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COMPOSIO_API_KEY")
        self.api_key = api_key

        self._environment = environment

        base_url_env = os.environ.get("COMPOSIO_BASE_URL")
        if is_given(base_url) and base_url is not None:
            # cast required because mypy doesn't understand the type narrowing
            base_url = cast("str | httpx.URL", base_url)  # pyright: ignore[reportUnnecessaryCast]
        elif is_given(environment):
            if base_url_env and base_url is not None:
                raise ValueError(
                    "Ambiguous URL; The `COMPOSIO_BASE_URL` env var and the `environment` argument are given. If you want to use the environment, you must pass base_url=None",
                )

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc
        elif base_url_env is not None:
            base_url = base_url_env
        else:
            self._environment = environment = "production"

            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.auth_configs = auth_configs.AsyncAuthConfigsResource(self)
        self.connected_accounts = connected_accounts.AsyncConnectedAccountsResource(self)
        self.link = link.AsyncLinkResource(self)
        self.toolkits = toolkits.AsyncToolkitsResource(self)
        self.tools = tools.AsyncToolsResource(self)
        self.trigger_instances = trigger_instances.AsyncTriggerInstancesResource(self)
        self.triggers_types = triggers_types.AsyncTriggersTypesResource(self)
        self.mcp = mcp.AsyncMcpResource(self)
        self.files = files.AsyncFilesResource(self)
        self.migration = migration.AsyncMigrationResource(self)
        self.cli = cli.AsyncCliResource(self)
        self.tool_router = tool_router.AsyncToolRouterResource(self)
        self.with_raw_response = AsyncComposioWithRawResponse(self)
        self.with_streaming_response = AsyncComposioWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "staging", "local"] | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            environment=environment or self._environment,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ComposioWithRawResponse:
    def __init__(self, client: Composio) -> None:
        self.auth_configs = auth_configs.AuthConfigsResourceWithRawResponse(client.auth_configs)
        self.connected_accounts = connected_accounts.ConnectedAccountsResourceWithRawResponse(client.connected_accounts)
        self.link = link.LinkResourceWithRawResponse(client.link)
        self.toolkits = toolkits.ToolkitsResourceWithRawResponse(client.toolkits)
        self.tools = tools.ToolsResourceWithRawResponse(client.tools)
        self.trigger_instances = trigger_instances.TriggerInstancesResourceWithRawResponse(client.trigger_instances)
        self.triggers_types = triggers_types.TriggersTypesResourceWithRawResponse(client.triggers_types)
        self.mcp = mcp.McpResourceWithRawResponse(client.mcp)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.migration = migration.MigrationResourceWithRawResponse(client.migration)
        self.cli = cli.CliResourceWithRawResponse(client.cli)
        self.tool_router = tool_router.ToolRouterResourceWithRawResponse(client.tool_router)


class AsyncComposioWithRawResponse:
    def __init__(self, client: AsyncComposio) -> None:
        self.auth_configs = auth_configs.AsyncAuthConfigsResourceWithRawResponse(client.auth_configs)
        self.connected_accounts = connected_accounts.AsyncConnectedAccountsResourceWithRawResponse(
            client.connected_accounts
        )
        self.link = link.AsyncLinkResourceWithRawResponse(client.link)
        self.toolkits = toolkits.AsyncToolkitsResourceWithRawResponse(client.toolkits)
        self.tools = tools.AsyncToolsResourceWithRawResponse(client.tools)
        self.trigger_instances = trigger_instances.AsyncTriggerInstancesResourceWithRawResponse(
            client.trigger_instances
        )
        self.triggers_types = triggers_types.AsyncTriggersTypesResourceWithRawResponse(client.triggers_types)
        self.mcp = mcp.AsyncMcpResourceWithRawResponse(client.mcp)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.migration = migration.AsyncMigrationResourceWithRawResponse(client.migration)
        self.cli = cli.AsyncCliResourceWithRawResponse(client.cli)
        self.tool_router = tool_router.AsyncToolRouterResourceWithRawResponse(client.tool_router)


class ComposioWithStreamedResponse:
    def __init__(self, client: Composio) -> None:
        self.auth_configs = auth_configs.AuthConfigsResourceWithStreamingResponse(client.auth_configs)
        self.connected_accounts = connected_accounts.ConnectedAccountsResourceWithStreamingResponse(
            client.connected_accounts
        )
        self.link = link.LinkResourceWithStreamingResponse(client.link)
        self.toolkits = toolkits.ToolkitsResourceWithStreamingResponse(client.toolkits)
        self.tools = tools.ToolsResourceWithStreamingResponse(client.tools)
        self.trigger_instances = trigger_instances.TriggerInstancesResourceWithStreamingResponse(
            client.trigger_instances
        )
        self.triggers_types = triggers_types.TriggersTypesResourceWithStreamingResponse(client.triggers_types)
        self.mcp = mcp.McpResourceWithStreamingResponse(client.mcp)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.migration = migration.MigrationResourceWithStreamingResponse(client.migration)
        self.cli = cli.CliResourceWithStreamingResponse(client.cli)
        self.tool_router = tool_router.ToolRouterResourceWithStreamingResponse(client.tool_router)


class AsyncComposioWithStreamedResponse:
    def __init__(self, client: AsyncComposio) -> None:
        self.auth_configs = auth_configs.AsyncAuthConfigsResourceWithStreamingResponse(client.auth_configs)
        self.connected_accounts = connected_accounts.AsyncConnectedAccountsResourceWithStreamingResponse(
            client.connected_accounts
        )
        self.link = link.AsyncLinkResourceWithStreamingResponse(client.link)
        self.toolkits = toolkits.AsyncToolkitsResourceWithStreamingResponse(client.toolkits)
        self.tools = tools.AsyncToolsResourceWithStreamingResponse(client.tools)
        self.trigger_instances = trigger_instances.AsyncTriggerInstancesResourceWithStreamingResponse(
            client.trigger_instances
        )
        self.triggers_types = triggers_types.AsyncTriggersTypesResourceWithStreamingResponse(client.triggers_types)
        self.mcp = mcp.AsyncMcpResourceWithStreamingResponse(client.mcp)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.migration = migration.AsyncMigrationResourceWithStreamingResponse(client.migration)
        self.cli = cli.AsyncCliResourceWithStreamingResponse(client.cli)
        self.tool_router = tool_router.AsyncToolRouterResourceWithStreamingResponse(client.tool_router)


Client = Composio

AsyncClient = AsyncComposio
