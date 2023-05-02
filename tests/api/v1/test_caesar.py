# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Vigenere-API                                                                        +
#  Copyright (C) 2023 Axel DAVID                                                       +
#                                                                                      +
#  This program is free software: you can redistribute it and/or modify it under       +
#  the terms of the GNU General Public License as published by the Free Software       +
#  Foundation, either version 3 of the License, or (at your option) any later version. +
#                                                                                      +
#  This program is distributed in the hope that it will be useful, but WITHOUT ANY     +
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR       +
#  A PARTICULAR PURPOSE. See the GNU General Public License for more details.          +
#                                                                                      +
#  You should have received a copy of the GNU General Public License along with        +
#  this program.  If not, see <https://www.gnu.org/licenses/>.                         +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from typing import Any

import pytest
from blacksheep import Content
from blacksheep.testing import TestClient
from essentials.json import dumps
from pydantic import BaseModel

from vigenere_api.models import CaesarData


def json_content(data: BaseModel) -> Content:
    return Content(
        b"application/json",
        dumps(data, separators=(",", ":")).encode("utf8"),
    )


def bad_content(content: Any, key: Any) -> Content:
    msg = '{"content": '
    msg += f'"{content}"' if isinstance(content, str) else f"{content}"
    msg += ', "key": '
    msg += f'"{key}"' if isinstance(key, str) else f"{key}"
    msg += "}"

    return Content(
        b"application/json",
        msg.encode(),
    )


