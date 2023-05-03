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

"""Common base for each model in Vigenere-API."""

from dataclasses import dataclass
from typing import final

from pydantic import BaseModel, Extra


class Model(BaseModel):
    """Base model for each model in Vigenere-API."""

    @final
    @dataclass
    class Config:
        """Model configuration."""

        title = "CaesarData"
        validate_all = True
        validate_assignment = True
        extra = Extra.forbid
        frozen = True
        smart_union = True
        arbitrary_types_allowed = False
