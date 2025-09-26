# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import (
    ToolkitListResponse,
    ToolkitRetrieveResponse,
    ToolkitRetrieveCategoriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToolkits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Composio) -> None:
        toolkit = client.toolkits.retrieve(
            slug="github",
        )
        assert_matches_type(ToolkitRetrieveResponse, toolkit, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Composio) -> None:
        toolkit = client.toolkits.retrieve(
            slug="github",
            version="20250905_00",
        )
        assert_matches_type(ToolkitRetrieveResponse, toolkit, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Composio) -> None:
        response = client.toolkits.with_raw_response.retrieve(
            slug="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolkit = response.parse()
        assert_matches_type(ToolkitRetrieveResponse, toolkit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Composio) -> None:
        with client.toolkits.with_streaming_response.retrieve(
            slug="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolkit = response.parse()
            assert_matches_type(ToolkitRetrieveResponse, toolkit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Composio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.toolkits.with_raw_response.retrieve(
                slug="",
            )

    @parametrize
    def test_method_list(self, client: Composio) -> None:
        toolkit = client.toolkits.list()
        assert_matches_type(ToolkitListResponse, toolkit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Composio) -> None:
        toolkit = client.toolkits.list(
            category="productivity",
            cursor="cursor",
            is_local=True,
            limit=0,
            managed_by="composio",
            sort_by="usage",
        )
        assert_matches_type(ToolkitListResponse, toolkit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Composio) -> None:
        response = client.toolkits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolkit = response.parse()
        assert_matches_type(ToolkitListResponse, toolkit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Composio) -> None:
        with client.toolkits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolkit = response.parse()
            assert_matches_type(ToolkitListResponse, toolkit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_categories(self, client: Composio) -> None:
        toolkit = client.toolkits.retrieve_categories()
        assert_matches_type(ToolkitRetrieveCategoriesResponse, toolkit, path=["response"])

    @parametrize
    def test_method_retrieve_categories_with_all_params(self, client: Composio) -> None:
        toolkit = client.toolkits.retrieve_categories(
            cache="1",
        )
        assert_matches_type(ToolkitRetrieveCategoriesResponse, toolkit, path=["response"])

    @parametrize
    def test_raw_response_retrieve_categories(self, client: Composio) -> None:
        response = client.toolkits.with_raw_response.retrieve_categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolkit = response.parse()
        assert_matches_type(ToolkitRetrieveCategoriesResponse, toolkit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_categories(self, client: Composio) -> None:
        with client.toolkits.with_streaming_response.retrieve_categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolkit = response.parse()
            assert_matches_type(ToolkitRetrieveCategoriesResponse, toolkit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncToolkits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncComposio) -> None:
        toolkit = await async_client.toolkits.retrieve(
            slug="github",
        )
        assert_matches_type(ToolkitRetrieveResponse, toolkit, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncComposio) -> None:
        toolkit = await async_client.toolkits.retrieve(
            slug="github",
            version="20250905_00",
        )
        assert_matches_type(ToolkitRetrieveResponse, toolkit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncComposio) -> None:
        response = await async_client.toolkits.with_raw_response.retrieve(
            slug="github",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolkit = await response.parse()
        assert_matches_type(ToolkitRetrieveResponse, toolkit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncComposio) -> None:
        async with async_client.toolkits.with_streaming_response.retrieve(
            slug="github",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolkit = await response.parse()
            assert_matches_type(ToolkitRetrieveResponse, toolkit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncComposio) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.toolkits.with_raw_response.retrieve(
                slug="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncComposio) -> None:
        toolkit = await async_client.toolkits.list()
        assert_matches_type(ToolkitListResponse, toolkit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncComposio) -> None:
        toolkit = await async_client.toolkits.list(
            category="productivity",
            cursor="cursor",
            is_local=True,
            limit=0,
            managed_by="composio",
            sort_by="usage",
        )
        assert_matches_type(ToolkitListResponse, toolkit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncComposio) -> None:
        response = await async_client.toolkits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolkit = await response.parse()
        assert_matches_type(ToolkitListResponse, toolkit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncComposio) -> None:
        async with async_client.toolkits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolkit = await response.parse()
            assert_matches_type(ToolkitListResponse, toolkit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_categories(self, async_client: AsyncComposio) -> None:
        toolkit = await async_client.toolkits.retrieve_categories()
        assert_matches_type(ToolkitRetrieveCategoriesResponse, toolkit, path=["response"])

    @parametrize
    async def test_method_retrieve_categories_with_all_params(self, async_client: AsyncComposio) -> None:
        toolkit = await async_client.toolkits.retrieve_categories(
            cache="1",
        )
        assert_matches_type(ToolkitRetrieveCategoriesResponse, toolkit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_categories(self, async_client: AsyncComposio) -> None:
        response = await async_client.toolkits.with_raw_response.retrieve_categories()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolkit = await response.parse()
        assert_matches_type(ToolkitRetrieveCategoriesResponse, toolkit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_categories(self, async_client: AsyncComposio) -> None:
        async with async_client.toolkits.with_streaming_response.retrieve_categories() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolkit = await response.parse()
            assert_matches_type(ToolkitRetrieveCategoriesResponse, toolkit, path=["response"])

        assert cast(Any, response.is_closed) is True
