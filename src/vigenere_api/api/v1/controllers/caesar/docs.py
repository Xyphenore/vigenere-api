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
from enum import Enum
from enum import unique
from http import HTTPStatus
from typing import final

from blacksheep.server.openapi.common import ContentInfo
from blacksheep.server.openapi.common import EndpointDocs
from blacksheep.server.openapi.common import RequestBodyInfo
from blacksheep.server.openapi.common import ResponseExample
from blacksheep.server.openapi.common import ResponseInfo

from vigenere_api.models import CaesarData


@final
@unique
class CaesarOperation(Enum):
    """All Caesar operations."""

    value: str
    CIPHER = "cipher"
    DECIPHER = "decipher"


CAESAR_DATA1 = (
    CaesarData(content="Mabl bl t mxlm.", key="T"),
    CaesarData(content="Docd", key=10),
    CaesarData(content="Xiwx", key="e"),
)
CAESAR_DATA2 = (
    CaesarData(content="This is a test.", key="T"),
    CaesarData(content="Test", key=10),
    CaesarData(content="Test", key="e"),
)


@final
@dataclass
class CaesarControllerDocs(EndpointDocs):
    """Create the documentation for Caesar algorithm."""

    def __init__(self, operation: CaesarOperation) -> None:
        """
        Create a CaesarControllerDocs.

        Parameters
        ----------
        operation : CaesarOperation
        """
        response_examples = [
            ResponseExample(value=CAESAR_DATA1[0]),
            ResponseExample(value=CAESAR_DATA1[1]),
            ResponseExample(value=CAESAR_DATA1[2]),
        ]
        request_examples = {
            "example 0": CAESAR_DATA2[0],
            "example 1": CAESAR_DATA2[1],
            "example 2": CAESAR_DATA2[2],
        }

        if operation == CaesarOperation.DECIPHER:
            response_examples = [
                ResponseExample(value=CAESAR_DATA2[0]),
                ResponseExample(value=CAESAR_DATA2[1]),
                ResponseExample(value=CAESAR_DATA2[2]),
            ]
            request_examples = {
                "example 0": CAESAR_DATA1[0],
                "example 1": CAESAR_DATA1[1],
                "example 2": CAESAR_DATA1[2],
            }

        super().__init__(
            summary=(
                "Apply the Caesar algorithm to" + f" {operation.value} the content."
            ),
            description=(
                "Use the key with the Caesar algorithm to"
                + f" {operation.value} the content."
            ),
            tags=["Caesar"],
            request_body=RequestBodyInfo(
                description="Examples of requests body.",
                examples=request_examples,
            ),
            responses={
                HTTPStatus.OK: ResponseInfo(
                    description=f"Success {operation.value} with Caesar algorithm.",
                    content=[
                        ContentInfo(
                            type=CaesarData,
                            examples=response_examples,
                        ),
                    ],
                ),
                HTTPStatus.BAD_REQUEST: "Bad request.",
            },
        )


post_caesar_cipher_docs = CaesarControllerDocs(operation=CaesarOperation.CIPHER)
post_caesar_decipher_docs = CaesarControllerDocs(operation=CaesarOperation.DECIPHER)
