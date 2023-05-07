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

from vigenere_api.version import get_version, Version


class CtorSuite:
    @staticmethod
    def test_ctor() -> None:
        v = Version(major=1, minor=0, patch=0)

        assert v.major == 1
        assert v.minor == 0
        assert v.patch == 0

    class MissingFieldsSuite:
        @staticmethod
        @pytest.mark.raises(exception=ValidationError, message="major")
        def test_without_major() -> None:
            _ignored = Version(minor=0, patch=0)

        @staticmethod
        @pytest.mark.raises(exception=ValidationError, message="minor")
        def test_without_minor() -> None:
            _ignored = Version(major=0, patch=0)

        @staticmethod
        @pytest.mark.raises(exception=ValidationError, message="patch")
        def test_without_patch() -> None:
            _ignored = Version(minor=0, major=0)

        @staticmethod
        def test_with_only_patch() -> None:
            with pytest.raises(ValidationError) as error:
                _ignored = Version(patch=0)

            error_msg = str(error)
            assert "minor" in error_msg
            assert "major" in error_msg

        @staticmethod
        def test_with_only_minor() -> None:
            with pytest.raises(ValidationError) as error:
                _ignored = Version(minor=0)

            error_msg = str(error)
            assert "patch" in error_msg
            assert "major" in error_msg

        @staticmethod
        def test_with_only_manor() -> None:
            with pytest.raises(ValidationError) as error:
                _ignored = Version(major=0)

            error_msg = str(error)
            assert "minor" in error_msg
            assert "patch" in error_msg

        @staticmethod
        def test_with_nothing() -> None:
            with pytest.raises(ValidationError) as error:
                _ignored = Version()

            error = error.value.args[0]
            assert "major" in error[0]._loc
            assert "minor" in error[1]._loc
            assert "patch" in error[2]._loc

    class BadTypeSuite:
        @staticmethod
        @pytest.mark.raises(exception=ValidationError, message="major")
        def test_major() -> None:
            _ignored = Version(major=1.0, minor=0, patch=0)

        @staticmethod
        @pytest.mark.raises(exception=ValidationError, message="minor")
        def test_minor() -> None:
            _ignored = Version(major=1, minor=0.0, patch=0)

        @staticmethod
        @pytest.mark.raises(exception=ValidationError, message="patch")
        def test_patch() -> None:
            _ignored = Version(major=1, minor=0, patch=0.0)

    class BadValueSuite:
        @staticmethod
        @pytest.mark.raises(exception=ValidationError, message="major")
        def test_major() -> None:
            _ignored = Version(major=-10, minor=0, patch=0)

        @staticmethod
        @pytest.mark.raises(exception=ValidationError, message="minor")
        def test_minor() -> None:
            _ignored = Version(major=1, minor=-8, patch=0)

        @staticmethod
        @pytest.mark.raises(exception=ValidationError, message="patch")
        def test_patch() -> None:
            _ignored = Version(major=1, minor=0, patch=-9)


class OperationSuite:
    @staticmethod
    def test_str() -> None:
        v = Version(major=1, minor=0, patch=0)

        assert str(v) == "1.0.0"


def test_get_version() -> None:
    v = get_version()

    assert isinstance(v, Version)
    assert v == Version(major=2, minor=0, patch=0)
