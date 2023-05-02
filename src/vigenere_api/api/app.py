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

from blacksheep import Application
from blacksheep import Response
from blacksheep.server.env import is_development
from blacksheep.server.responses import redirect

from .v1.controllers import CaesarController
from .v1.openapi_docs import docs


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

application.register_controllers([CaesarController])
docs.bind_app(application)

get = application.router.get


@docs(ignored=True)
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
    return redirect("/api/v1")
