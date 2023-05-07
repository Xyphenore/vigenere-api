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

"""All errors used by utils."""

from collections.abc import Collection
from typing import Any, final

from vigenere_api.helpers import VigenereAPITypeError


@final
class ExcludedPathsTypeError(VigenereAPITypeError):
    """Thrown if 'excluded' is not a Collection."""

    def __init__(self, excluded: Any) -> None:
        """Create a new ExcludedPathsTypeError."""
        super().__init__(
            excluded,
            "excluded route collection",
            "a collection of string",
        )


@final
class ExcludedPathTypeError(TypeError):
    """Thrown if 'excluded' contains non-string values."""

    def __init__(self, path: Any, excluded: Collection[Any]) -> None:
        """Create a new ExcludedPathTypeError."""
        super().__init__(
            "The excluded route collection contains something else than a string."
            + f" The path '{path}' is bad. Please give a collection of string."
            + f" Complete collection: '{excluded}'",
        )


@final
class VersionTypeError(VigenereAPITypeError):
    """Thrown if 'version' is not a Version object."""

    def __init__(self, version: Any) -> None:
        """Create a new VersionTypeError."""
        super().__init__(version, "version", "a Version object")


@final
class NameTypeError(VigenereAPITypeError):
    """Thrown if 'name' is not a string."""

    def __init__(self, name: Any) -> None:
        """Create a new NameTypeError."""
        super().__init__(name, "name", "a string")


@final
class PathTypeError(VigenereAPITypeError):
    """Thrown if 'path' is not a string."""

    def __init__(self, path: Any) -> None:
        """Create a new PathTypeError."""
        super().__init__(path, "path", "a string")


@final
class OperationTypeError(VigenereAPITypeError):
    """Thrown if 'operation' is not an Operation object."""

    def __init__(self, operation: Any) -> None:
        """Create a new OperationTypeError."""
        super().__init__(operation, "operation", "an Operation object")


@final
class AlgorithmTypeError(VigenereAPITypeError):
    """Thrown if 'algorithm' is not an Algorithm object."""

    def __init__(self, algorithm: Any) -> None:
        """Create a new AlgorithmTypeError."""
        super().__init__(algorithm, "algorithm", "an Algorithm object")


@final
class ExamplesTypeError(VigenereAPITypeError):
    """Thrown if 'examples' is not a Sequence of CaesarData or VigenereData."""

    def __init__(self, data: Any, name: str) -> None:
        """Create a new ExamplesTypeError."""
        super().__init__(data, name, "a Sequence of CaesarData or VigenereData")


@final
class ExampleTypeError(TypeError):
    """Thrown if an example in 'data_examples' is not a CaesarData or VigenereData."""

    def __init__(self, example: Any, name: str) -> None:
        """Create a new ExampleTypeError."""
        cls_name = type(example).__qualname__

        super().__init__(
            f"An example is a '{cls_name}' in {name}."
            + " Please give a Sequence of CaesarData or VigenereData.",
        )
