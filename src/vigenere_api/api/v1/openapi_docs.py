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

"""Common OpenAPI docs."""

from blacksheep.server.openapi.ui import ReDocUIProvider

from openapidocs.common import Format
from openapidocs.v3 import Contact
from openapidocs.v3 import Info
from openapidocs.v3 import License
from vigenere_api.api.utils import VigenereAPIOpenAPIHandler


APP_URL = "https://localhost:8080"

docs = VigenereAPIOpenAPIHandler(
    info=Info(
        title="Vigenere-API",
        version="1.0.0",
        description="""
        An API to use cipher, decipher and decrypt method with the Vigenere algorithm.
        The Caesar algorithm is provided for the cipher method and decipher method.

        It's a JSON-RPC API.
        Powered by BlackSheep framework: https://www.neoteroi.dev/blacksheep/
        """,
        contact=Contact(name="Axel DAVID", email="axel.david@etu.univ-amu.fr"),
        license=License(name="GPL-3.0", url=APP_URL + "/LICENSE.md"),
    ),
    ui_path="/api/v1",
    preferred_format=Format.YAML,
)

docs.ui_providers.append(ReDocUIProvider(ui_path="/api/v1/redocs"))
