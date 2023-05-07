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
from vigenere_api.api.v2.controllers.vigenere.docs import (
    VIGENERE_DATA1,
    VIGENERE_DATA2,
    VigenereControllerDocs,
)
from vigenere_api.models import VigenereData


def test_operation_cipher() -> None:
    docs = VigenereControllerDocs(Operation.CIPHER)

    assert docs.summary == "Apply the Vigenere algorithm to cipher the content."
    assert (
        docs.description
        == "Use the key with the Vigenere algorithm to cipher the content."
    )
    assert "Vigenere" in docs.tags
    assert docs.request_body == RequestBodyInfo(
        description="Examples of requests body.",
        examples={
            "example 0": VIGENERE_DATA2[0],
            "example 1": VIGENERE_DATA2[1],
            "example 2": VIGENERE_DATA2[2],
            "example 3": VIGENERE_DATA2[3],
        },
    )
    assert docs.responses == {
        HTTPStatus.OK: ResponseInfo(
            description="Success cipher with Vigenere algorithm.",
            content=[
                ContentInfo(
                    type=VigenereData,
                    examples=[
                        ResponseExample(value=VIGENERE_DATA1[0]),
                        ResponseExample(value=VIGENERE_DATA1[1]),
                        ResponseExample(value=VIGENERE_DATA1[2]),
                        ResponseExample(value=VIGENERE_DATA1[3]),
                    ],
                ),
            ],
        ),
        HTTPStatus.BAD_REQUEST: "Bad request.",
    }


def test_operation_decipher() -> None:
    docs = VigenereControllerDocs(Operation.DECIPHER)

    assert docs.summary == "Apply the Vigenere algorithm to decipher the content."
    assert (
        docs.description
        == "Use the key with the Vigenere algorithm to decipher the content."
    )
    assert "Vigenere" in docs.tags
    assert docs.request_body == RequestBodyInfo(
        description="Examples of requests body.",
        examples={
            "example 0": VIGENERE_DATA1[0],
            "example 1": VIGENERE_DATA1[1],
            "example 2": VIGENERE_DATA1[2],
            "example 3": VIGENERE_DATA1[3],
        },
    )
    assert docs.responses == {
        HTTPStatus.OK: ResponseInfo(
            description="Success decipher with Vigenere algorithm.",
            content=[
                ContentInfo(
                    type=VigenereData,
                    examples=[
                        ResponseExample(value=VIGENERE_DATA2[0]),
                        ResponseExample(value=VIGENERE_DATA2[1]),
                        ResponseExample(value=VIGENERE_DATA2[2]),
                        ResponseExample(value=VIGENERE_DATA2[3]),
                    ],
                ),
            ],
        ),
        HTTPStatus.BAD_REQUEST: "Bad request.",
    }


@pytest.mark.raises(exception=OperationTypeError)
def test_bad_type_operation() -> None:
    VigenereControllerDocs("betet")
