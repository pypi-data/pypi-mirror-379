# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from legalesign import Legalesign, AsyncLegalesign
from tests.utils import assert_matches_type
from legalesign.types.templatepdf import FieldListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Legalesign) -> None:
        field = client.templatepdf.fields.create(
            pdf_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "ax": 0,
                    "ay": 0,
                    "bx": 0,
                    "by": 0,
                    "element_type": "signature",
                    "page": 0,
                    "signer": 1,
                }
            ],
        )
        assert field is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Legalesign) -> None:
        response = client.templatepdf.fields.with_raw_response.create(
            pdf_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "ax": 0,
                    "ay": 0,
                    "bx": 0,
                    "by": 0,
                    "element_type": "signature",
                    "page": 0,
                    "signer": 1,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert field is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Legalesign) -> None:
        with client.templatepdf.fields.with_streaming_response.create(
            pdf_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "ax": 0,
                    "ay": 0,
                    "bx": 0,
                    "by": 0,
                    "element_type": "signature",
                    "page": 0,
                    "signer": 1,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert field is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Legalesign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pdf_id` but received ''"):
            client.templatepdf.fields.with_raw_response.create(
                pdf_id="",
                body=[
                    {
                        "ax": 0,
                        "ay": 0,
                        "bx": 0,
                        "by": 0,
                        "element_type": "signature",
                        "page": 0,
                        "signer": 1,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Legalesign) -> None:
        field = client.templatepdf.fields.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FieldListResponse, field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Legalesign) -> None:
        response = client.templatepdf.fields.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Legalesign) -> None:
        with client.templatepdf.fields.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert_matches_type(FieldListResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Legalesign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pdf_id` but received ''"):
            client.templatepdf.fields.with_raw_response.list(
                "",
            )


class TestAsyncFields:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLegalesign) -> None:
        field = await async_client.templatepdf.fields.create(
            pdf_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "ax": 0,
                    "ay": 0,
                    "bx": 0,
                    "by": 0,
                    "element_type": "signature",
                    "page": 0,
                    "signer": 1,
                }
            ],
        )
        assert field is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLegalesign) -> None:
        response = await async_client.templatepdf.fields.with_raw_response.create(
            pdf_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "ax": 0,
                    "ay": 0,
                    "bx": 0,
                    "by": 0,
                    "element_type": "signature",
                    "page": 0,
                    "signer": 1,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert field is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLegalesign) -> None:
        async with async_client.templatepdf.fields.with_streaming_response.create(
            pdf_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body=[
                {
                    "ax": 0,
                    "ay": 0,
                    "bx": 0,
                    "by": 0,
                    "element_type": "signature",
                    "page": 0,
                    "signer": 1,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert field is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLegalesign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pdf_id` but received ''"):
            await async_client.templatepdf.fields.with_raw_response.create(
                pdf_id="",
                body=[
                    {
                        "ax": 0,
                        "ay": 0,
                        "bx": 0,
                        "by": 0,
                        "element_type": "signature",
                        "page": 0,
                        "signer": 1,
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLegalesign) -> None:
        field = await async_client.templatepdf.fields.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FieldListResponse, field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLegalesign) -> None:
        response = await async_client.templatepdf.fields.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert_matches_type(FieldListResponse, field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLegalesign) -> None:
        async with async_client.templatepdf.fields.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert_matches_type(FieldListResponse, field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLegalesign) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pdf_id` but received ''"):
            await async_client.templatepdf.fields.with_raw_response.list(
                "",
            )