class CipherSuite:
    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_int_key(test_client: TestClient) -> None:
        caesar_input = CaesarData(
            content="Test",
            key=2,
        )

        response = await test_client.post(
            "/api/v1/caesar/cipher",
            content=json_content(caesar_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        ciphered_caesar = CaesarData.parse_obj(data)

        assert ciphered_caesar.key == caesar_input.key
        assert ciphered_caesar.content == "Vguv"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_negative_int_key(test_client: TestClient) -> None:
        caesar_input = CaesarData(
            content="Test",
            key=-2,
        )

        response = await test_client.post(
            "/api/v1/caesar/cipher",
            content=json_content(caesar_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        ciphered_caesar = CaesarData.parse_obj(data)

        assert ciphered_caesar.key == caesar_input.key
        assert ciphered_caesar.content == "Rcqr"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_str_lower_key(test_client: TestClient) -> None:
        caesar_input = CaesarData(
            content="Test",
            key="c",
        )

        response = await test_client.post(
            "/api/v1/caesar/cipher",
            content=json_content(caesar_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        ciphered_caesar = CaesarData.parse_obj(data)

        assert ciphered_caesar.key == caesar_input.key
        assert ciphered_caesar.content == "Vguv"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_str_upper_key(test_client: TestClient) -> None:
        caesar_input = CaesarData(
            content="Test",
            key="C",
        )

        response = await test_client.post(
            "/api/v1/caesar/cipher",
            content=json_content(caesar_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        ciphered_caesar = CaesarData.parse_obj(data)

        assert ciphered_caesar.key == caesar_input.key
        assert ciphered_caesar.content == "Vguv"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_equality_between_keys(test_client: TestClient) -> None:
        caesar_input1 = CaesarData(
            content="Test",
            key=2,
        )

        response1 = await test_client.post(
            "/api/v1/caesar/cipher",
            content=json_content(caesar_input1),
        )

        assert response1 is not None

        data1 = await response1.json()
        assert data1 is not None

        ciphered_caesar1 = CaesarData.parse_obj(data1)

        assert ciphered_caesar1.key == caesar_input1.key
        assert ciphered_caesar1.content == "Vguv"

        caesar_input2 = CaesarData(
            content="Test",
            key="c",
        )

        response2 = await test_client.post(
            "/api/v1/caesar/cipher",
            content=json_content(caesar_input2),
        )

        assert response2 is not None

        data2 = await response2.json()
        assert data2 is not None

        ciphered_caesar2 = CaesarData.parse_obj(data2)

        assert ciphered_caesar2.key == caesar_input2.key
        assert ciphered_caesar2.content == "Vguv"

        caesar_input3 = CaesarData(
            content="Test",
            key="C",
        )

        response3 = await test_client.post(
            "/api/v1/caesar/cipher",
            content=json_content(caesar_input3),
        )

        assert response3 is not None

        data3 = await response3.json()
        assert data3 is not None

        ciphered_caesar3 = CaesarData.parse_obj(data3)

        assert ciphered_caesar3.key == caesar_input3.key
        assert ciphered_caesar3.content == "Vguv"

        assert (
            ciphered_caesar1.content
            == ciphered_caesar2.content
            == ciphered_caesar3.content
        )

    class BadCipherSuite:
        @staticmethod
        @pytest.mark.asyncio()
        async def test_missing_content(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/cipher",
                content=Content(
                    b"application/json",
                    b'{"key": 2}',
                ),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_missing_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/cipher",
                content=Content(
                    b"application/json",
                    b'{"content": "test"}',
                ),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_type_content(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/cipher",
                content=bad_content(254, 2),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "The content is 'int'. Please give a string.",
                    "type": "type_error.contenttype",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_empty_content(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/cipher",
                content=bad_content("", 2),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "The content is empty. Please give a not empty string.",
                    "type": "value_error.emptycontent",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_type_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/cipher",
                content=bad_content("Test", 25.8),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is 'float'. Please give a string or an integer.",
                    "type": "type_error.keytype",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_empty_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/cipher",
                content=bad_content("Test", ""),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is empty. Please give a one character string or an integer.",
                    "type": "value_error.emptykey",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_too_long_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/cipher",
                content=bad_content("Test", "TT"),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is too long. Please give a one character string or an "
                    "integer.",
                    "type": "value_error.toolongkey",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_not_alpha_str_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/cipher",
                content=bad_content("Test", "+"),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key '+' is invalid. Please give an alphabetic one character "
                    "string or an integer.",
                    "type": "value_error.badkey",
                },
            ]


class DecipherSuite:
    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_int_key(test_client: TestClient) -> None:
        caesar_input = CaesarData(
            content="Test",
            key=2,
        )

        response = await test_client.post(
            "/api/v1/caesar/decipher",
            content=json_content(caesar_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        deciphered_caesar = CaesarData.parse_obj(data)

        assert deciphered_caesar.key == caesar_input.key
        assert deciphered_caesar.content == "Rcqr"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_str_lower_key(test_client: TestClient) -> None:
        caesar_input = CaesarData(
            content="Test",
            key="c",
        )

        response = await test_client.post(
            "/api/v1/caesar/decipher",
            content=json_content(caesar_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        deciphered_caesar = CaesarData.parse_obj(data)

        assert deciphered_caesar.key == caesar_input.key
        assert deciphered_caesar.content == "Rcqr"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_str_upper_key(test_client: TestClient) -> None:
        caesar_input = CaesarData(
            content="Test",
            key="C",
        )

        response = await test_client.post(
            "/api/v1/caesar/decipher",
            content=json_content(caesar_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        deciphered_caesar = CaesarData.parse_obj(data)

        assert deciphered_caesar.key == caesar_input.key
        assert deciphered_caesar.content == "Rcqr"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_equality_between_keys(test_client: TestClient) -> None:
        caesar_input1 = CaesarData(
            content="Test",
            key=2,
        )

        response1 = await test_client.post(
            "/api/v1/caesar/decipher",
            content=json_content(caesar_input1),
        )

        assert response1 is not None

        data1 = await response1.json()
        assert data1 is not None

        deciphered_caesar1 = CaesarData.parse_obj(data1)

        assert deciphered_caesar1.key == caesar_input1.key
        assert deciphered_caesar1.content == "Rcqr"

        caesar_input2 = CaesarData(
            content="Test",
            key="c",
        )

        response2 = await test_client.post(
            "/api/v1/caesar/decipher",
            content=json_content(caesar_input2),
        )

        assert response2 is not None

        data2 = await response2.json()
        assert data2 is not None

        deciphered_caesar2 = CaesarData.parse_obj(data2)

        assert deciphered_caesar2.key == caesar_input2.key
        assert deciphered_caesar2.content == "Rcqr"

        caesar_input3 = CaesarData(
            content="Test",
            key="C",
        )

        response3 = await test_client.post(
            "/api/v1/caesar/decipher",
            content=json_content(caesar_input3),
        )

        assert response3 is not None

        data3 = await response3.json()
        assert data3 is not None

        deciphered_caesar3 = CaesarData.parse_obj(data3)

        assert deciphered_caesar3.key == caesar_input3.key
        assert deciphered_caesar3.content == "Rcqr"

        assert (
            deciphered_caesar1.content
            == deciphered_caesar2.content
            == deciphered_caesar3.content
        )

    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_negative_int_key(test_client: TestClient) -> None:
        caesar_input = CaesarData(
            content="Test",
            key=-2,
        )

        response = await test_client.post(
            "/api/v1/caesar/decipher",
            content=json_content(caesar_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        deciphered_caesar = CaesarData.parse_obj(data)

        assert deciphered_caesar.key == caesar_input.key
        assert deciphered_caesar.content == "Vguv"

    class BadDecipherSuite:
        @staticmethod
        @pytest.mark.asyncio()
        async def test_missing_content(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/decipher",
                content=Content(
                    b"application/json",
                    b'{"key": 2}',
                ),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_missing_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/decipher",
                content=Content(
                    b"application/json",
                    b'{"content": "test"}',
                ),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_type_content(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/decipher",
                content=bad_content(254, 2),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "The content is 'int'. Please give a string.",
                    "type": "type_error.contenttype",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_empty_content(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/decipher",
                content=bad_content("", 2),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "The content is empty. Please give a not empty string.",
                    "type": "value_error.emptycontent",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_type_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/decipher",
                content=bad_content("Test", 25.8),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is 'float'. Please give a string or an integer.",
                    "type": "type_error.keytype",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_empty_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/decipher",
                content=bad_content("Test", ""),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is empty. Please give a one character string or an integer.",
                    "type": "value_error.emptykey",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_too_long_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/decipher",
                content=bad_content("Test", "TT"),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is too long. Please give a one character string or an "
                    "integer.",
                    "type": "value_error.toolongkey",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_not_alpha_str_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v1/caesar/decipher",
                content=bad_content("Test", "+"),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key '+' is invalid. Please give an alphabetic one character "
                    "string or an integer.",
                    "type": "value_error.badkey",
                },
            ]
