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

from vigenere_api.models import VigenereData


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
    async def test_with_str_lower_key(test_client: TestClient) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="ct",
        )

        response = await test_client.post(
            "/api/v2/vigenere/cipher",
            content=json_content(vigenere_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        ciphered_vigenere = VigenereData.parse_obj(data)

        assert ciphered_vigenere.key == vigenere_input.key
        assert ciphered_vigenere.content == "Vxum"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_str_upper_key(test_client: TestClient) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="CT",
        )

        response = await test_client.post(
            "/api/v2/vigenere/cipher",
            content=json_content(vigenere_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        ciphered_vigenere = VigenereData.parse_obj(data)

        assert ciphered_vigenere.key == vigenere_input.key
        assert ciphered_vigenere.content == "Vxum"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_str_mixes_key(test_client: TestClient) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="Ct",
        )

        response = await test_client.post(
            "/api/v2/vigenere/cipher",
            content=json_content(vigenere_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        ciphered_vigenere = VigenereData.parse_obj(data)

        assert ciphered_vigenere.key == vigenere_input.key
        assert ciphered_vigenere.content == "Vxum"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_equality_between_keys(test_client: TestClient) -> None:
        vigenere_input1 = VigenereData(
            content="Test",
            key="ct",
        )

        response1 = await test_client.post(
            "/api/v2/vigenere/cipher",
            content=json_content(vigenere_input1),
        )

        assert response1 is not None

        data1 = await response1.json()
        assert data1 is not None

        ciphered_vigenere1 = VigenereData.parse_obj(data1)

        assert ciphered_vigenere1.key == vigenere_input1.key
        assert ciphered_vigenere1.content == "Vxum"

        vigenere_input2 = VigenereData(
            content="Test",
            key="cT",
        )

        response2 = await test_client.post(
            "/api/v2/vigenere/cipher",
            content=json_content(vigenere_input2),
        )

        assert response2 is not None

        data2 = await response2.json()
        assert data2 is not None

        ciphered_vigenere2 = VigenereData.parse_obj(data2)

        assert ciphered_vigenere2.key == vigenere_input2.key
        assert ciphered_vigenere2.content == "Vxum"

        vigenere_input3 = VigenereData(
            content="Test",
            key="CT",
        )

        response3 = await test_client.post(
            "/api/v2/vigenere/cipher",
            content=json_content(vigenere_input3),
        )

        assert response3 is not None

        data3 = await response3.json()
        assert data3 is not None

        ciphered_vigenere3 = VigenereData.parse_obj(data3)

        assert ciphered_vigenere3.key == vigenere_input3.key
        assert ciphered_vigenere3.content == "Vxum"

        assert (
            ciphered_vigenere1.content
            == ciphered_vigenere2.content
            == ciphered_vigenere3.content
        )

    class BadCipherSuite:
        @staticmethod
        @pytest.mark.asyncio()
        async def test_missing_content(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v2/vigenere/cipher",
                content=Content(
                    b"application/json",
                    b'{"key": "ct"}',
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
                "/api/v2/vigenere/cipher",
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
                "/api/v2/vigenere/cipher",
                content=bad_content(254, "tt"),
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
                "/api/v2/vigenere/cipher",
                content=bad_content("", "ty"),
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
                "/api/v2/vigenere/cipher",
                content=bad_content("Test", 25.8),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is 'float'. Please give a string.",
                    "type": "type_error.keytype",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_empty_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v2/vigenere/cipher",
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
        async def test_too_short_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v2/vigenere/cipher",
                content=bad_content("Test", "T"),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is too short. Please give a string with more than one character.",
                    "type": "value_error.tooshortkey",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_not_alpha_str_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v2/vigenere/cipher",
                content=bad_content("Test", "+t"),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key '+t' is invalid. Please give a string.",
                    "type": "value_error.badkey",
                },
            ]


class DecipherSuite:
    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_str_lower_key(test_client: TestClient) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="ct",
        )

        response = await test_client.post(
            "/api/v2/vigenere/decipher",
            content=json_content(vigenere_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        deciphered_vigenere = VigenereData.parse_obj(data)

        assert deciphered_vigenere.key == vigenere_input.key
        assert deciphered_vigenere.content == "Rlqa"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_str_upper_key(test_client: TestClient) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="CT",
        )

        response = await test_client.post(
            "/api/v2/vigenere/decipher",
            content=json_content(vigenere_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        deciphered_vigenere = VigenereData.parse_obj(data)

        assert deciphered_vigenere.key == vigenere_input.key
        assert deciphered_vigenere.content == "Rlqa"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_with_str_mixed_key(test_client: TestClient) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="Ct",
        )

        response = await test_client.post(
            "/api/v2/vigenere/decipher",
            content=json_content(vigenere_input),
        )

        assert response is not None

        data = await response.json()
        assert data is not None

        deciphered_vigenere = VigenereData.parse_obj(data)

        assert deciphered_vigenere.key == vigenere_input.key
        assert deciphered_vigenere.content == "Rlqa"

    @staticmethod
    @pytest.mark.asyncio()
    async def test_equality_between_keys(test_client: TestClient) -> None:
        vigenere_input1 = VigenereData(
            content="Test",
            key="ct",
        )

        response1 = await test_client.post(
            "/api/v2/vigenere/decipher",
            content=json_content(vigenere_input1),
        )

        assert response1 is not None

        data1 = await response1.json()
        assert data1 is not None

        deciphered_vigenere1 = VigenereData.parse_obj(data1)

        assert deciphered_vigenere1.key == vigenere_input1.key
        assert deciphered_vigenere1.content == "Rlqa"

        vigenere_input2 = VigenereData(
            content="Test",
            key="cT",
        )

        response2 = await test_client.post(
            "/api/v2/vigenere/decipher",
            content=json_content(vigenere_input2),
        )

        assert response2 is not None

        data2 = await response2.json()
        assert data2 is not None

        deciphered_vigenere2 = VigenereData.parse_obj(data2)

        assert deciphered_vigenere2.key == vigenere_input2.key
        assert deciphered_vigenere2.content == "Rlqa"

        vigenere_input3 = VigenereData(
            content="Test",
            key="CT",
        )

        response3 = await test_client.post(
            "/api/v2/vigenere/decipher",
            content=json_content(vigenere_input3),
        )

        assert response3 is not None

        data3 = await response3.json()
        assert data3 is not None

        deciphered_vigenere3 = VigenereData.parse_obj(data3)

        assert deciphered_vigenere3.key == vigenere_input3.key
        assert deciphered_vigenere3.content == "Rlqa"

        assert (
            deciphered_vigenere1.content
            == deciphered_vigenere2.content
            == deciphered_vigenere3.content
        )

    class BadDecipherSuite:
        @staticmethod
        @pytest.mark.asyncio()
        async def test_missing_content(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v2/vigenere/decipher",
                content=Content(
                    b"application/json",
                    b'{"key": "tt"}',
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
                "/api/v2/vigenere/decipher",
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
                "/api/v2/vigenere/decipher",
                content=bad_content(254, "tt"),
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
                "/api/v2/vigenere/decipher",
                content=bad_content("", "tt"),
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
                "/api/v2/vigenere/decipher",
                content=bad_content("Test", 25.8),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is 'float'. Please give a string.",
                    "type": "type_error.keytype",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_empty_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v2/vigenere/decipher",
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
        async def test_too_short_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v2/vigenere/decipher",
                content=bad_content("Test", "T"),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is too short. Please give a string with more than one character.",
                    "type": "value_error.tooshortkey",
                },
            ]

        @staticmethod
        @pytest.mark.asyncio()
        async def test_bad_not_alpha_str_key(test_client: TestClient) -> None:
            response = await test_client.post(
                "/api/v2/vigenere/decipher",
                content=bad_content("Test", "+t"),
            )

            assert response is not None

            data = await response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key '+t' is invalid. Please give a string.",
                    "type": "value_error.badkey",
                },
            ]
