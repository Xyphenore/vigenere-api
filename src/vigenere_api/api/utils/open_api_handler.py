"""
Override the OpenAPIHandler to give server list,
tag list and security of the VigenereAPI.
"""

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
from typing import final

from blacksheep.server.openapi.v3 import OpenAPIHandler

from openapidocs.v3 import ExternalDocs
from openapidocs.v3 import OpenAPI
from openapidocs.v3 import Tag


@final
class VigenereAPIOpenAPIHandler(OpenAPIHandler):
    """
    Override the OpenAPIHandler to give server list,
    tag list and security of the VigenereAPI.
    """

    def on_docs_generated(self, docs: OpenAPI) -> None:
        docs.tags = [
            Tag(
                name="Vigenere",
                description="Provide the Vigenere algorithm.",
                external_docs=ExternalDocs(
                    url="https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher",
                    description="Wikipedia page of Vigenere cipher.",
                ),
            ),
            Tag(
                name="Caesar",
                description="Provide the Caesar algorithm.",
                external_docs=ExternalDocs(
                    url="https://en.wikipedia.org/wiki/Caesar_cipher",
                    description="Wikipedia page of Caesar cipher.",
                ),
            ),
        ]
