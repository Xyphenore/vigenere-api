# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  MIT License                                                                         +
#                                                                                      +
#  Copyright (c) 2019 James C Sinclair                                                 +
#                                                                                      +
#  Permission is hereby granted, free of charge, to any person obtaining a copy        +
#  of this software and associated documentation files (the "Software"), to deal       +
#  in the Software without restriction, including without limitation the rights        +
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell           +
#  copies of the Software, and to permit persons to whom the Software is               +
#  furnished to do so, subject to the following conditions:                            +
#                                                                                      +
#  The above copyright notice and this permission notice shall be included in all      +
#  copies or substantial portions of the Software.                                     +
#                                                                                      +
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR          +
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,            +
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE         +
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER              +
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,       +
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE       +
#  SOFTWARE.                                                                           +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import enum
from typing import Any

class StrEnum(str, enum.Enum):
    def __str__(self) -> str: ...
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class LowercaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class UppercaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class CamelCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class PascalCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class KebabCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class SnakeCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class MacroCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class CamelSnakeCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class PascalSnakeCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class SpongebobCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class CobolCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...

class HttpHeaderCaseStrEnum(StrEnum):
    @staticmethod
    def _generate_next_value_(name: str, *_: Any) -> str: ...
