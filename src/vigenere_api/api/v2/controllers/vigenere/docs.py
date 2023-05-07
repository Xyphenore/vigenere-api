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

from vigenere_api.api.helpers import Algorithm, ControllerDocs, Operation
from vigenere_api.models import VigenereData


VIGENERE_DATA1 = (
    VigenereData(content="RI ZR VXGM XFLX CWMI", key="pierre"),
    VigenereData(content="ABC DAB CDA BCD ABC DAB", key="AbCd"),
    VigenereData(content="Ri zr vxgm xflx cwmi!", key="PIERRE"),
    VigenereData(content="AbC dab CDA bCd abc dAB", key="abcd"),
)
VIGENERE_DATA2 = (
    VigenereData(content="CA VA ETRE TOUT NOIR", key="PIERRE"),
    VigenereData(content="AAA AAA AAA AAA AAA AAA", key="abcd"),
    VigenereData(content="Ca va etre tout noir!", key="piErrE"),
    VigenereData(content="AaA aaa AAA aAa aaa aAA", key="aBCd"),
)


@final
@dataclass
class VigenereControllerDocs(ControllerDocs):
    """Create the documentation for Vigenere algorithm."""

    def __init__(self, operation: Operation) -> None:
        """
        Create a VigenereControllerDocs.

        Parameters
        ----------
        operation : Operation
        """
        super().__init__(operation, Algorithm.VIGENERE, VIGENERE_DATA1, VIGENERE_DATA2)


post_vigenere_cipher_docs = VigenereControllerDocs(operation=Operation.CIPHER)
post_vigenere_decipher_docs = VigenereControllerDocs(operation=Operation.DECIPHER)
