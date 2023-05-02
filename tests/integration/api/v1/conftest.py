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
import os
from collections.abc import Generator
from multiprocessing import Process
from time import sleep

import pytest
import uvicorn

from vigenere_api.api import application


def get_sleep_time() -> float:
    # when starting a server process,
    # a longer sleep time is necessary on Windows
    if os.name == "nt":
        return 1.5
    return 0.5


server_host = "127.0.0.1"
server_port = 44555


def _start_server() -> None:
    uvicorn.run(application, host=server_host, port=server_port, log_level="debug")


@pytest.fixture(scope="session", autouse=True)
def server() -> Generator[str, None, None]:
    server_process = Process(target=_start_server)
    server_process.start()
    sleep(get_sleep_time())

    if not server_process.is_alive():
        raise TypeError("The server process did not start!")

    yield "http://" + server_host + ":" + str(server_port)

    sleep(1.2)
    server_process.terminate()
