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

from vigenere_api.api.helpers import Algorithm, ControllerDocs, Operation
from vigenere_api.api.helpers.errors import (
    AlgorithmTypeError,
    ExamplesTypeError,
    ExampleTypeError,
    OperationTypeError,
)
from vigenere_api.api.v1.controllers.caesar.docs import CAESAR_DATA1, CAESAR_DATA2
from vigenere_api.api.v2.controllers.vigenere.docs import VIGENERE_DATA1, VIGENERE_DATA2
from vigenere_api.models import CaesarData, VigenereData


def test_operation_cipher_caesar() -> None:
    docs = ControllerDocs(
        Operation.CIPHER,
        Algorithm.CAESAR,
        CAESAR_DATA1,
        CAESAR_DATA2,
    )

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


def test_operation_decipher_caesar() -> None:
    docs = ControllerDocs(
        Operation.DECIPHER,
        Algorithm.CAESAR,
        CAESAR_DATA1,
        CAESAR_DATA2,
    )

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


def test_operation_cipher_vigenere() -> None:
    docs = ControllerDocs(
        Operation.CIPHER,
        Algorithm.VIGENERE,
        VIGENERE_DATA1,
        VIGENERE_DATA2,
    )

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


def test_operation_decipher_vigenere() -> None:
    docs = ControllerDocs(
        Operation.DECIPHER,
        Algorithm.VIGENERE,
        VIGENERE_DATA1,
        VIGENERE_DATA2,
    )

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


class BadTypeSuite:
    @staticmethod
    @pytest.mark.raises(exception=OperationTypeError)
    def test_bad_operation() -> None:
        ControllerDocs("Operation.CIPHER", Algorithm.CAESAR, CAESAR_DATA1, CAESAR_DATA2)

    @staticmethod
    @pytest.mark.raises(exception=AlgorithmTypeError)
    def test_bad_algorithm() -> None:
        ControllerDocs(Operation.CIPHER, "Algorithm.CAESAR", CAESAR_DATA1, CAESAR_DATA2)

    @staticmethod
    @pytest.mark.raises(exception=ExamplesTypeError, message="data1_examples")
    def test_bad_sequence_data1() -> None:
        ControllerDocs(
            Operation.CIPHER, Algorithm.CAESAR, {"CAESAR_DATA1": "tere"}, CAESAR_DATA2
        )

    @staticmethod
    @pytest.mark.raises(exception=ExamplesTypeError, message="data2_examples")
    def test_bad_sequence_data2() -> None:
        ControllerDocs(
            Operation.CIPHER, Algorithm.CAESAR, CAESAR_DATA1, {"CAESAR_DATA1": "tere"}
        )

    @staticmethod
    @pytest.mark.raises(exception=ExampleTypeError, message="data1_examples")
    def test_bad_example_data1() -> None:
        ControllerDocs(
            Operation.CIPHER,
            Algorithm.CAESAR,
            ("ter", "ettr"),
            CAESAR_DATA2,
        )

    @staticmethod
    @pytest.mark.raises(exception=ExampleTypeError, message="data2_examples")
    def test_bad_example_data2() -> None:
        ControllerDocs(
            Operation.CIPHER,
            Algorithm.CAESAR,
            CAESAR_DATA1,
            ("ter", "ettr"),
        )
