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

"""All errors thrown by version package."""

from enum import auto, unique
from typing import Any, final

from strenum import LowercaseStrEnum


@final
@unique
class Element(LowercaseStrEnum):
    """All elements in a version object."""

    MAJOR = auto()
    MINOR = auto()
    PATCH = auto()


class ElementVersionTypeError(TypeError):
    """Thrown if an element in the version is not an integer."""

    def __init__(self, element: Any, element_type: Element) -> None:
        """Create a ElementVersionTypeError from the element and element_type."""
        cls_name = type(element).__qualname__
        super().__init__(
            f"The {element_type} is '{cls_name}'."
            + " Please give an integer greater or equal to zero."
        )


@final
class MajorTypeError(ElementVersionTypeError):
    """Thrown if 'major' is not an integer."""

    def __init__(self, major: Any) -> None:
        """Create a MajorTypeError from the major."""
        super().__init__(major, Element.MAJOR)


@final
class MinorTypeError(ElementVersionTypeError):
    """Thrown if 'minor' is not an integer."""

    def __init__(self, minor: Any) -> None:
        """Create a MinorTypeError from the minor."""
        super().__init__(minor, Element.MINOR)


@final
class PatchTypeError(ElementVersionTypeError):
    """Thrown if 'patch' is not an integer."""

    def __init__(self, patch: Any) -> None:
        """Create a PatchTypeError from the patch."""
        super().__init__(patch, Element.PATCH)


class InvalidElementValueError(ValueError):
    """Thrown if an element in the version is less than 0."""

    def __init__(self, element: int, element_type: Element) -> None:
        super().__init__(
            f"The {element_type} is equal to '{element}'."
            + " Please give an integer greater or equal to zero."
        )


@final
class InvalidMajorValueError(InvalidElementValueError):
    """Thrown if 'major' is less than 0."""

    def __init__(self, major: int) -> None:
        super().__init__(major, Element.MAJOR)


@final
class InvalidMinorValueError(InvalidElementValueError):
    """Thrown if 'minor' is less than 0."""

    def __init__(self, minor: int) -> None:
        super().__init__(minor, Element.MINOR)


@final
class InvalidPatchValueError(InvalidElementValueError):
    """Thrown if 'patch' is less than 0."""

    def __init__(self, patch: int) -> None:
        super().__init__(patch, Element.PATCH)
