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

from typing import final, Union

from pydantic import StrictInt, StrictStr, validator

from vigenere_api.helpers import Model
from .errors import (
    AlgorithmExpectedKeyType,
    AlgorithmKeyTypeError,
    AlgorithmTextTypeError,
    ContentTypeError,
    EmptyContentError,
)
from .helpers import convert_key, move_char
from .helpers.errors import (
    BadKeyError,
    EmptyKeyError,
    ExpectedKeyType,
    KeyTypeError,
    TooLongKeyError,
)

Key = Union[StrictInt, StrictStr]


@final
class CaesarData(Model):
    """
    Caesar data to cipher the content or decipher.

    Exemples
    --------
    Basic example

    >>> from vigenere_api.models import CaesarData

    >>> caesar_data = CaesarData(content="Hello World", key=1)

    >>> ciphered_data = caesar_data.cipher()
    >>> deciphered_data = caesar_data.decipher()

    >>> assert caesar_data == deciphered_data == "Hello World"
    >>> assert caesar_data.key == ciphered_data.key == deciphered_data.key == 1
    """

    content: StrictStr
    """The content to be ciphered or deciphered."""

    key: Key
    """The key to cipher or decipher the content."""

    def cipher(self) -> CaesarData:
        """
        Cipher the content with the key.

        Returns
        -------
        ciphered_data
            CaesarData
        """
        return CaesarData(
            content=self.__algorithm(self.content, self.__convert_key()),
            key=self.key,
        )

    def decipher(self) -> CaesarData:
        """
        Decipher the content with the key.

        Returns
        -------
        deciphered_data
            CaesarData
        """
        return CaesarData(
            content=self.__algorithm(self.content, -self.__convert_key()),
            key=self.key,
        )

    @staticmethod
    def __algorithm(text: str, key: int) -> str:
        """
        Apply the common algorithm for Caesar.

        Parameters
        ----------
        text : str
            The text to apply the algorithm.
        key : int
            The key used by the algorithm.
            The key moves each alphabet character in text.

        Raises
        ------
        AlgorithmTextTypeError
            Thrown if 'text' is not a string.
        AlgorithmKeyTypeError
            Thrown if 'key' is not an integer.

        Returns
        -------
        converted_text
            str
        """
        if not isinstance(text, str):
            raise AlgorithmTextTypeError(text)

        if not isinstance(key, int):
            raise AlgorithmKeyTypeError(key, AlgorithmExpectedKeyType.INTEGER)

        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += move_char(char, key, "A")
                else:
                    result += move_char(char, key, "a")
            else:
                result += char

        return result

    def __convert_key(self) -> int:
        """
        Convert the key to int.

        Returns
        -------
        int_key
            int
        """
        if isinstance(self.key, int):
            return self.key

        return convert_key(self.key)

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
    def validate_key(cls, key: Key) -> Key:
        """
        Check if the affectation to key respects contraints.

        Parameters
        ----------
        key : Key
            The new key.

        Raises
        ------
        KeyTypeError
            Thrown if 'key' is not an integer and not a string.
        EmptyKeyError
            Thrown if 'key' is an empty string.
        TooLongKeyError
            Thrown if 'key' is a string with a length longer than 1.
        BadKeyError
            Thrown if 'key' is not an alphabetic character.

        Returns
        -------
        key
            Key
        """
        if not isinstance(key, (str, int)):
            raise KeyTypeError(key, ExpectedKeyType.STRING_OR_INTEGER)

        if isinstance(key, str):
            if len(key) == 0:
                raise EmptyKeyError

            if len(key) > 1:
                raise TooLongKeyError

            if not key.isalpha():
                raise BadKeyError(key, ExpectedKeyType.STRING_OR_INTEGER)

        return key
