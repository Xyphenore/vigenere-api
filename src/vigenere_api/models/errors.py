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

"""All errors thrown by the caesar model."""

from typing import Any, final


@final
class ContentTypeError(TypeError):
    """Thrown if the content is not a string."""

    def __init__(self, content: Any) -> None:
        cls_name = type(content).__qualname__

        super().__init__(
            f"The content is '{cls_name}'. Please give a string.",
        )


@final
class KeyTypeError(TypeError):
    """Thrown if the key is not a string and not an integer."""

    def __init__(self, key: Any) -> None:
        cls_name = type(key).__qualname__

        super().__init__(
            f"The key is '{cls_name}'. Please give a string or an integer.",
        )


@final
class EmptyContentError(ValueError):
    """Thrown if the content is empty."""

    def __init__(self) -> None:
        super().__init__(
            "The content is empty. Please give a not empty string.",
        )


@final
class EmptyKeyError(ValueError):
    """Thrown if the key is empty."""

    def __init__(self) -> None:
        super().__init__(
            "The key is empty. Please give a one character string or an integer.",
        )


@final
class TooLongKeyError(ValueError):
    """Thrown if the key is not an integer and not a one character string."""

    def __init__(self) -> None:
        super().__init__(
            "The key is too long. Please give a one character string or an integer.",
        )


@final
class BadKeyError(ValueError):
    """Thrown if the key is not an integer and not a one character string."""

    def __init__(self, key: str) -> None:
        super().__init__(
            f"The key '{key}' is invalid."
            + " Please give an alphabetic one character string or an integer.",
        )


@final
class AlgorithmTextTypeError(TypeError):
    """Thrown if the algorithm receives a bad type for the text variable."""

    def __init__(self, text: Any) -> None:
        cls_name = type(text).__qualname__

        super().__init__(
            f"The text variable is '{cls_name}'. Please give a string.",
        )


@final
class AlgorithmKeyTypeError(TypeError):
    """Thrown if the algorithm receives a bad type for the key variable."""

    def __init__(self, key: Any) -> None:
        cls_name = type(key).__qualname__

        super().__init__(
            f"The key variable is '{cls_name}'. Please give an integer.",
        )
