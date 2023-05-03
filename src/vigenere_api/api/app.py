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

"""Create the application Vigenere-API."""

from blacksheep import Application, Response
from blacksheep.server.env import is_development
from blacksheep.server.responses import redirect

from vigenere_api.version import get_version
from .v1.controllers import CaesarController as V1CaesarController
from .v1.openapi_docs import docs as v1_docs

application = Application()
application.debug = False
application.show_error_details = False
application.use_cors(
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_origins=["http://127.0.0.1:8080"],
    allow_headers=["Authorization"],
    max_age=300,
)
# Exclude from coverage because this depends on the env
if is_development():  # pragma: no cover
    application.debug = True
    application.show_error_details = True

application.register_controllers([V1CaesarController])
v1_docs.bind_app(application)

get = application.router.get

version = get_version()


@v1_docs(ignored=True)
@get()
async def index() -> Response:
    """
    Route handle for the index page.

    It redirects to the OpenAPI documentation of the API.

    Returns
    -------
    redirect
        Response
    """
    return redirect(f"/api/v{version.major}")


def __fallback() -> str:
    """
    Process all requests to bad routes.

    Returns
    -------
    error_text
        str
    """

    return "OOPS! Nothing was found here!"


application.router.fallback = __fallback
