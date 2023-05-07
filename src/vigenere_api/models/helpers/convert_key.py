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

"""Convert a one character string into an integer between 0 and 25."""

from .check_key import check_key
from .errors import TooLongKeyError


def convert_key(key: str) -> int:
    """
    Convert the one character string into an integer between 0 and 25.

    Parameters
    ----------
    key : str
        The key to convert.

    Raises
    ------
    KeyTypeError
        Thrown if 'key' is not a string.
    EmptyKeyError
        Thrown if 'key' is an empty string.
    TooLongKeyError
        Thrown if 'key' is too long.
    BadKeyError
        Thrown if 'key' is not a one alphabetical character.

    Returns
    -------
    key_converted
        int
    """
    check_key(key)

    if len(key) > 1:
        raise TooLongKeyError

    return ord(key) - ord("A") if key.isupper() else ord(key) - ord("a")
