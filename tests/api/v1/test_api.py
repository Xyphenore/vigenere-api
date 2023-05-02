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
from blacksheep.testing import TestClient


@pytest.mark.asyncio()
async def test_get_api_docs(test_client: TestClient) -> None:
    response = await test_client.get("/api/v1")

    assert response is not None

    assert response.status == 200
    assert response.content is not None
    assert (
        response.content.body
        == b'<!DOCTYPE html>\n<html>\n<head>\n    <title>Vigenere-API</title>\n    <link rel="icon" href="/favicon.png"/>\n    <link type="text/css" rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.30.0/swagger-ui.css">\n</head>\n<body>\n    <div id="swagger-ui"></div>\n    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.30.0/swagger-ui-bundle.js"></script>\n    <script>\n    const ui = SwaggerUIBundle({\n        url: \'/openapi.yaml\',\n        oauth2RedirectUrl: window.location.origin + \'/docs/oauth2-redirect\',\n        dom_id: \'#swagger-ui\',\n        presets: [\n            SwaggerUIBundle.presets.apis,\n            SwaggerUIBundle.SwaggerUIStandalonePreset\n        ],\n        layout: "BaseLayout",\n        deepLinking: true,\n        showExtensions: true,\n        showCommonExtensions: true\n    })\n    </script>\n</body>\n</html>\n'
    )
    assert response.reason.upper() == "OK"


@pytest.mark.asyncio()
async def test_get_api_redocs(test_client: TestClient) -> None:
    response = await test_client.get("/api/v1/redocs")

    assert response is not None

    assert response.status == 200
    assert response.content is not None
    assert (
        response.content.body
        == b'<!DOCTYPE html>\n<html>\n  <head>\n    <title>Vigenere-API</title>\n    <meta charset="utf-8"/>\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <link rel="icon" href="/favicon.png"/>\n    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">\n    <style>\n      body {\n        margin: 0;\n        padding: 0;\n      }\n    </style>\n  </head>\n  <body>\n    <redoc spec-url="/openapi.yaml"></redoc>\n    <script src="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"> </script>\n  </body>\n</html>\n'
    )
    assert response.reason.upper() == "OK"
