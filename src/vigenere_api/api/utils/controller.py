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

"""Common base for each api controller."""

from re import sub
from typing import final

from blacksheep.server.controllers import APIController

from .errors import NameTypeError


def _camel_to_kebab(name: str) -> str:
    """
    Convert the name in camel case to kebab case.

    Notes
    -----
    Does not check if the name is in CamelCase.

    Parameters
    ----------
    name : str
        The name to convert.

    Raises
    ------
    NameTypeError
        Thrown if 'name' is not a string.

    Returns
    -------
    kebab_name
        str
    """
    if not isinstance(name, str):
        raise NameTypeError(name)

    kebab_name = sub("([A-Z])", "-\\1", name)
    return kebab_name.lstrip("-").lower()


class Controller(APIController):
    """Common base for each api controller."""

    @classmethod
    @final
    def class_name(cls) -> str:
        """
        Name of the class.

        Returns
        -------
        class_name
            str
        """
        name = _camel_to_kebab(cls.__name__).removesuffix("controller")
        return name.rstrip("-")
