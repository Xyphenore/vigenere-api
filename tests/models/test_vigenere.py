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

"""Vigenere model tests."""

import pytest
from pydantic import ValidationError

from vigenere_api.models import VigenereData
from vigenere_api.models.errors import (
    AlgorithmKeyTypeError,
    AlgorithmOperationTypeError,
    AlgorithmTextTypeError,
)
from vigenere_api.models.vigenere import VigenereKey, VigenereOperation


class CtorSuite:
    @staticmethod
    def test_with_key() -> None:
        text = "Test"
        key = "zz"
        data = VigenereData(content=text, key=key)

        assert data.content == text
        assert data.key == key

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_missing_content() -> None:
        key = "zz"
        _ignored_data = VigenereData(key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_missing_key() -> None:
        text = "z"
        _ignored_data = VigenereData(content=text)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_type_content() -> None:
        text = b"Test"
        key = "zz"
        _ignored_data = VigenereData(content=text, key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_empty_content() -> None:
        text = ""
        key = "zz"
        _ignored_data = VigenereData(content=text, key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_type_key() -> None:
        text = "Test"
        key = b"z"
        _ignored_data = VigenereData(content=text, key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_empty_key() -> None:
        text = "Test"
        key = ""
        _ignored_data = VigenereData(content=text, key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_too_short_key() -> None:
        text = "Test"
        key = "e"
        _ignored_data = VigenereData(content=text, key=key)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_not_alpha_str_key() -> None:
        text = "Test"
        key = "$z"
        _ignored_data = VigenereData(content=text, key=key)


class OperationSuite:
    class CipherSuite:
        class SimpleKeySuite:
            @staticmethod
            def test_with_str_lower_key() -> None:
                text = "Test"
                key = "bb"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                cipher = data.cipher()

                ciphered_text = "Uftu"
                assert cipher.content == ciphered_text
                assert cipher.key == key

            @staticmethod
            def test_with_str_upper_key() -> None:
                text = "Test"
                key = "BB"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                cipher = data.cipher()

                ciphered_text = "Uftu"
                assert cipher.content == ciphered_text
                assert cipher.key == key

            @staticmethod
            def test_with_str_mixed_key() -> None:
                text = "Test"
                key = "Bb"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                cipher = data.cipher()

                ciphered_text = "Uftu"
                assert cipher.content == ciphered_text
                assert cipher.key == key

            @staticmethod
            def test_equality_between_keys() -> None:
                text = "Test"
                data1 = VigenereData(content=text, key="Bb")
                data2 = VigenereData(content=text, key="bb")
                data3 = VigenereData(content=text, key="BB")

                ciphered1 = data1.cipher()
                ciphered2 = data2.cipher()
                ciphered3 = data3.cipher()

                assert data1.content == data2.content == data3.content
                assert ciphered1.content == ciphered2.content == ciphered3.content

        class ComplexKeySuite:
            @staticmethod
            def test_with_str_lower_key() -> None:
                text = "Test"
                key = "abcd"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                cipher = data.cipher()

                ciphered_text = "Tfuw"
                assert cipher.content == ciphered_text
                assert cipher.key == key

            @staticmethod
            def test_with_str_upper_key() -> None:
                text = "Test"
                key = "ABCD"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                cipher = data.cipher()

                ciphered_text = "Tfuw"
                assert cipher.content == ciphered_text
                assert cipher.key == key

            @staticmethod
            def test_with_str_mixed_key() -> None:
                text = "Test"
                key = "aBcD"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                cipher = data.cipher()

                ciphered_text = "Tfuw"
                assert cipher.content == ciphered_text
                assert cipher.key == key

            @staticmethod
            def test_equality_between_keys() -> None:
                text = "Test"
                data1 = VigenereData(content=text, key="aBcD")
                data2 = VigenereData(content=text, key="abcd")
                data3 = VigenereData(content=text, key="ABCD")

                ciphered1 = data1.cipher()
                ciphered2 = data2.cipher()
                ciphered3 = data3.cipher()

                assert data1.content == data2.content == data3.content
                assert ciphered1.content == ciphered2.content == ciphered3.content

    class DecipherSuite:
        class SimpleKeySuite:
            @staticmethod
            def test_with_str_lower_key() -> None:
                text = "Test"
                key = "bb"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                decipher = data.decipher()

                deciphered_text = "Sdrs"
                assert decipher.content == deciphered_text
                assert decipher.key == key

            @staticmethod
            def test_with_str_upper_key() -> None:
                text = "Test ui"
                key = "BB"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                decipher = data.decipher()

                deciphered_text = "Sdrs th"
                assert decipher.content == deciphered_text
                assert decipher.key == key

            @staticmethod
            def test_with_str_mixed_key() -> None:
                text = "Test ui"
                key = "Bb"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                decipher = data.decipher()

                deciphered_text = "Sdrs th"
                assert decipher.content == deciphered_text
                assert decipher.key == key

            @staticmethod
            def test_equality_between_keys() -> None:
                text = "Test"
                data1 = VigenereData(content=text, key="Bb")
                data2 = VigenereData(content=text, key="bb")
                data3 = VigenereData(content=text, key="BB")

                deciphered1 = data1.decipher()
                deciphered2 = data2.decipher()
                deciphered3 = data3.decipher()

                assert data1.content == data2.content == data3.content
                assert deciphered1.content == deciphered2.content == deciphered3.content

        class ComplexKeySuite:
            @staticmethod
            def test_with_str_lower_key() -> None:
                text = "Test"
                key = "abcd"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                decipher = data.decipher()

                deciphered_text = "Tdqq"
                assert decipher.content == deciphered_text
                assert decipher.key == key

            @staticmethod
            def test_with_str_upper_key() -> None:
                text = "Test ui"
                key = "ABCD"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                decipher = data.decipher()

                deciphered_text = "Tdqq uh"
                assert decipher.content == deciphered_text
                assert decipher.key == key

            @staticmethod
            def test_with_str_mixed_key() -> None:
                text = "Test ui"
                key = "aBcD"
                data = VigenereData(content=text, key=key)

                assert data.content == text
                assert data.key == key

                decipher = data.decipher()

                deciphered_text = "Tdqq uh"
                assert decipher.content == deciphered_text
                assert decipher.key == key

            @staticmethod
            def test_equality_between_keys() -> None:
                text = "Test"
                data1 = VigenereData(content=text, key="aBcD")
                data2 = VigenereData(content=text, key="abcd")
                data3 = VigenereData(content=text, key="ABCD")

                deciphered1 = data1.decipher()
                deciphered2 = data2.decipher()
                deciphered3 = data3.decipher()

                assert data1.content == data2.content == data3.content
                assert deciphered1.content == deciphered2.content == deciphered3.content


class InternalSuite:
    class AlgorithmSuite:
        algo_func = VigenereData._VigenereData__algorithm

        @classmethod
        @pytest.mark.raises(exception=AlgorithmKeyTypeError)
        def test_with_bad_key(cls) -> None:
            _ignored = cls.algo_func("test", "A", VigenereOperation.CIPHER)

        @classmethod
        @pytest.mark.raises(exception=AlgorithmTextTypeError)
        def test_with_bad_text(cls) -> None:
            _ignored = cls.algo_func(b"test", 10, VigenereOperation.DECIPHER)

        @classmethod
        @pytest.mark.raises(exception=AlgorithmOperationTypeError)
        def test_with_bad_operation(cls) -> None:
            _ignored = cls.algo_func("test", VigenereKey("test"), b"CIPEHR")

        @classmethod
        def test_cipher(cls) -> None:
            ciphered_text = cls.algo_func(
                "teSt uio", VigenereKey("test"), VigenereOperation.CIPHER
            )

            assert ciphered_text == "miKm nmg"

        @classmethod
        def test_decipher(cls) -> None:
            ciphered_text = cls.algo_func(
                "teSt uio", VigenereKey("test"), VigenereOperation.DECIPHER
            )

            assert ciphered_text == "aaAa bew"
