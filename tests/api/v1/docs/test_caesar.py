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

from http import HTTPStatus

import pytest
from blacksheep.server.openapi.common import (
    ContentInfo,
    RequestBodyInfo,
    ResponseExample,
    ResponseInfo,
)

from vigenere_api.api.helpers import Operation
from vigenere_api.api.helpers.errors import OperationTypeError
from vigenere_api.api.v1.controllers.caesar.docs import (
    CAESAR_DATA1,
    CAESAR_DATA2,
    CaesarControllerDocs,
)
from vigenere_api.models import CaesarData


def test_operation_cipher() -> None:
    docs = CaesarControllerDocs(Operation.CIPHER)

    assert docs.summary == "Apply the Caesar algorithm to cipher the content."
    assert (
        docs.description
        == "Use the key with the Caesar algorithm to cipher the content."
    )
    assert "Caesar" in docs.tags
    assert docs.request_body == RequestBodyInfo(
        description="Examples of requests body.",
        examples={
            "example 0": CAESAR_DATA2[0],
            "example 1": CAESAR_DATA2[1],
            "example 2": CAESAR_DATA2[2],
        },
    )
    assert docs.responses == {
        HTTPStatus.OK: ResponseInfo(
            description="Success cipher with Caesar algorithm.",
            content=[
                ContentInfo(
                    type=CaesarData,
                    examples=[
                        ResponseExample(value=CAESAR_DATA1[0]),
                        ResponseExample(value=CAESAR_DATA1[1]),
                        ResponseExample(value=CAESAR_DATA1[2]),
                    ],
                ),
            ],
        ),
        HTTPStatus.BAD_REQUEST: "Bad request.",
    }


def test_operation_decipher() -> None:
    docs = CaesarControllerDocs(Operation.DECIPHER)

    assert docs.summary == "Apply the Caesar algorithm to decipher the content."
    assert (
        docs.description
        == "Use the key with the Caesar algorithm to decipher the content."
    )
    assert "Caesar" in docs.tags
    assert docs.request_body == RequestBodyInfo(
        description="Examples of requests body.",
        examples={
            "example 0": CAESAR_DATA1[0],
            "example 1": CAESAR_DATA1[1],
            "example 2": CAESAR_DATA1[2],
        },
    )
    assert docs.responses == {
        HTTPStatus.OK: ResponseInfo(
            description="Success decipher with Caesar algorithm.",
            content=[
                ContentInfo(
                    type=CaesarData,
                    examples=[
                        ResponseExample(value=CAESAR_DATA2[0]),
                        ResponseExample(value=CAESAR_DATA2[1]),
                        ResponseExample(value=CAESAR_DATA2[2]),
                    ],
                ),
            ],
        ),
        HTTPStatus.BAD_REQUEST: "Bad request.",
    }


@pytest.mark.raises(exception=OperationTypeError)
def test_bad_type_operation() -> None:
    CaesarControllerDocs("btest")
