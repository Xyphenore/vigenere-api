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

"""Version of the API."""

from typing import final

from pydantic import validator

from vigenere_api.helpers import Model

from .errors import (
    InvalidMajorValueError,
    InvalidMinorValueError,
    InvalidPatchValueError,
    MajorTypeError,
    MinorTypeError,
    PatchTypeError,
)


StrictPositiveIntOrNull = int


@final
class Version(Model):
    """Version of the API."""

    major: StrictPositiveIntOrNull
    minor: StrictPositiveIntOrNull
    patch: StrictPositiveIntOrNull

    @validator("major", pre=True)
    def validate_major(cls, major: int) -> int:
        """
        Check if the affectation to major respects contraints.

        Parameters
        ----------
        major : int
            The new major element of version.

        Raises
        ------
        MajorTypeError
            Thrown if 'major' is not an integer.
        InvalidMajorValueError
            Thrown if 'major' is negative.

        Returns
        -------
        major
            int
        """
        if not isinstance(major, int):
            raise MajorTypeError(major)

        if major < 0:
            raise InvalidMajorValueError(major)

        return major

    @validator("minor", pre=True)
    def validate_minor(cls, minor: int) -> int:
        """
        Check if the affectation to minor respects contraints.

        Parameters
        ----------
        minor : int
            The new minor element of version.

        Raises
        ------
        MinorTypeError
            Thrown if 'minor' is not an integer.
        InvalidMinorValueError
            Thrown if 'minor' is negative.

        Returns
        -------
        minor
            int
        """
        if not isinstance(minor, int):
            raise MinorTypeError(minor)

        if minor < 0:
            raise InvalidMinorValueError(minor)

        return minor

    @validator("patch", pre=True)
    def validate_patch(cls, patch: int) -> int:
        """
        Check if the affectation to patch respects contraints.

        Parameters
        ----------
        patch : int
            The new patch element of version.

        Raises
        ------
        PatchTypeError
            Thrown if 'patch' is not an integer.
        InvalidPatchValueError
            Thrown if 'patch' is negative.

        Returns
        -------
        patch
            int
        """
        if not isinstance(patch, int):
            raise PatchTypeError(patch)

        if patch < 0:
            raise InvalidPatchValueError(patch)

        return patch

    def __str__(self) -> str:
        """
        Convert the version to a string.

        Returns
        -------
        version
            str
        """
        return f"{self.major}.{self.minor}.{self.patch}"


def get_version() -> Version:
    """
    Get project version.

    Returns
    -------
    version
        Version
    """
    return Version(major=2, minor=0, patch=0)
