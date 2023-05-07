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

"""Caesar model."""

from __future__ import annotations

from enum import auto, unique
from typing import final

from pydantic import StrictStr, validator

from strenum import StrEnum
from vigenere_api.helpers import Model
from .errors import (
    AlgorithmExpectedKeyType,
    AlgorithmKeyTypeError,
    AlgorithmOperationTypeError,
    AlgorithmTextTypeError,
    ContentTypeError,
    EmptyContentError,
)
from .helpers import convert_key, move_char, VigenereKey


@final
@unique
class VigenereOperation(StrEnum):
    """All possible Vigenere operations."""

    CIPHER = auto()
    DECIPHER = auto()


@final
class VigenereData(Model):
    """
    Vigenere data to cipher the content or decipher.

    Exemples
    --------
    Basic example

    >>> from vigenere_api.models import VigenereData

    >>> vigenere_data = VigenereData(content="Hello World", key="test")

    >>> ciphered_data = vigenere_data.cipher()
    >>> deciphered_data = vigenere_data.decipher()

    >>> assert vigenere_data == deciphered_data == "Hello World"
    >>> assert vigenere_data.key == ciphered_data.key == deciphered_data.key == "test"
    """

    content: StrictStr
    """The content to be ciphered or deciphered."""

    key: StrictStr
    """The key to cipher or decipher the content."""

    def cipher(self) -> VigenereData:
        """
        Cipher the content with the key.

        Returns
        -------
        ciphered_data
            VigenereData
        """
        return VigenereData(
            content=self.__algorithm(
                self.content,
                VigenereKey(self.key),
                VigenereOperation.CIPHER,
            ),
            key=self.key,
        )

    def decipher(self) -> VigenereData:
        """
        Decipher the content with the key.

        Returns
        -------
        deciphered_data
            VigenereData
        """
        return VigenereData(
            content=self.__algorithm(
                self.content,
                VigenereKey(self.key),
                VigenereOperation.DECIPHER,
            ),
            key=self.key,
        )

    @staticmethod
    def __algorithm(text: str, key: VigenereKey, operation: VigenereOperation) -> str:
        """
        Apply the common algorithm for Vigenere.

        Parameters
        ----------
        text : str
            The text to apply the algorithm.
        key : VigenereKey
            The key used by the algorithm.
        operation : VigenereOperation
            The wanted operation.

        Raises
        ------
        AlgorithmTextTypeError
            Thrown if 'text' is not a string.
        AlgorithmKeyTypeError
            Thrown if 'key' is not a VigenereKey object.
        AlgorithmOperationTypeError
            Thrown if 'operation' is not a VigenereOperation object.

        Returns
        -------
        converted_text
            str
        """
        if not isinstance(text, str):
            raise AlgorithmTextTypeError(text)

        if not isinstance(key, VigenereKey):
            raise AlgorithmKeyTypeError(key, AlgorithmExpectedKeyType.VIGENERE_KEY)

        if not isinstance(operation, VigenereOperation):
            raise AlgorithmOperationTypeError(operation)

        result = ""
        for char in text:
            if char.isalpha():
                index_key = convert_key(next(key))
                if operation == VigenereOperation.DECIPHER:
                    index_key = -index_key

                if char.isupper():
                    result += move_char(char, index_key, "A")
                else:
                    result += move_char(char, index_key, "a")
            else:
                result += char

        return result

    @validator("content", pre=True)
    def validate_content(cls, content: str) -> str:
        """
        Check if the affectation to content respects contraints.

        Parameters
        ----------
        content : str
            The new content.

        Raises
        ------
        ContentTypeError
            Thrown if 'content' is not a string.
        EmptyContentError
            Thrown if 'content' is an empty string.

        Returns
        -------
        content
            str
        """
        if not isinstance(content, str):
            raise ContentTypeError(content)

        if len(content) == 0:
            raise EmptyContentError

        return content

    @validator("key", pre=True)
    def validate_key(cls, key: str) -> str:
        """
        Check if the affectation to key respects contraints.

        Parameters
        ----------
        key : str
            The new key.

        Raises
        ------
        KeyTypeError
            Thrown if 'key' is not a string.
        EmptyKeyError
            Thrown if 'key' is an empty string.
        TooShortKeyError
            Thrown if 'key' is a string with a length of 1.
        BadKeyError
            Thrown if 'key' is not an alphabetic character.

        Returns
        -------
        key
            str
        """
        _key_can_be_instantiate = VigenereKey(key)

        return key
