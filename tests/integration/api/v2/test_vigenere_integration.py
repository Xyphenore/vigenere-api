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
import requests
from pydantic import BaseModel

from vigenere_api.models import VigenereData


def json_data(data: BaseModel) -> dict[str, Any]:
    return data.dict()


def bad_content(content: Any, key: Any) -> dict[str, Any]:
    return {"content": content, "key": key}


class IntegrationCipherSuite:
    @staticmethod
    @pytest.mark.integration_test()
    def test_with_str_lower_key(server: str) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="ct",
        )

        response = requests.post(
            url=server + "/api/v2/vigenere/cipher",
            json=json_data(vigenere_input),
            timeout=1,
        )

        assert response is not None

        data = response.json()
        assert data is not None

        ciphered_vigenere = VigenereData.parse_obj(data)

        assert ciphered_vigenere.key == vigenere_input.key
        assert ciphered_vigenere.content == "Vxum"

    @staticmethod
    @pytest.mark.integration_test()
    def test_with_str_upper_key(server: str) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="CT",
        )

        response = requests.post(
            url=server + "/api/v2/vigenere/cipher",
            json=json_data(vigenere_input),
            timeout=1,
        )

        assert response is not None

        data = response.json()
        assert data is not None

        ciphered_vigenere = VigenereData.parse_obj(data)

        assert ciphered_vigenere.key == vigenere_input.key
        assert ciphered_vigenere.content == "Vxum"

    @staticmethod
    @pytest.mark.integration_test()
    def test_with_str_mixed_key(server: str) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="Ct",
        )

        response = requests.post(
            url=server + "/api/v2/vigenere/cipher",
            json=json_data(vigenere_input),
            timeout=1,
        )

        assert response is not None

        data = response.json()
        assert data is not None

        ciphered_vigenere = VigenereData.parse_obj(data)

        assert ciphered_vigenere.key == vigenere_input.key
        assert ciphered_vigenere.content == "Vxum"

    @staticmethod
    @pytest.mark.integration_test()
    def test_equality_between_keys(server: str) -> None:
        vigenere_input1 = VigenereData(
            content="Test",
            key="ct",
        )

        response1 = requests.post(
            url=server + "/api/v2/vigenere/cipher",
            json=json_data(vigenere_input1),
            timeout=1,
        )

        assert response1 is not None

        data1 = response1.json()
        assert data1 is not None

        ciphered_vigenere1 = VigenereData.parse_obj(data1)

        assert ciphered_vigenere1.key == vigenere_input1.key
        assert ciphered_vigenere1.content == "Vxum"

        vigenere_input2 = VigenereData(
            content="Test",
            key="cT",
        )

        response2 = requests.post(
            url=server + "/api/v2/vigenere/cipher",
            json=json_data(vigenere_input2),
            timeout=1,
        )

        assert response2 is not None

        data2 = response2.json()
        assert data2 is not None

        ciphered_vigenere2 = VigenereData.parse_obj(data2)

        assert ciphered_vigenere2.key == vigenere_input2.key
        assert ciphered_vigenere2.content == "Vxum"

        vigenere_input3 = VigenereData(
            content="Test",
            key="CT",
        )

        response3 = requests.post(
            url=server + "/api/v2/vigenere/cipher",
            json=json_data(vigenere_input3),
            timeout=1,
        )

        assert response3 is not None

        data3 = response3.json()
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
        @pytest.mark.integration_test()
        def test_missing_content(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/cipher",
                json={"key": "tt"},
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_missing_key(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/cipher",
                json={"content": "test"},
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_bad_type_content(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/cipher",
                json=bad_content(254, "tt"),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "The content is 'int'. Please give a string.",
                    "type": "type_error.contenttype",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_bad_empty_content(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/cipher",
                json=bad_content("", "tt"),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "The content is empty. Please give a not empty string.",
                    "type": "value_error.emptycontent",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_bad_type_key(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/cipher",
                json=bad_content("Test", 25.8),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is 'float'. Please give a string.",
                    "type": "type_error.keytype",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_bad_empty_key(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/cipher",
                json=bad_content("Test", ""),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is empty. Please give a one character string or an integer.",
                    "type": "value_error.emptykey",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_too_short_key(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/cipher",
                json=bad_content("Test", "T"),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is too short. Please give a string with more than one character.",
                    "type": "value_error.tooshortkey",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_bad_not_alpha_str_key(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/cipher",
                json=bad_content("Test", "+t"),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key '+t' is invalid. Please give a string.",
                    "type": "value_error.badkey",
                },
            ]


class IntegrationDecipherSuite:
    @staticmethod
    @pytest.mark.integration_test()
    def test_with_str_lower_key(server: str) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="ct",
        )

        response = requests.post(
            url=server + "/api/v2/vigenere/decipher",
            json=json_data(vigenere_input),
            timeout=1,
        )

        assert response is not None

        data = response.json()
        assert data is not None

        deciphered_vigenere = VigenereData.parse_obj(data)

        assert deciphered_vigenere.key == vigenere_input.key
        assert deciphered_vigenere.content == "Rlqa"

    @staticmethod
    @pytest.mark.integration_test()
    def test_with_str_upper_key(server: str) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="CT",
        )

        response = requests.post(
            url=server + "/api/v2/vigenere/decipher",
            json=json_data(vigenere_input),
            timeout=1,
        )

        assert response is not None

        data = response.json()
        assert data is not None

        deciphered_vigenere = VigenereData.parse_obj(data)

        assert deciphered_vigenere.key == vigenere_input.key
        assert deciphered_vigenere.content == "Rlqa"

    @staticmethod
    @pytest.mark.integration_test()
    def test_with_str_mixed_key(server: str) -> None:
        vigenere_input = VigenereData(
            content="Test",
            key="Ct",
        )

        response = requests.post(
            url=server + "/api/v2/vigenere/decipher",
            json=json_data(vigenere_input),
            timeout=1,
        )

        assert response is not None

        data = response.json()
        assert data is not None

        deciphered_vigenere = VigenereData.parse_obj(data)

        assert deciphered_vigenere.key == vigenere_input.key
        assert deciphered_vigenere.content == "Rlqa"

    @staticmethod
    @pytest.mark.integration_test()
    def test_equality_between_keys(server: str) -> None:
        vigenere_input1 = VigenereData(
            content="Test",
            key="ct",
        )

        response1 = requests.post(
            url=server + "/api/v2/vigenere/decipher",
            json=json_data(vigenere_input1),
            timeout=1,
        )

        assert response1 is not None

        data1 = response1.json()
        assert data1 is not None

        deciphered_vigenere1 = VigenereData.parse_obj(data1)

        assert deciphered_vigenere1.key == vigenere_input1.key
        assert deciphered_vigenere1.content == "Rlqa"

        vigenere_input2 = VigenereData(
            content="Test",
            key="cT",
        )

        response2 = requests.post(
            url=server + "/api/v2/vigenere/decipher",
            json=json_data(vigenere_input2),
            timeout=1,
        )

        assert response2 is not None

        data2 = response2.json()
        assert data2 is not None

        deciphered_vigenere2 = VigenereData.parse_obj(data2)

        assert deciphered_vigenere2.key == vigenere_input2.key
        assert deciphered_vigenere2.content == "Rlqa"

        vigenere_input3 = VigenereData(
            content="Test",
            key="CT",
        )

        response3 = requests.post(
            url=server + "/api/v2/vigenere/decipher",
            json=json_data(vigenere_input3),
            timeout=1,
        )

        assert response3 is not None

        data3 = response3.json()
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
        @pytest.mark.integration_test()
        def test_missing_content(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/decipher",
                json={"key": "tt"},
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_missing_key(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/decipher",
                json={"content": "test"},
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "field required",
                    "type": "value_error.missing",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_bad_type_content(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/decipher",
                json=bad_content(254, "tt"),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "The content is 'int'. Please give a string.",
                    "type": "type_error.contenttype",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_bad_empty_content(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/decipher",
                json=bad_content("", "tt"),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["content"],
                    "msg": "The content is empty. Please give a not empty string.",
                    "type": "value_error.emptycontent",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_bad_type_key(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/decipher",
                json=bad_content("Test", 25.8),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is 'float'. Please give a string.",
                    "type": "type_error.keytype",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_bad_empty_key(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/decipher",
                json=bad_content("Test", ""),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is empty. Please give a one character string or an integer.",
                    "type": "value_error.emptykey",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_too_short_key(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/decipher",
                json=bad_content("Test", "T"),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key is too short. Please give a string with more than one character.",
                    "type": "value_error.tooshortkey",
                },
            ]

        @staticmethod
        @pytest.mark.integration_test()
        def test_bad_not_alpha_str_key(server: str) -> None:
            response = requests.post(
                url=server + "/api/v2/vigenere/decipher",
                json=bad_content("Test", "+t"),
                timeout=1,
            )

            assert response is not None

            data = response.json()
            assert data is not None

            assert data == [
                {
                    "loc": ["key"],
                    "msg": "The key '+t' is invalid. Please give a string.",
                    "type": "value_error.badkey",
                },
            ]
