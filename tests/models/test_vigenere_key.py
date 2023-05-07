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

import pytest

from vigenere_api.models.helpers.errors import (
    BadKeyError,
    EmptyKeyError,
    KeyTypeError,
    TooShortKeyError,
)
from vigenere_api.models.vigenere import VigenereKey


class CtorSuite:
    @staticmethod
    def test_with_key() -> None:
        key = "zz"
        data = VigenereKey(key)

        assert data._VigenereKey__key == key
        assert len(data) == len(key)

    @staticmethod
    @pytest.mark.raises(exception=KeyTypeError)
    def test_bad_type_key() -> None:
        key = b"z"
        _ignored_data = VigenereKey(key)

    @staticmethod
    @pytest.mark.raises(exception=EmptyKeyError)
    def test_bad_empty_key() -> None:
        key = ""
        _ignored_data = VigenereKey(key)

    @staticmethod
    @pytest.mark.raises(exception=TooShortKeyError)
    def test_too_short_key() -> None:
        key = "e"
        _ignored_data = VigenereKey(key)

    @staticmethod
    @pytest.mark.raises(exception=BadKeyError)
    def test_bad_not_alpha_str_key() -> None:
        key = "$z"
        _ignored_data = VigenereKey(key)


def test_next() -> None:
    key = "abcd"
    data = VigenereKey(key)

    assert data._VigenereKey__key == key
    assert len(data) == len(key)

    for char in key:
        assert next(data) == char

    assert next(data) == key[0]


def test_increase_index() -> None:
    key = "abcd"
    data = VigenereKey(key)

    assert data._VigenereKey__key == key
    assert len(data) == len(key)

    assert data._VigenereKey__index == 0
    data._VigenereKey__increase_index()
    assert data._VigenereKey__index == 1

    for _ in range(len(data)):
        data._VigenereKey__increase_index()

    assert data._VigenereKey__index == 1
