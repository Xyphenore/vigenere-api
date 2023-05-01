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

import os
from enum import Enum, unique
from typing import final

from blacksheep import Application, Response
from blacksheep.server.responses import redirect

from .v1.controllers import CaesarController
from .v1.openapi_docs import docs

TYPE = os.environ.get("APPLICATION_TYPE", "Production").upper()


@final
@unique
class Types(Enum):
    """All available application environment types."""

    value: str

    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"


# TODO Remove it
TYPE = Types.DEVELOPMENT.value

if Types.DEVELOPMENT.value == TYPE:
    app = Application(
        debug=True,
        show_error_details=True,
    )

elif Types.PRODUCTION.value == TYPE:
    app = Application(show_error_details=False)

else:
    raise ValueError(f"The application type is unknown: '{TYPE}'.")

get = app.router.get
post = app.router.post
docs.bind_app(app)

app.register_controllers([CaesarController])

app.use_cors(
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_origins=["http://127.0.0.1:8080"],
    allow_headers=["Authorization"],
    max_age=300,
)


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
