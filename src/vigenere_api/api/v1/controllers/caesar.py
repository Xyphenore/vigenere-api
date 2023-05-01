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

"""The caesar controller."""

from typing import final

from blacksheep import FromJSON, Response
from blacksheep.server.controllers import APIController, post

from vigenere_api.api.v1.openapi_docs import docs
from vigenere_api.models import CaesarData
from .docs import post_caesar_cipher_docs, post_caesar_decipher_docs


@final
class CaesarController(APIController):
    """
    The caesar controller.

    Provides routes:
    - POST /api/v1/caesar/cipher
    - POST /api/v1/caesar/decipher
    """

    @classmethod
    def version(cls) -> str:
        """
        Version of the API.

        Returns
        -------
        version
            str
        """

        return "v1"

    @classmethod
    def class_name(cls) -> str:
        """
        Name of the class.

        Returns
        -------
        class_name
            str
        """

        return "caesar"

    @docs(post_caesar_cipher_docs)
    @post("cipher")
    async def cipher(self, data: FromJSON[CaesarData]) -> Response:
        """
        Cipher the input request with Caesar algorithm.

        Parameters
        ----------
        data : CaesarData
            A CaesarData from JSON from the request body.

        Returns
        -------
        response
            Response
        """

        return self.json(data.value.cipher())

    @docs(post_caesar_decipher_docs)
    @post("decipher")
    async def decipher(self, data: FromJSON[CaesarData]) -> Response:
        """
        Decipher the input request with Caesar algorithm.

        Parameters
        ----------
        data : CaesarData
            A CaesarData from JSON from the request body.

        Returns
        -------
        response
            Response
        """

        return self.json(data.value.decipher())
