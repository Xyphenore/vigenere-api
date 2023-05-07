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

"""All errors thrown by the caesar and vigenere model."""

from enum import auto, unique
from typing import Any, final

from strenum import LowercaseStrEnum
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
class EmptyContentError(ValueError):
    """Thrown if the content is empty."""

    def __init__(self) -> None:
        """Create an EmptyContentError."""
        super().__init__(
            "The content is empty. Please give a not empty string.",
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
@unique
class AlgorithmExpectedKeyType(LowercaseStrEnum):
    """The type of key, the algorithm needs it."""

    STRING = auto()
    INTEGER = auto()
    VIGENERE_KEY = "VigenereKey"


@final
class AlgorithmKeyTypeError(VigenereAPITypeError):
    """Thrown if the algorithm receives a bad type for the key variable."""

    def __init__(self, key: Any, expected_type: AlgorithmExpectedKeyType) -> None:
        """
        Create an AlgorithmKeyTypeError with the key.

        Parameters
        ----------
        key : Any
            The given key.
        expected_type : AlgorithmExpectedKeyType
            The expected type of the key.
        """
        expected = f"a {expected_type}"
        if expected_type == AlgorithmExpectedKeyType.INTEGER:
            expected = f"an {expected_type}"
        elif expected_type == AlgorithmExpectedKeyType.VIGENERE_KEY:
            expected += " object"

        super().__init__(key, "key variable", expected)


@final
class AlgorithmOperationTypeError(VigenereAPITypeError):
    """Thrown if the operation is not a VigenereOperation object."""

    def __init__(self, operation: Any) -> None:
        """
        Create an AlgorithmOperationTypeError with the operation.

        Parameters
        ----------
        operation : Any
        """
        super().__init__(operation, "operation", "a VigenereOperation object")
