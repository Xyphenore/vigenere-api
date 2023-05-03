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
    assert response.reason.upper() == "OK"


@pytest.mark.asyncio()
async def test_get_api_redocs(test_client: TestClient) -> None:
    response = await test_client.get("/api/v1/redocs")

    assert response is not None

    assert response.status == 200
    assert response.content is not None
    assert response.reason.upper() == "OK"
