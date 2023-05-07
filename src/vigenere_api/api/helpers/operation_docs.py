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

"""A controller's documentation."""

from collections.abc import Sequence
from dataclasses import dataclass
from enum import auto, unique
from http import HTTPStatus
from typing import final, Union

from blacksheep.server.openapi.common import (
    ContentInfo,
    EndpointDocs,
    RequestBodyInfo,
    ResponseExample,
    ResponseInfo,
)

from strenum import LowercaseStrEnum, PascalCaseStrEnum
from vigenere_api.models import CaesarData, VigenereData

from .errors import (
    AlgorithmTypeError,
    ExamplesTypeError,
    ExampleTypeError,
    OperationTypeError,
)


@final
@unique
class Operation(LowercaseStrEnum):
    """All Caesar or Vigenere operations."""

    CIPHER = auto()
    DECIPHER = auto()


@final
@unique
class Algorithm(PascalCaseStrEnum):
    """All algorithms available."""

    CAESAR = auto()
    VIGENERE = auto()


@dataclass
class ControllerDocs(EndpointDocs):
    """Create the documentation for Caesar algorithm."""

    def __init__(
        self,
        operation: Operation,
        algorithm: Algorithm,
        data1_examples: Sequence[Union[CaesarData, VigenereData]],
        data2_examples: Sequence[Union[CaesarData, VigenereData]],
    ) -> None:
        """
        Create a ControllerDocs.

        Parameters
        ----------
        operation : Operation
            The operation type.
        algorithm : Algorithm
            The algorithm type.
        data1_examples : Sequence[Union[CaesarData, VigenereData]]
            The first set of examples.
        data2_examples : Sequence[Union[CaesarData, VigenereData]]
            The second set of examples.

        Raises
        ------
        OperationTypeError
            Thrown if 'operation' is not an Operation object.
        AlgorithmTypeError
            Thrown if 'algorithm' is not an Algorithm object.
        ExamplesTypeError
            Thrown if 'data1_examples' is not a Sequence object.
        ExamplesTypeError
            Thrown if 'data2_examples' is not a Sequence object.
        ExampleTypeError
            Thrown if 'data1_examples[i]' is not a CaesarData or VigenereData object.
        ExampleTypeError
            Thrown if 'data2_examples[i]' is not a CaesarData or VigenereData object.
        """
        if not isinstance(operation, Operation):
            raise OperationTypeError(operation)

        if not isinstance(algorithm, Algorithm):
            raise AlgorithmTypeError(algorithm)

        if not isinstance(data1_examples, Sequence):
            raise ExamplesTypeError(data1_examples, "data1_examples")

        if not isinstance(data2_examples, Sequence):
            raise ExamplesTypeError(data2_examples, "data2_examples")

        for example in data1_examples:
            if not isinstance(example, (CaesarData, VigenereData)):
                raise ExampleTypeError(example, "data1_examples")

        for example in data2_examples:
            if not isinstance(example, (CaesarData, VigenereData)):
                raise ExampleTypeError(example, "data2_examples")

        response_examples = [ResponseExample(value=data) for data in data1_examples]
        request_examples = {
            f"example {i}": data for i, data in enumerate(data2_examples)
        }

        if operation == Operation.DECIPHER:
            response_examples = [ResponseExample(value=data) for data in data2_examples]
            request_examples = {
                f"example {i}": data for i, data in enumerate(data1_examples)
            }

        response_type = VigenereData if algorithm == Algorithm.VIGENERE else CaesarData

        ok_res = ResponseInfo(
            description=f"Success {operation.value} with {algorithm} algorithm.",
            content=[
                ContentInfo(
                    type=response_type,
                    examples=response_examples,
                ),
            ],
        )

        summary_str = (
            f"Apply the {algorithm} algorithm to {operation.value} the content."
        )

        super().__init__(
            summary=summary_str,
            description=(
                f"Use the key with the {algorithm} algorithm"
                + f" to {operation.value} the content."
            ),
            tags=[f"{algorithm}"],
            request_body=RequestBodyInfo(
                description="Examples of requests body.",
                examples=request_examples,
            ),
            responses={
                HTTPStatus.OK: ok_res,
                HTTPStatus.BAD_REQUEST: "Bad request.",
            },
        )
