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

import pytest

from openapidocs.common import Format
from openapidocs.v3 import ExternalDocs, Tag
from vigenere_api.api import application
from vigenere_api.api.helpers import VigenereAPIOpenAPIHandler
from vigenere_api.api.helpers.errors import VersionTypeError
from vigenere_api.version import Version


def basic_test() -> None:
    docs = VigenereAPIOpenAPIHandler(Version(major=1, minor=0, patch=0))

    assert docs.version == Version(major=1, minor=0, patch=0)

    info = docs.info
    assert info.title == "Vigenere-API"
    assert info.version == "1.0.0"
    assert (
        info.description
        == """
        An API to use cipher, decipher and decrypt method with the Vigenere algorithm.
        The Caesar algorithm is provided for the cipher method and decipher method.

        It's a JSON-RPC API.
        Powered by BlackSheep framework: https://www.neoteroi.dev/blacksheep/
        """
    )
    assert info.contact.name == "Axel DAVID"
    assert info.contact.email == "axel.david@etu.univ-amu.fr"
    assert info.license.name == "GPL-3.0"
    assert info.license.url == "http://localhost:8080/LICENSE.md"

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


@pytest.mark.raises(exception=VersionTypeError)
def test_bad_type_version() -> None:
    _ignored = VigenereAPIOpenAPIHandler(b"toto")
