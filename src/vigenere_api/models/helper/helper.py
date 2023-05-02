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

"""Helpers for models."""

from typing import Literal

from .errors import HelperBadCharValueError
from .errors import HelperBadFirstLetterValueError
from .errors import HelperBadLengthCharValueError
from .errors import HelperCharTypeError
from .errors import HelperFirstLetterTypeError
from .errors import HelperKeyTypeError


def move_char(char: str, key: int, first_letter: Literal["a", "A"]) -> str:
    """
    Move the character to the right.

    Parameters
    ----------
    char : str
        The character to move.
    key : int
        The key to moving the character.
    first_letter : {a, A}
        The first letter of alphabetic in uppercase or lowercase.

    Raises
    ------
    HelperCharTypeError
        Thrown if 'char' is not a string.
    HelperBadLengthCharValueError
        Thrown if 'char' has not a length equals to 1.
    HelperBadCharValueError
        Thrown if 'char' is not an alphabetic character.
    HelperKeyTypeError
        Thrown if 'key' is not an integer.
    HelperFirstLetterTypeError
        Thrown if 'first_letter' is not a string.
    HelperBadFirstLetterValueError
        Thrown if 'first_letter' is not “A” or "a".

    Returns
    -------
    str
        The moved character.
    """

    if not isinstance(char, str):
        raise HelperCharTypeError(char)

    if len(char) != 1:
        raise HelperBadLengthCharValueError(char)

    if not char.isalpha():
        raise HelperBadCharValueError(char)

    if not isinstance(key, int):
        raise HelperKeyTypeError(key)

    if not isinstance(first_letter, str):
        raise HelperFirstLetterTypeError(first_letter)

    if first_letter not in ("a", "A"):
        raise HelperBadFirstLetterValueError(first_letter)

    return chr((ord(char) - ord(first_letter) + key) % 26 + ord(first_letter))
