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

"""All OpenAPI docs for each controller."""

from .openapi_v1 import docs as openapi_v1_docs
from .openapi_versions import docs as openapi_versions_docs

__all__ = ["openapi_versions_docs", "openapi_v1_docs"]
