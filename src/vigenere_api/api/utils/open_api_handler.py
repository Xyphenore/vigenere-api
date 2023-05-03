"""APIHandler with a tag list of the VigenereAPI."""

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

from typing import final, Final

from blacksheep.server.openapi.ui import ReDocUIProvider
from blacksheep.server.openapi.v3 import OpenAPIHandler

from openapidocs.common import Format
from openapidocs.v3 import Contact, ExternalDocs, Info, License, OpenAPI, Tag
from vigenere_api.version import Version

from .errors import VersionTypeError
from .open_api_route_filter import get_route_filter


@final
class VigenereAPIOpenAPIHandler(OpenAPIHandler):
    """APIHandler with a tag list of the VigenereAPI."""

    def __init__(self, version: Version) -> None:
        """
        Create a new OpenAPIHandler for the version.

        Parameters
        ----------
        version : Version
            The API version.

        Raises
        ------
        VersionTypeError
            Thrown if 'version' is not a Version object.
        """

        if not isinstance(version, Version):
            raise VersionTypeError(version)

        self.__version: Final = version

        app_url = "http://localhost:8080"
        api_route = f"/api/v{version.major}"

        json_spec_path = f"{api_route}/openapi.json"
        yaml_spec_path = f"{api_route}/openapi.yaml"

        super().__init__(
            info=Info(
                title="Vigenere-API",
                version=str(version),
                description="""
                An API to use cipher, decipher and decrypt method with the Vigenere algorithm.
                The Caesar algorithm is provided for the cipher method and decipher method.

                It's a JSON-RPC API.
                Powered by BlackSheep framework: https://www.neoteroi.dev/blacksheep/
                """,
                contact=Contact(name="Axel DAVID", email="axel.david@etu.univ-amu.fr"),
                license=License(name="GPL-3.0", url=f"{app_url}/LICENSE.md"),
            ),
            ui_path=api_route,
            json_spec_path=json_spec_path,
            yaml_spec_path=yaml_spec_path,
            preferred_format=Format.YAML,
        )

        self.ui_providers.append(ReDocUIProvider(ui_path=f"{api_route}/redocs"))
        self.include = get_route_filter((api_route, json_spec_path, yaml_spec_path))

    @property
    def version(self) -> Version:
        """
        Get the API version.

        Returns
        -------
        Version
            The API version.
        """
        return self.__version

    def on_docs_generated(self, docs: OpenAPI) -> None:
        """Add a tag list to docs."""
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
