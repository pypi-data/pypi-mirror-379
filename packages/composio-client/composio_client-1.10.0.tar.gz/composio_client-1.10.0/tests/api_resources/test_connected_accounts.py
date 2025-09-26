# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    ConnectedAccountListResponse,
    ConnectedAccountCreateResponse,
    ConnectedAccountDeleteResponse,
    ConnectedAccountRefreshResponse,
    ConnectedAccountRetrieveResponse,
    ConnectedAccountUpdateStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectedAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Composio) -> None:
        connected_account = client.connected_accounts.create(
            auth_config={"id": "id"},
            connection={},
        )
        assert_matches_type(ConnectedAccountCreateResponse, connected_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Composio) -> None:
        connected_account = client.connected_accounts.create(
            auth_config={"id": "id"},
            connection={
                "callback_url": "https://example.com",
                "state": {
                    "auth_scheme": "OAUTH1",
                    "val": {
                        "status": "INITIALIZING",
                        "account_id": "account_id",
                        "account_url": "account_url",
                        "api_url": "api_url",
                        "base_url": "base_url",
                        "borneo_dashboard_url": "borneo_dashboard_url",
                        "companydomain": "COMPANYDOMAIN",
                        "dc": "dc",
                        "domain": "domain",
                        "extension": "extension",
                        "form_api_base_url": "form_api_base_url",
                        "instance_endpoint": "instanceEndpoint",
                        "instance_name": "instanceName",
                        "proxy_password": "proxy_password",
                        "proxy_username": "proxy_username",
                        "region": "region",
                        "server_location": "server_location",
                        "shop": "shop",
                        "site_name": "site_name",
                        "subdomain": "subdomain",
                        "version": "version",
                        "your_server": "your_server",
                        "your_domain": "your-domain",
                    },
                },
                "user_id": "user_id",
            },
        )
        assert_matches_type(ConnectedAccountCreateResponse, connected_account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Composio) -> None:
        response = client.connected_accounts.with_raw_response.create(
            auth_config={"id": "id"},
            connection={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccountCreateResponse, connected_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Composio) -> None:
        with client.connected_accounts.with_streaming_response.create(
            auth_config={"id": "id"},
            connection={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccountCreateResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        connected_account = client.connected_accounts.retrieve(
            "con_1a2b3c4d5e6f",
        )
        assert_matches_type(ConnectedAccountRetrieveResponse, connected_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.connected_accounts.with_raw_response.retrieve(
            "con_1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccountRetrieveResponse, connected_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.connected_accounts.with_streaming_response.retrieve(
            "con_1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccountRetrieveResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            client.connected_accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_method_list(self, client: Composio) -> None:
        connected_account = client.connected_accounts.list()
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        connected_account = client.connected_accounts.list(
            auth_config_ids=["string"],
            connected_account_ids=["string"],
            cursor="cursor",
            labels=["string"],
            limit=0,
            order_by="created_at",
            order_direction="asc",
            statuses=["INITIALIZING"],
            toolkit_slugs=["string"],
            user_ids=["string"],
        )
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.connected_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.connected_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Composio) -> None:
        connected_account = client.connected_accounts.delete(
            "con_1a2b3c4d5e6f",
        )
        assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Composio) -> None:
        response = client.connected_accounts.with_raw_response.delete(
            "con_1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Composio) -> None:
        with client.connected_accounts.with_streaming_response.delete(
            "con_1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            client.connected_accounts.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_refresh(self, client: Composio) -> None:
        connected_account = client.connected_accounts.refresh(
            nanoid="con_1a2b3c4d5e6f",
        )
        assert_matches_type(ConnectedAccountRefreshResponse, connected_account, path=["response"])

    @parametrize
    def test_method_refresh_with_all_params(self, client: Composio) -> None:
        connected_account = client.connected_accounts.refresh(
            nanoid="con_1a2b3c4d5e6f",
            query_redirect_url="redirect_url",
            body_redirect_url="redirect_url",
        )
        assert_matches_type(ConnectedAccountRefreshResponse, connected_account, path=["response"])

    @parametrize
    def test_raw_response_refresh(self, client: Composio) -> None:
        response = client.connected_accounts.with_raw_response.refresh(
            nanoid="con_1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccountRefreshResponse, connected_account, path=["response"])

    @parametrize
    def test_streaming_response_refresh(self, client: Composio) -> None:
        with client.connected_accounts.with_streaming_response.refresh(
            nanoid="con_1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccountRefreshResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_refresh(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            client.connected_accounts.with_raw_response.refresh(
                nanoid="",
            )

    @parametrize
    def test_method_update_status(self, client: Composio) -> None:
        connected_account = client.connected_accounts.update_status(
            nano_id="con_1a2b3c4d5e6f",
            enabled=True,
        )
        assert_matches_type(ConnectedAccountUpdateStatusResponse, connected_account, path=["response"])

    @parametrize
    def test_raw_response_update_status(self, client: Composio) -> None:
        response = client.connected_accounts.with_raw_response.update_status(
            nano_id="con_1a2b3c4d5e6f",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = response.parse()
        assert_matches_type(ConnectedAccountUpdateStatusResponse, connected_account, path=["response"])

    @parametrize
    def test_streaming_response_update_status(self, client: Composio) -> None:
        with client.connected_accounts.with_streaming_response.update_status(
            nano_id="con_1a2b3c4d5e6f",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = response.parse()
            assert_matches_type(ConnectedAccountUpdateStatusResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_status(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nano_id` but received ''"):
            client.connected_accounts.with_raw_response.update_status(
                nano_id="",
                enabled=True,
            )


class TestAsyncConnectedAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncComposio) -> None:
        connected_account = await async_client.connected_accounts.create(
            auth_config={"id": "id"},
            connection={},
        )
        assert_matches_type(ConnectedAccountCreateResponse, connected_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncComposio) -> None:
        connected_account = await async_client.connected_accounts.create(
            auth_config={"id": "id"},
            connection={
                "callback_url": "https://example.com",
                "state": {
                    "auth_scheme": "OAUTH1",
                    "val": {
                        "status": "INITIALIZING",
                        "account_id": "account_id",
                        "account_url": "account_url",
                        "api_url": "api_url",
                        "base_url": "base_url",
                        "borneo_dashboard_url": "borneo_dashboard_url",
                        "companydomain": "COMPANYDOMAIN",
                        "dc": "dc",
                        "domain": "domain",
                        "extension": "extension",
                        "form_api_base_url": "form_api_base_url",
                        "instance_endpoint": "instanceEndpoint",
                        "instance_name": "instanceName",
                        "proxy_password": "proxy_password",
                        "proxy_username": "proxy_username",
                        "region": "region",
                        "server_location": "server_location",
                        "shop": "shop",
                        "site_name": "site_name",
                        "subdomain": "subdomain",
                        "version": "version",
                        "your_server": "your_server",
                        "your_domain": "your-domain",
                    },
                },
                "user_id": "user_id",
            },
        )
        assert_matches_type(ConnectedAccountCreateResponse, connected_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncComposio) -> None:
        response = await async_client.connected_accounts.with_raw_response.create(
            auth_config={"id": "id"},
            connection={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccountCreateResponse, connected_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncComposio) -> None:
        async with async_client.connected_accounts.with_streaming_response.create(
            auth_config={"id": "id"},
            connection={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccountCreateResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        connected_account = await async_client.connected_accounts.retrieve(
            "con_1a2b3c4d5e6f",
        )
        assert_matches_type(ConnectedAccountRetrieveResponse, connected_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.connected_accounts.with_raw_response.retrieve(
            "con_1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccountRetrieveResponse, connected_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.connected_accounts.with_streaming_response.retrieve(
            "con_1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccountRetrieveResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            await async_client.connected_accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        connected_account = await async_client.connected_accounts.list()
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        connected_account = await async_client.connected_accounts.list(
            auth_config_ids=["string"],
            connected_account_ids=["string"],
            cursor="cursor",
            labels=["string"],
            limit=0,
            order_by="created_at",
            order_direction="asc",
            statuses=["INITIALIZING"],
            toolkit_slugs=["string"],
            user_ids=["string"],
        )
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.connected_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.connected_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccountListResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncComposio) -> None:
        connected_account = await async_client.connected_accounts.delete(
            "con_1a2b3c4d5e6f",
        )
        assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncComposio) -> None:
        response = await async_client.connected_accounts.with_raw_response.delete(
            "con_1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncComposio) -> None:
        async with async_client.connected_accounts.with_streaming_response.delete(
            "con_1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccountDeleteResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            await async_client.connected_accounts.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_refresh(self, async_client: AsyncComposio) -> None:
        connected_account = await async_client.connected_accounts.refresh(
            nanoid="con_1a2b3c4d5e6f",
        )
        assert_matches_type(ConnectedAccountRefreshResponse, connected_account, path=["response"])

    @parametrize
    async def test_method_refresh_with_all_params(self, async_client: AsyncComposio) -> None:
        connected_account = await async_client.connected_accounts.refresh(
            nanoid="con_1a2b3c4d5e6f",
            query_redirect_url="redirect_url",
            body_redirect_url="redirect_url",
        )
        assert_matches_type(ConnectedAccountRefreshResponse, connected_account, path=["response"])

    @parametrize
    async def test_raw_response_refresh(self, async_client: AsyncComposio) -> None:
        response = await async_client.connected_accounts.with_raw_response.refresh(
            nanoid="con_1a2b3c4d5e6f",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccountRefreshResponse, connected_account, path=["response"])

    @parametrize
    async def test_streaming_response_refresh(self, async_client: AsyncComposio) -> None:
        async with async_client.connected_accounts.with_streaming_response.refresh(
            nanoid="con_1a2b3c4d5e6f",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccountRefreshResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_refresh(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nanoid` but received ''"):
            await async_client.connected_accounts.with_raw_response.refresh(
                nanoid="",
            )

    @parametrize
    async def test_method_update_status(self, async_client: AsyncComposio) -> None:
        connected_account = await async_client.connected_accounts.update_status(
            nano_id="con_1a2b3c4d5e6f",
            enabled=True,
        )
        assert_matches_type(ConnectedAccountUpdateStatusResponse, connected_account, path=["response"])

    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncComposio) -> None:
        response = await async_client.connected_accounts.with_raw_response.update_status(
            nano_id="con_1a2b3c4d5e6f",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connected_account = await response.parse()
        assert_matches_type(ConnectedAccountUpdateStatusResponse, connected_account, path=["response"])

    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncComposio) -> None:
        async with async_client.connected_accounts.with_streaming_response.update_status(
            nano_id="con_1a2b3c4d5e6f",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connected_account = await response.parse()
            assert_matches_type(ConnectedAccountUpdateStatusResponse, connected_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `nano_id` but received ''"):
            await async_client.connected_accounts.with_raw_response.update_status(
                nano_id="",
                enabled=True,
            )
