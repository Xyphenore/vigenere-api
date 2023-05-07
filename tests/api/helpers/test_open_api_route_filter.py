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
from inspect import signature

import pytest
from blacksheep import Route

from vigenere_api.api.helpers.errors import (
    ExcludedPathsTypeError,
    ExcludedPathTypeError,
    PathTypeError,
    VersionTypeError,
)
from vigenere_api.api.helpers.open_api_route_filter import get_route_filter
from vigenere_api.version import Version


def test_get_filter() -> None:
    excluded = []
    version = Version(major=1, minor=1, patch=10)
    filter = get_route_filter(excluded, version)

    assert callable(filter)
    s = signature(filter)

    assert s.return_annotation == bool

    parameters_type = list(s.parameters.values())

    assert len(parameters_type) == 2
    assert parameters_type[0].annotation == str
    assert parameters_type[1].annotation == Route


@pytest.mark.raises(exception=ExcludedPathsTypeError)
def test_bad_type_excluded() -> None:
    excluded = 10
    version = Version(major=1, minor=1, patch=10)
    _ignored = get_route_filter(excluded, version)


@pytest.mark.raises(exception=ExcludedPathTypeError)
def test_bad_type_path_in_excluded() -> None:
    excluded = [b"test"]
    version = Version(major=1, minor=1, patch=10)
    _ignored = get_route_filter(excluded, version)


@pytest.mark.raises(exception=VersionTypeError)
def test_bad_type_version() -> None:
    _ignored = get_route_filter((), "1.0.0")


@pytest.mark.raises(exception=PathTypeError)
def test_filter_bad_type_path() -> None:
    version = Version(major=1, minor=1, patch=10)
    route_filter = get_route_filter(["/api"], version)
    _ignored = route_filter(b"/http", Route("http", {}))


def test_filter_bad_type_route() -> None:
    version = Version(major=1, minor=1, patch=10)
    route_filter = get_route_filter(["/api"], version)
    assert route_filter(f"/api/v{version.major}/test", {})


def test_filter_route_excluded() -> None:
    version = Version(major=1, minor=1, patch=10)
    route_filter = get_route_filter(["/api"], version)
    assert not route_filter("/api", Route("http", {}))


def test_filter_route_not_excluded() -> None:
    version = Version(major=1, minor=1, patch=10)
    route_filter = get_route_filter(["/api"], version)
    assert route_filter(f"/api/v{version.major}/test", Route("http", {}))
