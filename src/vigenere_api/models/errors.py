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

from typing import Any
from typing import final

from vigenere_api.helpers import VigenereAPITypeError


@final
class ContentTypeError(VigenereAPITypeError):
    """Thrown if the content is not a string."""

    def __init__(self, content: Any) -> None:
        """
        Create a ContentTypeError with the content.

        Parameters
        ----------
        content : Any
            The received content.
        """
        super().__init__(content, "content", "a string")


@final
class KeyTypeError(VigenereAPITypeError):
    """Thrown if the key is not a string and not an integer."""

    def __init__(self, key: Any) -> None:
        """
        Create a KeyTypeError with the key.

        Parameters
        ----------
        key : Any
            The received key.
        """
        super().__init__(key, "key", "a string or an integer")


@final
class EmptyContentError(ValueError):
    """Thrown if the content is empty."""

    def __init__(self) -> None:
        """Create an EmptyContentError."""
        super().__init__(
            "The content is empty. Please give a not empty string.",
        )


@final
class EmptyKeyError(ValueError):
    """Thrown if the key is empty."""

    def __init__(self) -> None:
        """Create an EmptyKeyError."""
        super().__init__(
            "The key is empty. Please give a one character string or an integer.",
        )


@final
class TooLongKeyError(ValueError):
    """Thrown if the key is not an integer and not a one character string."""

    def __init__(self) -> None:
        """Create a TooLongKeyError."""
        super().__init__(
            "The key is too long. Please give a one character string or an integer.",
        )


@final
class BadKeyError(ValueError):
    """Thrown if the key is not an integer and not a one character string."""

    def __init__(self, key: str) -> None:
        """
        Create a BadKeyError with the key.

        Parameters
        ----------
        key : str
            The received key.
        """
        super().__init__(
            f"The key '{key}' is invalid."
            + " Please give an alphabetic one character string or an integer.",
        )


@final
class AlgorithmTextTypeError(VigenereAPITypeError):
    """Thrown if the algorithm receives a bad type for the text variable."""

    def __init__(self, text: Any) -> None:
        """
        Create an AlgorithmTextTypeError with the text.

        Parameters
        ----------
        text : Any
            The given text.
        """
        super().__init__(text, "text variable", "a string")


@final
class AlgorithmKeyTypeError(VigenereAPITypeError):
    """Thrown if the algorithm receives a bad type for the key variable."""

    def __init__(self, key: Any) -> None:
        """
        Create an AlgorithmKeyTypeError with the key.

        Parameters
        ----------
        key : Any
            The given key.
        """
        super().__init__(key, "key variable", "an integer")
