# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from composio_client import Composio, AsyncComposio
from composio_client.types import CliGetSessionResponse, CliCreateSessionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCli:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_session(self, client: Composio) -> None:
        cli = client.cli.create_session()
        assert_matches_type(CliCreateSessionResponse, cli, path=["response"])

    @parametrize
    def test_raw_response_create_session(self, client: Composio) -> None:
        response = client.cli.with_raw_response.create_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cli = response.parse()
        assert_matches_type(CliCreateSessionResponse, cli, path=["response"])

    @parametrize
    def test_streaming_response_create_session(self, client: Composio) -> None:
        with client.cli.with_streaming_response.create_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cli = response.parse()
            assert_matches_type(CliCreateSessionResponse, cli, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_session(self, client: Composio) -> None:
        cli = client.cli.get_session(
            id="ABC123",
        )
        assert_matches_type(CliGetSessionResponse, cli, path=["response"])

    @parametrize
    def test_raw_response_get_session(self, client: Composio) -> None:
        response = client.cli.with_raw_response.get_session(
            id="ABC123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cli = response.parse()
        assert_matches_type(CliGetSessionResponse, cli, path=["response"])

    @parametrize
    def test_streaming_response_get_session(self, client: Composio) -> None:
        with client.cli.with_streaming_response.get_session(
            id="ABC123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cli = response.parse()
            assert_matches_type(CliGetSessionResponse, cli, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCli:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_session(self, async_client: AsyncComposio) -> None:
        cli = await async_client.cli.create_session()
        assert_matches_type(CliCreateSessionResponse, cli, path=["response"])

    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncComposio) -> None:
        response = await async_client.cli.with_raw_response.create_session()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cli = await response.parse()
        assert_matches_type(CliCreateSessionResponse, cli, path=["response"])

    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncComposio) -> None:
        async with async_client.cli.with_streaming_response.create_session() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cli = await response.parse()
            assert_matches_type(CliCreateSessionResponse, cli, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_session(self, async_client: AsyncComposio) -> None:
        cli = await async_client.cli.get_session(
            id="ABC123",
        )
        assert_matches_type(CliGetSessionResponse, cli, path=["response"])

    @parametrize
    async def test_raw_response_get_session(self, async_client: AsyncComposio) -> None:
        response = await async_client.cli.with_raw_response.get_session(
            id="ABC123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cli = await response.parse()
        assert_matches_type(CliGetSessionResponse, cli, path=["response"])

    @parametrize
    async def test_streaming_response_get_session(self, async_client: AsyncComposio) -> None:
        async with async_client.cli.with_streaming_response.get_session(
            id="ABC123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cli = await response.parse()
            assert_matches_type(CliGetSessionResponse, cli, path=["response"])

        assert cast(Any, response.is_closed) is True
