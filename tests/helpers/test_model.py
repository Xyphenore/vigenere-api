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
from vigenere_api.helpers import Model


def test_instantiate() -> None:
    obj = Model()

    assert obj is not None


class InheritanceSuite:
    @staticmethod
    def test_basic() -> None:
        class Test(Model):
            pass

        obj = Test()

        assert obj is not None
        assert obj == Model()

    @staticmethod
    def test_with_new_field() -> None:
        class Test(Model):
            test: str

        obj = Test(test="TEST")

        assert obj is not None
        assert obj.test == "TEST"
