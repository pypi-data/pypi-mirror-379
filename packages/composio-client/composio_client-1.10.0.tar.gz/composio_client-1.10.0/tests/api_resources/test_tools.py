# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    ToolListResponse,
    ToolProxyResponse,
    ToolExecuteResponse,
    ToolGetInputResponse,
    ToolRetrieveResponse,
    ToolRetrieveEnumResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        tool = client.tools.retrieve(
            tool_slug="tool_slug",
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Composio) -> None:
        tool = client.tools.retrieve(
            tool_slug="tool_slug",
            toolkit_versions="string",
            version="version",
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.tools.with_raw_response.retrieve(
            tool_slug="tool_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.tools.with_streaming_response.retrieve(
            tool_slug="tool_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_slug` but received ''"):
            client.tools.with_raw_response.retrieve(
                tool_slug="",
            )

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_method_list(self, client: Composio) -> None:
        tool = client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        tool = client.tools.list(
            auth_config_ids=["string"],
            cursor="cursor",
            important="true",
            include_deprecated=True,
            limit=0,
            scopes=["string"],
            search="search",
            tags=["string"],
            tool_slugs="tool_slugs",
            toolkit_slug="toolkit_slug",
            toolkit_versions="string",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_execute(self, client: Composio) -> None:
        tool = client.tools.execute(
            tool_slug="tool_slug",
        )
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Composio) -> None:
        tool = client.tools.execute(
            tool_slug="tool_slug",
            allow_tracing=False,
            arguments={
                "repository": "bar",
                "workflow_id": "bar",
                "ref": "bar",
                "inputs": "bar",
            },
            connected_account_id="ca_1a2b3c4d5e6f",
            custom_auth_params={
                "base_url": "https://api.example.com",
                "body": {"foo": "bar"},
                "parameters": [
                    {
                        "in": "header",
                        "name": "x-api-key",
                        "value": "secret-key",
                    }
                ],
            },
            custom_connection_data={
                "auth_scheme": "OAUTH2",
                "toolkit_slug": "github",
                "val": {
                    "access_token": "secret-token",
                    "account_id": "account_id",
                    "account_url": "account_url",
                    "api_url": "api_url",
                    "authed_user": {
                        "access_token": "access_token",
                        "scope": "scope",
                    },
                    "base_url": "base_url",
                    "borneo_dashboard_url": "borneo_dashboard_url",
                    "companydomain": "COMPANYDOMAIN",
                    "dc": "dc",
                    "domain": "domain",
                    "expires_in": 0,
                    "extension": "extension",
                    "form_api_base_url": "form_api_base_url",
                    "id_token": "id_token",
                    "instance_endpoint": "instanceEndpoint",
                    "instance_name": "instanceName",
                    "long_redirect_url": True,
                    "proxy_password": "proxy_password",
                    "proxy_username": "proxy_username",
                    "refresh_token": "refresh_token",
                    "region": "region",
                    "scope": "string",
                    "server_location": "server_location",
                    "shop": "shop",
                    "site_name": "site_name",
                    "state_prefix": "state_prefix",
                    "subdomain": "subdomain",
                    "token_type": "token_type",
                    "version": "version",
                    "webhook_signature": "webhook_signature",
                    "your_server": "your_server",
                    "your_domain": "your-domain",
                },
            },
            text="Trigger the main workflow in the octocat/Hello-World repository on the main branch for the production environment",
            user_id="user-123",
            version="latest",
        )
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Composio) -> None:
        response = client.tools.with_raw_response.execute(
            tool_slug="tool_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Composio) -> None:
        with client.tools.with_streaming_response.execute(
            tool_slug="tool_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolExecuteResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_execute(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_slug` but received ''"):
            client.tools.with_raw_response.execute(
                tool_slug="",
            )

    @parametrize
    def test_method_get_input(self, client: Composio) -> None:
        tool = client.tools.get_input(
            tool_slug="tool_slug",
            text="I need to trigger the main workflow in the octocat/Hello-World repository to deploy to production",
        )
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    def test_method_get_input_with_all_params(self, client: Composio) -> None:
        tool = client.tools.get_input(
            tool_slug="tool_slug",
            text="I need to trigger the main workflow in the octocat/Hello-World repository to deploy to production",
            custom_description="This tool triggers GitHub Actions workflows in a repository. It requires the repository name, workflow ID, and optional input parameters.",
            system_prompt="You are an expert assistant that generates precise GitHub Actions workflow parameters. Extract exact repository names, workflow IDs, and input values from user descriptions.",
            version="latest",
        )
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_get_input(self, client: Composio) -> None:
        response = client.tools.with_raw_response.get_input(
            tool_slug="tool_slug",
            text="I need to trigger the main workflow in the octocat/Hello-World repository to deploy to production",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_get_input(self, client: Composio) -> None:
        with client.tools.with_streaming_response.get_input(
            tool_slug="tool_slug",
            text="I need to trigger the main workflow in the octocat/Hello-World repository to deploy to production",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolGetInputResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_input(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_slug` but received ''"):
            client.tools.with_raw_response.get_input(
                tool_slug="",
                text="I need to trigger the main workflow in the octocat/Hello-World repository to deploy to production",
            )

    @parametrize
    def test_method_proxy(self, client: Composio) -> None:
        tool = client.tools.proxy(
            endpoint="/api/v1/resources",
            method="GET",
        )
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    def test_method_proxy_with_all_params(self, client: Composio) -> None:
        tool = client.tools.proxy(
            endpoint="/api/v1/resources",
            method="GET",
            body={
                "name": "New Resource",
                "description": "This is a new resource",
            },
            connected_account_id="ca_1a2b3c4d5e6f",
            custom_connection_data={
                "auth_scheme": "OAUTH2",
                "toolkit_slug": "toolkitSlug",
                "val": {
                    "access_token": "access_token",
                    "account_id": "account_id",
                    "account_url": "account_url",
                    "api_url": "api_url",
                    "authed_user": {
                        "access_token": "access_token",
                        "scope": "scope",
                    },
                    "base_url": "base_url",
                    "borneo_dashboard_url": "borneo_dashboard_url",
                    "companydomain": "COMPANYDOMAIN",
                    "dc": "dc",
                    "domain": "domain",
                    "expires_in": 0,
                    "extension": "extension",
                    "form_api_base_url": "form_api_base_url",
                    "id_token": "id_token",
                    "instance_endpoint": "instanceEndpoint",
                    "instance_name": "instanceName",
                    "long_redirect_url": True,
                    "proxy_password": "proxy_password",
                    "proxy_username": "proxy_username",
                    "refresh_token": "refresh_token",
                    "region": "region",
                    "scope": "string",
                    "server_location": "server_location",
                    "shop": "shop",
                    "site_name": "site_name",
                    "state_prefix": "state_prefix",
                    "subdomain": "subdomain",
                    "token_type": "token_type",
                    "version": "version",
                    "webhook_signature": "webhook_signature",
                    "your_server": "your_server",
                    "your_domain": "your-domain",
                },
            },
            parameters=[
                {
                    "name": "x-api-key",
                    "type": "header",
                    "value": "abc123def456",
                },
                {
                    "name": "filter",
                    "type": "query",
                    "value": "active",
                },
            ],
        )
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_proxy(self, client: Composio) -> None:
        response = client.tools.with_raw_response.proxy(
            endpoint="/api/v1/resources",
            method="GET",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_proxy(self, client: Composio) -> None:
        with client.tools.with_streaming_response.proxy(
            endpoint="/api/v1/resources",
            method="GET",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolProxyResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_enum(self, client: Composio) -> None:
        tool = client.tools.retrieve_enum()
        assert_matches_type(ToolRetrieveEnumResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_retrieve_enum(self, client: Composio) -> None:
        response = client.tools.with_raw_response.retrieve_enum()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolRetrieveEnumResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_enum(self, client: Composio) -> None:
        with client.tools.with_streaming_response.retrieve_enum() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolRetrieveEnumResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.retrieve(
            tool_slug="tool_slug",
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.retrieve(
            tool_slug="tool_slug",
            toolkit_versions="string",
            version="version",
        )
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.retrieve(
            tool_slug="tool_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.retrieve(
            tool_slug="tool_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolRetrieveResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_slug` but received ''"):
            await async_client.tools.with_raw_response.retrieve(
                tool_slug="",
            )

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.list(
            auth_config_ids=["string"],
            cursor="cursor",
            important="true",
            include_deprecated=True,
            limit=0,
            scopes=["string"],
            search="search",
            tags=["string"],
            tool_slugs="tool_slugs",
            toolkit_slug="toolkit_slug",
            toolkit_versions="string",
        )
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_execute(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.execute(
            tool_slug="tool_slug",
        )
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.execute(
            tool_slug="tool_slug",
            allow_tracing=False,
            arguments={
                "repository": "bar",
                "workflow_id": "bar",
                "ref": "bar",
                "inputs": "bar",
            },
            connected_account_id="ca_1a2b3c4d5e6f",
            custom_auth_params={
                "base_url": "https://api.example.com",
                "body": {"foo": "bar"},
                "parameters": [
                    {
                        "in": "header",
                        "name": "x-api-key",
                        "value": "secret-key",
                    }
                ],
            },
            custom_connection_data={
                "auth_scheme": "OAUTH2",
                "toolkit_slug": "github",
                "val": {
                    "access_token": "secret-token",
                    "account_id": "account_id",
                    "account_url": "account_url",
                    "api_url": "api_url",
                    "authed_user": {
                        "access_token": "access_token",
                        "scope": "scope",
                    },
                    "base_url": "base_url",
                    "borneo_dashboard_url": "borneo_dashboard_url",
                    "companydomain": "COMPANYDOMAIN",
                    "dc": "dc",
                    "domain": "domain",
                    "expires_in": 0,
                    "extension": "extension",
                    "form_api_base_url": "form_api_base_url",
                    "id_token": "id_token",
                    "instance_endpoint": "instanceEndpoint",
                    "instance_name": "instanceName",
                    "long_redirect_url": True,
                    "proxy_password": "proxy_password",
                    "proxy_username": "proxy_username",
                    "refresh_token": "refresh_token",
                    "region": "region",
                    "scope": "string",
                    "server_location": "server_location",
                    "shop": "shop",
                    "site_name": "site_name",
                    "state_prefix": "state_prefix",
                    "subdomain": "subdomain",
                    "token_type": "token_type",
                    "version": "version",
                    "webhook_signature": "webhook_signature",
                    "your_server": "your_server",
                    "your_domain": "your-domain",
                },
            },
            text="Trigger the main workflow in the octocat/Hello-World repository on the main branch for the production environment",
            user_id="user-123",
            version="latest",
        )
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.execute(
            tool_slug="tool_slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolExecuteResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.execute(
            tool_slug="tool_slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolExecuteResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_execute(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_slug` but received ''"):
            await async_client.tools.with_raw_response.execute(
                tool_slug="",
            )

    @parametrize
    async def test_method_get_input(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.get_input(
            tool_slug="tool_slug",
            text="I need to trigger the main workflow in the octocat/Hello-World repository to deploy to production",
        )
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    async def test_method_get_input_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.get_input(
            tool_slug="tool_slug",
            text="I need to trigger the main workflow in the octocat/Hello-World repository to deploy to production",
            custom_description="This tool triggers GitHub Actions workflows in a repository. It requires the repository name, workflow ID, and optional input parameters.",
            system_prompt="You are an expert assistant that generates precise GitHub Actions workflow parameters. Extract exact repository names, workflow IDs, and input values from user descriptions.",
            version="latest",
        )
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_get_input(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.get_input(
            tool_slug="tool_slug",
            text="I need to trigger the main workflow in the octocat/Hello-World repository to deploy to production",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolGetInputResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_get_input(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.get_input(
            tool_slug="tool_slug",
            text="I need to trigger the main workflow in the octocat/Hello-World repository to deploy to production",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolGetInputResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_input(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tool_slug` but received ''"):
            await async_client.tools.with_raw_response.get_input(
                tool_slug="",
                text="I need to trigger the main workflow in the octocat/Hello-World repository to deploy to production",
            )

    @parametrize
    async def test_method_proxy(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.proxy(
            endpoint="/api/v1/resources",
            method="GET",
        )
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    async def test_method_proxy_with_all_params(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.proxy(
            endpoint="/api/v1/resources",
            method="GET",
            body={
                "name": "New Resource",
                "description": "This is a new resource",
            },
            connected_account_id="ca_1a2b3c4d5e6f",
            custom_connection_data={
                "auth_scheme": "OAUTH2",
                "toolkit_slug": "toolkitSlug",
                "val": {
                    "access_token": "access_token",
                    "account_id": "account_id",
                    "account_url": "account_url",
                    "api_url": "api_url",
                    "authed_user": {
                        "access_token": "access_token",
                        "scope": "scope",
                    },
                    "base_url": "base_url",
                    "borneo_dashboard_url": "borneo_dashboard_url",
                    "companydomain": "COMPANYDOMAIN",
                    "dc": "dc",
                    "domain": "domain",
                    "expires_in": 0,
                    "extension": "extension",
                    "form_api_base_url": "form_api_base_url",
                    "id_token": "id_token",
                    "instance_endpoint": "instanceEndpoint",
                    "instance_name": "instanceName",
                    "long_redirect_url": True,
                    "proxy_password": "proxy_password",
                    "proxy_username": "proxy_username",
                    "refresh_token": "refresh_token",
                    "region": "region",
                    "scope": "string",
                    "server_location": "server_location",
                    "shop": "shop",
                    "site_name": "site_name",
                    "state_prefix": "state_prefix",
                    "subdomain": "subdomain",
                    "token_type": "token_type",
                    "version": "version",
                    "webhook_signature": "webhook_signature",
                    "your_server": "your_server",
                    "your_domain": "your-domain",
                },
            },
            parameters=[
                {
                    "name": "x-api-key",
                    "type": "header",
                    "value": "abc123def456",
                },
                {
                    "name": "filter",
                    "type": "query",
                    "value": "active",
                },
            ],
        )
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_proxy(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.proxy(
            endpoint="/api/v1/resources",
            method="GET",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolProxyResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_proxy(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.proxy(
            endpoint="/api/v1/resources",
            method="GET",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolProxyResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_enum(self, async_client: AsyncComposio) -> None:
        tool = await async_client.tools.retrieve_enum()
        assert_matches_type(ToolRetrieveEnumResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_enum(self, async_client: AsyncComposio) -> None:
        response = await async_client.tools.with_raw_response.retrieve_enum()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolRetrieveEnumResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_enum(self, async_client: AsyncComposio) -> None:
        async with async_client.tools.with_streaming_response.retrieve_enum() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolRetrieveEnumResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
