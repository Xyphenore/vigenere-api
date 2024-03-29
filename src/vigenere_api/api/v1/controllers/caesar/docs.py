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


"""The caesar controller's documentation."""

from dataclasses import dataclass
from typing import final

from vigenere_api.api.helpers.operation_docs import Algorithm, ControllerDocs, Operation
from vigenere_api.models import CaesarData


CAESAR_DATA1 = (
    CaesarData(content="DeFgHiJkLmNoPqRsTuVwXyZaBc", key=3),
    CaesarData(content="DeFgHiJkLmNoPqRsTuVwXyZaBc", key="D"),
    CaesarData(content="Mabl bl t mxlm.", key="T"),
)
CAESAR_DATA2 = (
    CaesarData(content="AbCdEfGhIjKlMnOpQrStUvWxYz", key=3),
    CaesarData(content="AbCdEfGhIjKlMnOpQrStUvWxYz", key="d"),
    CaesarData(content="This is a test.", key="T"),
)


@final
@dataclass
class CaesarControllerDocs(ControllerDocs):
    """Create the documentation for Caesar algorithm."""

    def __init__(self, operation: Operation) -> None:
        """
        Create a CaesarControllerDocs.

        Parameters
        ----------
        operation : Operation
        """
        super().__init__(operation, Algorithm.CAESAR, CAESAR_DATA1, CAESAR_DATA2)


post_caesar_cipher_docs = CaesarControllerDocs(operation=Operation.CIPHER)
post_caesar_decipher_docs = CaesarControllerDocs(operation=Operation.DECIPHER)
