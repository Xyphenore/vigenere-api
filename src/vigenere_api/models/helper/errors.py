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

"""All errors thrown by the helper."""

from typing import Any
from typing import final

from vigenere_api.helpers import VigenereAPITypeError


@final
class HelperCharTypeError(VigenereAPITypeError):
    """Thrown if the helper receives a bad type for the char variable."""

    def __init__(self, char: Any) -> None:
        """
        Create a HelperCharTypeError with the received char.

        Parameters
        ----------
        char : Any
            The received char.
        """
        super().__init__(char, "char variable", "a string")


@final
class HelperBadLengthCharValueError(ValueError):
    """Thrown if the helper receives a char with a length different from 1."""

    def __init__(self, char: str) -> None:
        """
        Create a HelperBadLengthCharValueError with the received char.

        Parameters
        ----------
        char : str
        """
        super().__init__(
            f"The helper function receives a char with a length of '{len(char)}'."
            + " Please give one character string.",
        )


@final
class HelperBadCharValueError(ValueError):
    """Thrown if the helper receives a char, which is not an alphabetical character."""

    def __init__(self, char: str) -> None:
        """
        Create a HelperBadCharValueError with the received char.

        Parameters
        ----------
        char : str
        """
        super().__init__(
            f"The helper function receives the char '{len(char)}'."
            + " Please give one alphabetical character string.",
        )


@final
class HelperKeyTypeError(VigenereAPITypeError):
    """Thrown if the algorithm receives a bad type for the key variable."""

    def __init__(self, key: Any) -> None:
        """
        Create a HelperBadKeyTypeError with the received key.

        Parameters
        ----------
        key : Any
            The key.
        """
        super().__init__(key, "key variable", "an integer")


@final
class HelperFirstLetterTypeError(VigenereAPITypeError):
    """Thrown if the helper receives a bad type for the char variable."""

    def __init__(self, first_letter: Any) -> None:
        """
        Create a HelperBadFirstLetterTypeError with the received letter.

        Parameters
        ----------
        first_letter : Any
            The first letter.
        """
        super().__init__(first_letter, "first letter variable", "a string")


@final
class HelperBadFirstLetterValueError(ValueError):
    """Thrown if the helper receives a char with a length different from 1."""

    def __init__(self, first_letter: str) -> None:
        """
        Create a HelperBadFirstLetterValueError with the received letter.

        Parameters
        ----------
        first_letter : str
            The first letter.
        """
        super().__init__(
            f"The helper function receives a first letter equals to '{first_letter}'."
            + " Please give a string in {'a', 'A'}.",
        )
