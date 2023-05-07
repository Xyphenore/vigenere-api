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

"""Provide a route filter for OpenAPI docs."""

from collections.abc import Callable, Collection

from blacksheep import Route

from vigenere_api.version import Version
from .errors import (
    ExcludedPathsTypeError,
    ExcludedPathTypeError,
    PathTypeError,
    VersionTypeError,
)


def get_route_filter(
    excluded: Collection[str],
    api_version: Version,
) -> Callable[[str, Route], bool]:
    """
    Get the route filter.

    Parameters
    ----------
    excluded : Collection[str]
        All routes that should not be exposed.
    api_version : Version
        The API version.

    Raises
    ------
    ExcludedPathsTypeError
        Thrown if 'excluded' is not a Collection.
    ExcludedPathTypeError
        Thrown if 'excluded' does not contain only str.
    VersionTypeError
        Thrown if 'api_version' is not a Version.

    Returns
    -------
    filter
        Callable[[str, Route], bool]
    """
    if not isinstance(excluded, Collection):
        raise ExcludedPathsTypeError(excluded)

    for excluded_path in excluded:
        if not isinstance(excluded_path, str):
            raise ExcludedPathTypeError(excluded_path, excluded)

    if not isinstance(api_version, Version):
        raise VersionTypeError(api_version)

    def _route_filter(path: str, _: Route) -> bool:
        """
        Exclude routes that should not be exposed.

        Excluded routes:
        - /api/vx
        - /api/vx/openapi.json
        - /api/vx/openapi.yaml

        Parameters
        ----------
        path : str
            The URL path of route.
        _ : Route
            Ignored. The route object.

        Raises
        ------
        PathTypeError
            Thrown if 'path' is not a string.

        Returns
        -------
        route_shown
            bool
        """
        if not isinstance(path, str):
            raise PathTypeError(path)

        return path not in excluded and path.startswith(f"/api/v{api_version.major}")

    return _route_filter
