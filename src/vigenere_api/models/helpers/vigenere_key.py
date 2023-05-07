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

"""Utils class for VigenereData."""

from typing import final, Final

from .errors import (
    BadKeyError,
    EmptyKeyError,
    ExpectedKeyType,
    KeyTypeError,
    TooShortKeyError,
)


@final
class VigenereKey:
    """Util class to loop on each character of the key."""

    def __init__(self, key: str) -> None:
        """
        Create a new Vigenere key.

        Parameters
        ----------
        key : str
            The string used like a key.

        Raises
        ------
        KeyTypeError
            Thrown if 'key' is not a string.
        EmptyKeyError
            Thrown if 'key' is empty.
        TooShortKeyError
            Thrown if 'key' is too short.
        BadKeyError
            Thrown if 'key' contains invalid characters.
        """

        if not isinstance(key, str):
            raise KeyTypeError(key, ExpectedKeyType.STRING)

        if len(key) == 0:
            raise EmptyKeyError

        if len(key) == 1:
            raise TooShortKeyError

        if not key.isalpha():
            raise BadKeyError(key, ExpectedKeyType.STRING)

        self.__index = 0
        self.__key: Final = key

    def __next__(self) -> str:
        """
        Get the next character of the key.

        Returns
        -------
        The next character of the key.
            str
        """
        try:
            return self.__key[self.__index]
        finally:
            self.__increase_index()

    def __increase_index(self) -> None:
        """Increase the index of the key."""
        self.__index += 1
        self.__index %= len(self)

    def __len__(self) -> int:
        """
        Get the length of the key.

        Returns
        -------
        int
            The length of the key.
        """
        return len(self.__key)
