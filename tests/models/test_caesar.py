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

"""Caesar model tests."""

import pytest
from pydantic import ValidationError

from vigenere_api.models.caesar import CaesarData
from vigenere_api.models.errors import AlgorithmKeyTypeError, AlgorithmTextTypeError


class CtorSuite:
    @staticmethod
    def test_with_int_key() -> None:
        text = "Test"
        key = 1
        data = CaesarData(content=text, key=key)

        assert data.content == text
        assert data.key == key

    @staticmethod
    def test_with_str_key() -> None:
        text = "Test"
        key = "z"
        data = CaesarData(content=text, key=key)

        assert data.content == text
        assert data.key == key

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_type_content() -> None:
        text = b"Test"
        key = "z"
        _ignored_data = CaesarData(content=text, key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_empty_content() -> None:
        text = ""
        key = "z"
        _ignored_data = CaesarData(content=text, key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_type_key() -> None:
        text = "Test"
        key = b"z"
        _ignored_data = CaesarData(content=text, key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_empty_key() -> None:
        text = "Test"
        key = ""
        _ignored_data = CaesarData(content=text, key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_too_long_key() -> None:
        text = "Test"
        key = "ert"
        _ignored_data = CaesarData(content=text, key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_not_alpha_str_key() -> None:
        text = "Test"
        key = "$"
        _ignored_data = CaesarData(content=text, key=key)


class OperationSuite:
    class CipherSuite:
        @staticmethod
        def test_with_int_key() -> None:
            text = "Test"
            key = 1
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key

            cipher = data.cipher()

            ciphered_text = "Uftu"
            assert cipher.content == ciphered_text
            assert cipher.key == key

        @staticmethod
        def test_with_str_lower_key() -> None:
            text = "Test"
            key = "b"
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key

            cipher = data.cipher()

            ciphered_text = "Uftu"
            assert cipher.content == ciphered_text
            assert cipher.key == key

        @staticmethod
        def test_with_str_upper_key() -> None:
            text = "Test"
            key = "B"
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key

            cipher = data.cipher()

            ciphered_text = "Uftu"
            assert cipher.content == ciphered_text
            assert cipher.key == key

        @staticmethod
        def test_equality_between_keys() -> None:
            text = "Test"
            data1 = CaesarData(content=text, key=1)
            data2 = CaesarData(content=text, key="b")
            data3 = CaesarData(content=text, key="B")

            ciphered1 = data1.cipher()
            ciphered2 = data2.cipher()
            ciphered3 = data3.cipher()

            assert data1.content == data2.content == data3.content
            assert ciphered1.content == ciphered2.content == ciphered3.content

        @staticmethod
        def test_with_negative_int_key() -> None:
            text = "Test"
            key = -1
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key

            cipher = data.cipher()

            deciphered_text = "Sdrs"
            assert cipher.content == deciphered_text
            assert cipher.key == key

    class DecipherSuite:
        @staticmethod
        def test_with_int_key() -> None:
            text = "Test"
            key = 1
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key

            decipher = data.decipher()

            deciphered_text = "Sdrs"
            assert decipher.content == deciphered_text
            assert decipher.key == key

        @staticmethod
        def test_with_str_lower_key() -> None:
            text = "Test"
            key = "b"
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key

            decipher = data.decipher()

            deciphered_text = "Sdrs"
            assert decipher.content == deciphered_text
            assert decipher.key == key

        @staticmethod
        def test_with_str_upper_key() -> None:
            text = "Test ui"
            key = "B"
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key

            decipher = data.decipher()

            deciphered_text = "Sdrs th"
            assert decipher.content == deciphered_text
            assert decipher.key == key

        @staticmethod
        def test_equality_between_keys() -> None:
            text = "Test"
            data1 = CaesarData(content=text, key=1)
            data2 = CaesarData(content=text, key="b")
            data3 = CaesarData(content=text, key="B")

            deciphered1 = data1.decipher()
            deciphered2 = data2.decipher()
            deciphered3 = data3.decipher()

            assert data1.content == data2.content == data3.content
            assert deciphered1.content == deciphered2.content == deciphered3.content

        @staticmethod
        def test_with_negative_int_key() -> None:
            text = "Test"
            key = -1
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key

            decipher = data.decipher()

            deciphered_text = "Uftu"
            assert decipher.content == deciphered_text
            assert decipher.key == key


class InternalSuite:
    class AlgorithmSuite:
        algo_func = CaesarData._CaesarData__algorithm

        @classmethod
        @pytest.mark.raises(exception=AlgorithmKeyTypeError)
        def test_with_bad_key(cls) -> None:
            _ignored = cls.algo_func("test", "A")

        @classmethod
        @pytest.mark.raises(exception=AlgorithmTextTypeError)
        def test_with_bad_test(cls) -> None:
            _ignored = cls.algo_func(b"test", 10)

        @classmethod
        def test_cipher(cls) -> None:
            ciphered_text = cls.algo_func("teSt", 2)

            assert ciphered_text == "vgUv"

        @classmethod
        def test_decipher(cls) -> None:
            ciphered_text = cls.algo_func("teSt", -2)

            assert ciphered_text == "rcQr"

    class ConvertKeySuite:
        @staticmethod
        def test_with_int_key() -> None:
            text = "Test"
            key = 1
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key
            assert data._CaesarData__convert_key() == key

        @staticmethod
        def test_with_str_lower_key() -> None:
            text = "Test"
            key = "z"
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key
            assert data._CaesarData__convert_key() == 25

        @staticmethod
        def test_with_str_upper_key() -> None:
            text = "Test"
            key = "Z"
            data = CaesarData(content=text, key=key)

            assert data.content == text
            assert data.key == key
            assert data._CaesarData__convert_key() == 25
