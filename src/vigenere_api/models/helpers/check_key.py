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

"""Check if the key is good."""

from .errors import BadKeyError, EmptyKeyError, ExpectedKeyType, KeyTypeError


def check_key(key: str) -> None:
    """
    Check if the key is an alphabetic string and not empty.

    Parameters
    ----------
    key : str
        The key to check.

    Raises
    ------
    KeyTypeError
        Thrown if 'key' is not a string.
    EmptyKeyError
        Thrown if 'key' is empty.
    BadKeyError
        Thrown if 'key' is not an alphabetic string.
    """
    if not isinstance(key, str):
        raise KeyTypeError(key, ExpectedKeyType.STRING)

    if len(key) == 0:
        raise EmptyKeyError

    if not key.isalpha():
        raise BadKeyError(key, ExpectedKeyType.STRING)
