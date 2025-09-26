# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    TriggerInstanceUpsertResponse,
    TriggerInstanceListActiveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTriggerInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_method_list_active(self, client: Composio) -> None:
        trigger_instance = client.trigger_instances.list_active()
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_method_list_active_with_all_params(self, client: Composio) -> None:
        trigger_instance = client.trigger_instances.list_active(
            query_auth_config_ids_1=["string"],
            query_auth_config_ids_2="authConfigIds",
            query_connected_account_ids_1=["string"],
            query_connected_account_ids_2="connectedAccountIds",
            cursor="cursor",
            deprecated_auth_config_uuids=["string"],
            deprecated_connected_account_uuids=["string"],
            limit=0,
            page=1,
            query_show_disabled_1=True,
            query_show_disabled_2="showDisabled",
            query_trigger_ids_1=["string"],
            query_trigger_names_1=["string"],
            query_trigger_ids_2="triggerIds",
            query_trigger_names_2="triggerNames",
        )
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_raw_response_list_active(self, client: Composio) -> None:
        response = client.trigger_instances.with_raw_response.list_active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = response.parse()
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    def test_streaming_response_list_active(self, client: Composio) -> None:
        with client.trigger_instances.with_streaming_response.list_active() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = response.parse()
            assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upsert(self, client: Composio) -> None:
        trigger_instance = client.trigger_instances.upsert(
            slug="slug",
        )
        assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    def test_method_upsert_with_all_params(self, client: Composio) -> None:
        trigger_instance = client.trigger_instances.upsert(
            slug="slug",
            connected_account_id="connected_account_id",
            body_trigger_config_1={"foo": "bar"},
            body_trigger_config_2={"foo": "bar"},
        )
        assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    def test_raw_response_upsert(self, client: Composio) -> None:
        response = client.trigger_instances.with_raw_response.upsert(
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = response.parse()
        assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    def test_streaming_response_upsert(self, client: Composio) -> None:
        with client.trigger_instances.with_streaming_response.upsert(
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = response.parse()
            assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upsert(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.trigger_instances.with_raw_response.upsert(
                slug="",
            )


class TestAsyncTriggerInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_method_list_active(self, async_client: AsyncComposio) -> None:
        trigger_instance = await async_client.trigger_instances.list_active()
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_method_list_active_with_all_params(self, async_client: AsyncComposio) -> None:
        trigger_instance = await async_client.trigger_instances.list_active(
            query_auth_config_ids_1=["string"],
            query_auth_config_ids_2="authConfigIds",
            query_connected_account_ids_1=["string"],
            query_connected_account_ids_2="connectedAccountIds",
            cursor="cursor",
            deprecated_auth_config_uuids=["string"],
            deprecated_connected_account_uuids=["string"],
            limit=0,
            page=1,
            query_show_disabled_1=True,
            query_show_disabled_2="showDisabled",
            query_trigger_ids_1=["string"],
            query_trigger_names_1=["string"],
            query_trigger_ids_2="triggerIds",
            query_trigger_names_2="triggerNames",
        )
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_raw_response_list_active(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger_instances.with_raw_response.list_active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = await response.parse()
        assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

    @pytest.mark.skip(reason="no prism support for query param arrays")
    @parametrize
    async def test_streaming_response_list_active(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger_instances.with_streaming_response.list_active() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = await response.parse()
            assert_matches_type(TriggerInstanceListActiveResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upsert(self, async_client: AsyncComposio) -> None:
        trigger_instance = await async_client.trigger_instances.upsert(
            slug="slug",
        )
        assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncComposio) -> None:
        trigger_instance = await async_client.trigger_instances.upsert(
            slug="slug",
            connected_account_id="connected_account_id",
            body_trigger_config_1={"foo": "bar"},
            body_trigger_config_2={"foo": "bar"},
        )
        assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncComposio) -> None:
        response = await async_client.trigger_instances.with_raw_response.upsert(
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trigger_instance = await response.parse()
        assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncComposio) -> None:
        async with async_client.trigger_instances.with_streaming_response.upsert(
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trigger_instance = await response.parse()
            assert_matches_type(TriggerInstanceUpsertResponse, trigger_instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.trigger_instances.with_raw_response.upsert(
                slug="",
            )
