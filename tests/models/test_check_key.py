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

from vigenere_api.models.helpers.check_key import check_key
from vigenere_api.models.helpers.errors import BadKeyError, EmptyKeyError, KeyTypeError


def test_with_key() -> None:
    key = "zz"
    check_key(key)


@pytest.mark.raises(exception=KeyTypeError)
def test_bad_type_key() -> None:
    key = b"z"
    check_key(key)


@pytest.mark.raises(exception=EmptyKeyError)
def test_bad_empty_key() -> None:
    key = ""
    check_key(key)


@pytest.mark.raises(exception=BadKeyError)
def test_bad_not_alpha_str_key() -> None:
    key = "$z"
    check_key(key)
