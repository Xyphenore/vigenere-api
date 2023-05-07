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
from pydantic import ValidationError

from vigenere_api.models.base_data import BaseData


class CtorSuite:
    @staticmethod
    def test_with_text() -> None:
        text = "Test"
        data = BaseData(content=text)

        assert data.content == text

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_missing_content() -> None:
        _ignored_data = BaseData()

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_type_content() -> None:
        text = b"Test"
        _ignored_data = BaseData(content=text)

    @staticmethod
    @pytest.mark.raises(exception=ValidationError)
    def test_bad_empty_content() -> None:
        text = ""
        _ignored_data = BaseData(content=text)
