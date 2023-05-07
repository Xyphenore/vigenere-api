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

"""Base model."""

from __future__ import annotations

from pydantic import StrictStr, validator

from vigenere_api.helpers import Model

from .errors import ContentTypeError, EmptyContentError


class BaseData(Model):
    """Base data to verify the content."""

    content: StrictStr
    """The content to be ciphered or deciphered."""

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
