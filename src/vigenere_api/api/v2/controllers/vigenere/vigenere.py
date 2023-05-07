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
from blacksheep.server.controllers import post

from vigenere_api.api.helpers import Controller
from vigenere_api.api.v2.openapi_docs import docs
from vigenere_api.models import VigenereData

from .docs import post_vigenere_cipher_docs, post_vigenere_decipher_docs


@final
class VigenereController(Controller):
    """
    The vigenere controller.

    Provides routes:
    - POST /api/v2/vigenere/cipher
    - POST /api/v2/vigenere/decipher
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
        return f"v{docs.version.major}"

    @docs(post_vigenere_cipher_docs)
    @post("cipher")
    async def cipher(self, data: FromJSON[VigenereData]) -> Response:
        """
        Cipher the input request with Vigenere algorithm.

        Parameters
        ----------
        data : VigenereData
            A VigenereData from JSON from the request body.

        Returns
        -------
        response
            Response
        """
        return self.json(data.value.cipher())

    @docs(post_vigenere_decipher_docs)
    @post("decipher")
    async def decipher(self, data: FromJSON[VigenereData]) -> Response:
        """
        Decipher the input request with Vigenere algorithm.

        Parameters
        ----------
        data : VigenereData
            A VigenereData from JSON from the request body.

        Returns
        -------
        response
            Response
        """
        return self.json(data.value.decipher())
