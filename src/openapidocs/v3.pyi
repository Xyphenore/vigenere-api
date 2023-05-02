"""
This module defines classes that can be used to generate OpenAPI Documentation
version 3.
https://swagger.io/specification/.
"""

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
from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Any
from typing import Optional
from typing import Union

from openapidocs.common import OpenAPIElement
from openapidocs.common import OpenAPIRoot

class ParameterLocation(Enum):
    QUERY = "query"
    HEADER = "header"
    PATH = "path"
    COOKIE = "cookie"

class ValueType(Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    NUMBER = "number"
    OBJECT = "object"
    STRING = "string"

class ValueFormat(Enum):
    BASE64 = "base64"
    BINARY = "binary"
    BYTE = "byte"
    DATE = "date"
    DATETIME = "date-time"
    DOUBLE = "double"
    FLOAT = "float"
    INT32 = "int32"
    INT64 = "int64"
    PASSWORD = "password"
    EMAIL = "email"
    UUID = "uuid"
    PARTIALTIME = "partial-time"

class SecuritySchemeType(Enum):
    APIKEY = "apiKey"
    HTTP = "http"
    OAUTH = "oauth2"
    OAUTH2 = "oauth2"
    OIDC = "openIdConnect"
    OPENIDCONNECT = "openIdConnect"

@dataclass
class Contact(OpenAPIElement):
    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None

@dataclass
class ExternalDocs(OpenAPIElement):
    url: str
    description: Optional[str] = None

@dataclass
class License(OpenAPIElement):
    name: str
    url: Optional[str] = None

@dataclass
class Info(OpenAPIElement):
    title: str
    version: str
    description: Optional[str] = None
    terms_of_service: Optional[str] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None

@dataclass
class ServerVariable(OpenAPIElement):
    default: str
    description: Optional[str] = None
    enum: Optional[list[str]] = None

@dataclass
class Server(OpenAPIElement):
    url: str
    description: Optional[str] = None
    variables: Optional[dict[str, ServerVariable]] = None

@dataclass
class XML(OpenAPIElement):
    name: Optional[str] = None
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    attribute: Optional[bool] = None
    wrapped: Optional[bool] = None

@dataclass
class Discriminator(OpenAPIElement):
    property_name: str
    mapping: Optional[dict[str, str]] = None

@dataclass
class Schema(OpenAPIElement):
    type: Union[None, str, ValueType] = None
    format: Union[None, str, ValueFormat] = None
    required: Optional[list[str]] = None
    properties: Optional[dict[str, Union[Schema, Reference]]] = None
    default: Optional[Any] = None
    deprecated: Optional[bool] = None
    example: Any = None
    external_docs: Optional[ExternalDocs] = None
    ref: Optional[str] = None
    title: Optional[str] = None
    max_length: Optional[float] = None
    min_length: Optional[float] = None
    maximum: Optional[float] = None
    minimum: Optional[float] = None
    nullable: Optional[bool] = None
    xml: Optional[XML] = None
    items: Union[None, Schema, Reference] = None
    enum: Optional[list[str]] = None
    discriminator: Optional[Discriminator] = None
    all_of: Optional[list[Union[Schema, Reference]]] = None
    any_of: Optional[list[Union[Schema, Reference]]] = None
    one_of: Optional[list[Union[Schema, Reference]]] = None
    not_: Optional[list[Union[Schema, Reference]]] = None

@dataclass
class Header(OpenAPIElement):
    description: Optional[str] = None
    schema: Union[None, Schema, Reference] = None

@dataclass
class Example(OpenAPIElement):
    summary: Optional[str] = None
    description: Optional[str] = None
    value: Any = None
    external_value: Optional[str] = None

@dataclass
class Reference(OpenAPIElement):
    ref: str

@dataclass
class Encoding(OpenAPIElement):
    content_type: Optional[str] = None
    headers: Optional[dict[str, Union[Header, Reference]]] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allow_reserved: Optional[bool] = None

@dataclass
class Link(OpenAPIElement):
    operation_ref: Optional[str] = None
    operation_id: Optional[str] = None
    parameters: Optional[dict[str, Any]] = None
    request_body: Any = None
    description: Optional[str] = None
    server: Optional[Server] = None

@dataclass
class MediaType(OpenAPIElement):
    schema: Union[None, Schema, Reference] = None
    example: Any = None
    examples: Optional[dict[str, Union[Example, Reference]]] = None
    encoding: Optional[dict[str, Encoding]] = None

@dataclass
class Response(OpenAPIElement):
    description: Optional[str] = None
    headers: Optional[dict[str, Union[Header, Reference]]] = None
    content: Optional[dict[str, Union[MediaType, Reference]]] = None
    links: Optional[dict[str, Union[Link, Reference]]] = None

@dataclass
class Parameter(OpenAPIElement):
    name: str
    in_: ParameterLocation
    schema: Union[None, Schema, Reference] = None
    content: Optional[dict[str, MediaType]] = None
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    allow_empty_value: Optional[bool] = None
    example: Optional[Any] = None
    examples: Optional[dict[str, Union[Example, Reference]]] = None

@dataclass
class RequestBody(OpenAPIElement):
    content: dict[str, MediaType]
    required: Optional[bool] = None
    description: Optional[str] = None

@dataclass
class SecurityRequirement(OpenAPIElement):
    name: str
    value: list[str]

@dataclass
class Operation(OpenAPIElement):
    responses: dict[str, Response]
    tags: Optional[list[str]] = None
    operation_id: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    external_docs: Optional[ExternalDocs] = None
    parameters: Optional[list[Union[Parameter, Reference]]] = None
    request_body: Union[None, RequestBody, Reference] = None
    callbacks: Optional[dict[str, Union[Callback, Reference]]] = None
    deprecated: Optional[bool] = None
    security: Optional[list[SecurityRequirement]] = None
    servers: Optional[list[Server]] = None

@dataclass
class PathItem(OpenAPIElement):
    summary: Optional[str] = None
    ref: Optional[str] = None
    description: Optional[str] = None
    get: Optional[Operation] = None
    put: Optional[Operation] = None
    post: Optional[Operation] = None
    delete: Optional[Operation] = None
    options: Optional[Operation] = None
    head: Optional[Operation] = None
    patch: Optional[Operation] = None
    trace: Optional[Operation] = None
    servers: Optional[list[Server]] = None
    parameters: Optional[list[Union[Parameter, Reference]]] = None

@dataclass
class Callback(OpenAPIElement):
    expression: str
    path: PathItem

@dataclass
class OAuthFlow(OpenAPIElement):
    scopes: dict[str, str]
    authorization_url: Optional[str] = None
    token_url: Optional[str] = None
    refresh_url: Optional[str] = None

@dataclass
class OAuthFlows(OpenAPIElement):
    implicit: Optional[OAuthFlow] = None
    password: Optional[OAuthFlow] = None
    client_credentials: Optional[OAuthFlow] = None
    authorization_code: Optional[OAuthFlow] = None

class SecurityScheme(OpenAPIElement, ABC):
    """Abstract security scheme."""

@dataclass
class HTTPSecurity(SecurityScheme):
    scheme: str
    type: SecuritySchemeType = ...
    description: Optional[str] = None
    bearer_format: Optional[str] = None

@dataclass
class APIKeySecurity(SecurityScheme):
    name: str
    in_: ParameterLocation
    type: SecuritySchemeType = ...
    description: Optional[str] = None

@dataclass
class OAuth2Security(SecurityScheme):
    flows: OAuthFlows
    type: SecuritySchemeType = ...
    description: Optional[str] = None

@dataclass
class OpenIdConnectSecurity(SecurityScheme):
    open_id_connect_url: str
    type: SecuritySchemeType = ...
    description: Optional[str] = None

@dataclass
class Components(OpenAPIElement):
    schemas: Optional[dict[str, Union[Schema, Reference]]] = None
    responses: Optional[dict[str, Union[Response, Reference]]] = None
    parameters: Optional[dict[str, Union[Parameter, Reference]]] = None
    examples: Optional[dict[str, Union[Example, Reference]]] = None
    request_bodies: Optional[dict[str, Union[RequestBody, Reference]]] = None
    headers: Optional[dict[str, Union[Header, Reference]]] = None
    security_schemes: Optional[dict[str, Union[SecurityScheme, Reference]]] = None
    links: Optional[dict[str, Union[Link, Reference]]] = None
    callbacks: Optional[dict[str, Union[Callback, Reference]]] = None

@dataclass
class Tag(OpenAPIElement):
    name: str
    description: Optional[str] = None
    external_docs: Optional[ExternalDocs] = None

@dataclass
class Security(OpenAPIElement):
    requirements: list[SecurityRequirement]
    optional: bool = False

@dataclass
class OpenAPI(OpenAPIRoot):
    openapi: str = "3.0.3"
    info: Optional[Info] = None
    paths: Optional[dict[str, PathItem]] = None
    servers: Optional[list[Server]] = None
    components: Optional[Components] = None
    tags: Optional[list[Tag]] = None
    security: Optional[Security] = None
    external_docs: Optional[ExternalDocs] = None
