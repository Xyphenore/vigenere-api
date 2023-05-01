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

from vigenere_api.models.helper import move_char
from vigenere_api.models.helper.errors import (
    HelperBadCharValueError,
    HelperBadFirstLetterValueError,
    HelperBadLengthCharValueError,
    HelperCharTypeError,
    HelperFirstLetterTypeError,
    HelperKeyTypeError,
)


def test_move_lower_letter() -> None:
    moved_letter = move_char("a", 2, "a")

    assert moved_letter == "c"


def test_move_upper_letter() -> None:
    moved_letter = move_char("A", 2, "A")

    assert moved_letter == "C"


@pytest.mark.raises(exception=HelperCharTypeError)
def test_bad_type_char() -> None:
    _ignored = move_char(b"r", 2, "a")


@pytest.mark.raises(exception=HelperBadLengthCharValueError)
def test_bad_length_char() -> None:
    _ignored = move_char("rr", 2, "a")


@pytest.mark.raises(exception=HelperBadCharValueError)
def test_bad_alpha_char() -> None:
    _ignored = move_char("+", 2, "a")


@pytest.mark.raises(exception=HelperKeyTypeError)
def test_bad_type_key() -> None:
    _ignored = move_char("a", "v", "a")


@pytest.mark.raises(exception=HelperFirstLetterTypeError)
def test_bad_type_first_letter() -> None:
    _ignored = move_char("a", 2, b"a")


@pytest.mark.raises(exception=HelperBadFirstLetterValueError)
def test_bad_first_letter_value() -> None:
    _ignored = move_char("a", 2, "g")
