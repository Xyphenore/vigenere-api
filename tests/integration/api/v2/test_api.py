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
import requests


@pytest.mark.integration_test()
def test_get_api_docs(server: str) -> None:
    response = requests.get(
        url=server + "/api/v2",
        timeout=1,
        allow_redirects=False,
    )

    assert response is not None

    assert response.status_code == 200
    assert response.content != b""
    assert response.text != ""
    assert not response.is_redirect

    assert response.next is None


@pytest.mark.integration_test()
def test_get_api_redocs(server: str) -> None:
    response = requests.get(
        url=server + "/api/v2/redocs",
        timeout=1,
        allow_redirects=False,
    )

    assert response is not None

    assert response.status_code == 200
    assert response.content != b""
    assert response.text != ""
    assert not response.is_redirect

    assert response.next is None
