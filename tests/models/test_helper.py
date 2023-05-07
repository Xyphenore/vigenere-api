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

"""Model helper tests."""

import pytest

from vigenere_api.models.helpers import convert_key, move_char
from vigenere_api.models.helpers.errors import (
    BadKeyError,
    EmptyKeyError,
    HelperBadCharValueError,
    HelperBadFirstLetterValueError,
    HelperBadLengthCharValueError,
    HelperCharTypeError,
    HelperFirstLetterTypeError,
    HelperKeyTypeError,
    KeyTypeError,
    TooLongKeyError,
)


class MoveCharSuite:
    @staticmethod
    def test_move_lower_letter() -> None:
        moved_letter = move_char("a", 2, "a")

        assert moved_letter == "c"

    @staticmethod
    def test_move_upper_letter() -> None:
        moved_letter = move_char("A", 2, "A")

        assert moved_letter == "C"

    @staticmethod
    @pytest.mark.raises(exception=HelperCharTypeError)
    def test_bad_type_char() -> None:
        _ignored = move_char(b"r", 2, "a")

    @staticmethod
    @pytest.mark.raises(exception=HelperBadLengthCharValueError)
    def test_bad_length_char() -> None:
        _ignored = move_char("rr", 2, "a")

    @staticmethod
    @pytest.mark.raises(exception=HelperBadCharValueError)
    def test_bad_alpha_char() -> None:
        _ignored = move_char("+", 2, "a")

    @staticmethod
    @pytest.mark.raises(exception=HelperKeyTypeError)
    def test_bad_type_key() -> None:
        _ignored = move_char("a", "v", "a")

    @staticmethod
    @pytest.mark.raises(exception=HelperFirstLetterTypeError)
    def test_bad_type_first_letter() -> None:
        _ignored = move_char("a", 2, b"a")

    @staticmethod
    @pytest.mark.raises(exception=HelperBadFirstLetterValueError)
    def test_bad_first_letter_value() -> None:
        _ignored = move_char("a", 2, "g")


class ConvertKeySuite:
    @staticmethod
    def test_convert_lower_key() -> None:
        lower_index = convert_key("a")
        assert lower_index == 0

    @staticmethod
    def test_convert_upper_key() -> None:
        upper_index = convert_key("A")
        assert upper_index == 0

    @staticmethod
    @pytest.mark.raises(exception=KeyTypeError)
    def test_bad_type_key() -> None:
        _ignored = convert_key(b"ter")

    @staticmethod
    @pytest.mark.raises(exception=BadKeyError)
    def test_bad_key() -> None:
        _ignored = convert_key("8")

    @staticmethod
    @pytest.mark.raises(exception=EmptyKeyError)
    def test_empty_key() -> None:
        _ignored = convert_key("")

    @staticmethod
    @pytest.mark.raises(exception=TooLongKeyError)
    def test_too_long_key() -> None:
        _ignored = convert_key("aa")
