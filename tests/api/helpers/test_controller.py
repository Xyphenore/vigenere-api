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
from blacksheep.server.controllers import APIController

from vigenere_api.api.helpers.controller import _camel_to_kebab, Controller
from vigenere_api.api.helpers.errors import NameTypeError


class CamelCaseToKebabCaseSuite:
    @staticmethod
    def test_camelcase() -> None:
        converted = _camel_to_kebab("Camel")
        assert converted == "camel"

        converted = _camel_to_kebab("CamelCase")
        assert converted == "camel-case"

    @staticmethod
    def test_kebab() -> None:
        converted = _camel_to_kebab("camel-case")
        assert converted == "camel-case"

    @staticmethod
    def test_snake_case() -> None:
        converted = _camel_to_kebab("tedede_test")
        assert converted == "tedede_test"

    @staticmethod
    @pytest.mark.raises(excpetion=NameTypeError)
    def test_bad_type_name() -> None:
        _ignored = _camel_to_kebab(b"tedede")


class ControllerSuite:
    @staticmethod
    def test_instantiate() -> None:
        controller = Controller()
        assert controller is not None
        assert isinstance(controller, Controller)
        assert isinstance(controller, APIController)

    @staticmethod
    def test_class_name() -> None:
        assert Controller.__name__ == "Controller"

        assert Controller.class_name() == ""

    @staticmethod
    def test_inheritance_with_basic_name() -> None:
        class Test(Controller):
            pass

        test = Test()

        assert isinstance(test, Controller)
        assert isinstance(test, APIController)
        assert test.class_name() == "test"

    @staticmethod
    def test_inheritance_with_controller_name() -> None:
        class TestController(Controller):
            pass

        test = TestController()

        assert isinstance(test, Controller)
        assert isinstance(test, APIController)
        assert test.class_name() == "test"

    @staticmethod
    def test_inheritance_with_complex_controller_name() -> None:
        class ComplexTestController(Controller):
            pass

        test = ComplexTestController()

        assert isinstance(test, Controller)
        assert isinstance(test, APIController)
        assert test.class_name() == "complex-test"
