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

from vigenere_api.models.helpers import convert_key
from vigenere_api.models.helpers.errors import (
    BadKeyError,
    EmptyKeyError,
    KeyTypeError,
    TooLongKeyError,
)


def test_convert_lower_key() -> None:
    lower_index = convert_key("a")
    assert lower_index == 0


def test_convert_upper_key() -> None:
    upper_index = convert_key("A")
    assert upper_index == 0


@pytest.mark.raises(exception=KeyTypeError)
def test_bad_type_key() -> None:
    _ignored = convert_key(b"ter")


@pytest.mark.raises(exception=BadKeyError)
def test_bad_key() -> None:
    _ignored = convert_key("8")


@pytest.mark.raises(exception=EmptyKeyError)
def test_empty_key() -> None:
    _ignored = convert_key("")


@pytest.mark.raises(exception=TooLongKeyError)
def test_too_long_key() -> None:
    _ignored = convert_key("aa")
