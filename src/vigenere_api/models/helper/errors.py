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


@final
class HelperCharTypeError(TypeError):
    """Thrown if the helper receives a bad type for the char variable."""

    def __init__(self, char: Any) -> None:
        cls_name = type(char).__qualname__

        super().__init__(
            f"The char variable is '{cls_name}'. Please give a string.",
        )


@final
class HelperBadLengthCharValueError(ValueError):
    """Thrown if the helper receives a char with a length different from 1."""

    def __init__(self, char: str) -> None:
        super().__init__(
            f"The helper function receives a char with a length of '{len(char)}'."
            + " Please give one character string.",
        )


@final
class HelperBadCharValueError(ValueError):
    """Thrown if the helper receives a char, which is not an alphabetical character."""

    def __init__(self, char: str) -> None:
        super().__init__(
            f"The helper function receives the char '{len(char)}'."
            + " Please give one alphabetical character string.",
        )


@final
class HelperKeyTypeError(TypeError):
    """Thrown if the algorithm receives a bad type for the key variable."""

    def __init__(self, key: Any) -> None:
        cls_name = type(key).__qualname__

        super().__init__(
            f"The key variable is '{cls_name}'. Please give an integer.",
        )


@final
class HelperFirstLetterTypeError(TypeError):
    """Thrown if the helper receives a bad type for the char variable."""

    def __init__(self, first_letter: Any) -> None:
        cls_name = type(first_letter).__qualname__

        super().__init__(
            f"The first letter variable is '{cls_name}'. Please give a string.",
        )


@final
class HelperBadFirstLetterValueError(ValueError):
    """Thrown if the helper receives a char with a length different from 1."""

    def __init__(self, first_letter: str) -> None:
        super().__init__(
            f"The helper function receives a first letter equals to '{first_letter}'."
            + " Please give a string in {'a', 'A'}.",
        )
