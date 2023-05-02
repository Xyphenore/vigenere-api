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

from openapidocs.common import Format
from openapidocs.v3 import Contact
from openapidocs.v3 import ExternalDocs
from openapidocs.v3 import Info
from openapidocs.v3 import License
from openapidocs.v3 import Tag
from vigenere_api.api import application
from vigenere_api.api.utils import VigenereAPIOpenAPIHandler


def basic_test() -> None:
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
            license=License(name="GPL-3.0", url="TEST/LICENSE.md"),
        ),
        ui_path="/api/v1",
        preferred_format=Format.YAML,
    )

    info = docs.info
    assert info.title == "Vigenere-API"
    assert info.version == "1.0.0"
    assert info.description == (
        "\n"
        "            An API to use cipher, decipher and decrypt method with the "
        "Vigenere algorithm.\n"
        "            The Caesar algorithm is provided for the cipher method and "
        "decipher method.\n"
        "\n"
        "            It's a JSON-RPC API.\n"
        "            Powered by BlackSheep framework: "
        "https://www.neoteroi.dev/blacksheep/\n"
        "            "
    )
    assert info.contact.name == "Axel DAVID"
    assert info.contact.email == "axel.david@etu.univ-amu.fr"
    assert info.license.name == "GPL-3.0"
    assert info.license.url == "TEST/LICENSE.md"

    assert docs.ui_providers[0].ui_path == "/api/v1"

    assert docs.preferred_format == Format.YAML

    openapi_docs = docs.generate_documentation(application)
    docs.on_docs_generated(openapi_docs)
    assert openapi_docs.info == docs.info
    assert openapi_docs.tags == [
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
