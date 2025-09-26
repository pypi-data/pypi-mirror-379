import httpx
from abc import ABC, abstractmethod
from collections.abc import Iterable, Sequence
from Crypto.PublicKey.RSA import RsaKey
from datetime import timedelta
from enum import StrEnum
from fastapi import status, HTTPException, Security
from fastapi.security import APIKeyHeader, HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, Field, ValidationError
from starlette.requests import HTTPConnection
from typing import (
    Annotated,
    Callable,
    Generator,
    Generic,
    Literal,
    Optional,
    Self,
    TypeGuard,
    TypeVar,
    Union,
    overload,
)
from maleo.enums.connection import Header
from maleo.types.misc import BytesOrString
from maleo.types.string import ListOfStrings, OptionalString
from .enums import Domain
from .token import TokenV1, TenantToken, SystemToken, AnyToken, is_tenant, is_system


class Scheme(StrEnum):
    API_KEY = "api_key"
    BEARER_TOKEN = "bearer_token"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


SchemeT = TypeVar("SchemeT", bound=Scheme)


class Source(StrEnum):
    HEADER = "header"
    STATE = "state"


class GenericAuthorization(ABC, BaseModel, Generic[SchemeT]):
    scheme: SchemeT = Field(..., description="Authorization's scheme")
    credentials: Annotated[str, Field(..., description="Authorization's credentials")]

    @overload
    @classmethod
    def from_state(
        cls, conn: HTTPConnection, *, auto_error: Literal[False]
    ) -> Optional[Self]: ...
    @overload
    @classmethod
    def from_state(
        cls, conn: HTTPConnection, *, auto_error: Literal[True] = True
    ) -> Self: ...
    @classmethod
    def from_state(
        cls, conn: HTTPConnection, *, auto_error: bool = True
    ) -> Optional[Self]:
        authorization = conn.state.authorization
        if isinstance(authorization, cls):
            return authorization

        if auto_error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or unable to determine authorization in state",
            )

        return None

    @classmethod
    @abstractmethod
    def from_header(
        cls, conn: HTTPConnection, *, auto_error: bool = True
    ) -> Optional[Self]:
        """Extract authorization from Header"""

    @classmethod
    def assign_to_state(
        cls,
        conn: HTTPConnection,
        /,
    ):
        authorization = cls.from_header(conn, auto_error=False)
        conn.state.authorization = authorization

    @overload
    @classmethod
    def extract(
        cls, conn: HTTPConnection, *, auto_error: Literal[False]
    ) -> Optional[Self]: ...
    @overload
    @classmethod
    def extract(
        cls, conn: HTTPConnection, *, auto_error: Literal[True] = True
    ) -> Self: ...
    @classmethod
    def extract(
        cls, conn: HTTPConnection, *, auto_error: bool = True
    ) -> Optional[Self]:
        authorization = cls.from_state(conn, auto_error=auto_error)
        if authorization is not None:
            return authorization

        authorization = cls.from_header(conn, auto_error=auto_error)
        if authorization is not None:
            return authorization

        if auto_error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or unable to determine authorization",
            )

        return None

    @overload
    @classmethod
    def as_dependency(
        cls, *, auto_error: Literal[False]
    ) -> Callable[..., Optional[Self]]: ...
    @overload
    @classmethod
    def as_dependency(
        cls, *, auto_error: Literal[True] = True
    ) -> Callable[..., Self]: ...
    @classmethod
    def as_dependency(cls, *, auto_error: bool = True) -> Union[
        Callable[
            [HTTPConnection, Optional[HTTPAuthorizationCredentials], OptionalString],
            Optional[Self],
        ],
        Callable[
            [HTTPConnection, Optional[HTTPAuthorizationCredentials], OptionalString],
            Self,
        ],
    ]:
        def dependency(
            conn: HTTPConnection,
            # These are for documentation purpose only
            bearer: Annotated[
                Optional[HTTPAuthorizationCredentials],
                Security(HTTPBearer(auto_error=False)),
            ],
            api_key: Annotated[
                OptionalString,
                Security(APIKeyHeader(name=Header.X_API_KEY.value, auto_error=False)),
            ],
        ) -> Optional[Self]:
            return cls.extract(conn, auto_error=auto_error)

        return dependency


class APIKeyAuthorization(GenericAuthorization[Literal[Scheme.API_KEY]]):
    scheme: Annotated[
        Literal[Scheme.API_KEY],
        Field(Scheme.API_KEY, description="Authorization's scheme"),
    ] = Scheme.API_KEY

    @overload
    @classmethod
    def from_header(
        cls, conn: HTTPConnection, *, auto_error: Literal[False]
    ) -> Optional[Self]: ...
    @overload
    @classmethod
    def from_header(
        cls, conn: HTTPConnection, *, auto_error: Literal[True] = True
    ) -> Self: ...
    @classmethod
    def from_header(
        cls, conn: HTTPConnection, *, auto_error: bool = True
    ) -> Optional[Self]:
        api_key = conn.headers.get(Header.X_API_KEY)
        if api_key is not None:
            return cls(scheme=Scheme.API_KEY, credentials=api_key)

        if auto_error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid or unable to determine authorization from {Header.X_API_KEY} Header",
            )

        return None


class BearerTokenAuthorization(GenericAuthorization[Literal[Scheme.BEARER_TOKEN]]):
    scheme: Annotated[
        Literal[Scheme.BEARER_TOKEN],
        Field(Scheme.BEARER_TOKEN, description="Authorization's scheme"),
    ] = Scheme.BEARER_TOKEN

    @overload
    @classmethod
    def from_header(
        cls, conn: HTTPConnection, *, auto_error: Literal[False]
    ) -> Optional[Self]: ...
    @overload
    @classmethod
    def from_header(
        cls, conn: HTTPConnection, *, auto_error: Literal[True] = True
    ) -> Self: ...
    @classmethod
    def from_header(
        cls, conn: HTTPConnection, *, auto_error: bool = True
    ) -> Optional[Self]:
        token = conn.headers.get(Header.AUTHORIZATION.value, "")
        scheme, _, credentials = token.partition(" ")
        if token and scheme and credentials and scheme.lower() == "bearer":
            return cls(scheme=Scheme.BEARER_TOKEN, credentials=credentials)

        if auto_error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid or unable to determine authorization from {Header.AUTHORIZATION} Header",
            )

        return None

    @overload
    def parse_token(
        self,
        domain: Literal[Domain.TENANT],
        *,
        key: Union[RsaKey, BytesOrString],
        audience: str | Iterable[str] | None = None,
        subject: OptionalString = None,
        issuer: str | Sequence[str] | None = None,
        leeway: float | timedelta = 0,
    ) -> TenantToken: ...
    @overload
    def parse_token(
        self,
        domain: Literal[Domain.SYSTEM],
        *,
        key: Union[RsaKey, BytesOrString],
        audience: str | Iterable[str] | None = None,
        subject: OptionalString = None,
        issuer: str | Sequence[str] | None = None,
        leeway: float | timedelta = 0,
    ) -> SystemToken: ...
    @overload
    def parse_token(
        self,
        domain: None = None,
        *,
        key: Union[RsaKey, BytesOrString],
        audience: str | Iterable[str] | None = None,
        subject: OptionalString = None,
        issuer: str | Sequence[str] | None = None,
        leeway: float | timedelta = 0,
    ) -> AnyToken: ...
    def parse_token(
        self,
        domain: Optional[Domain] = None,
        *,
        key: Union[RsaKey, BytesOrString],
        audience: str | Iterable[str] | None = None,
        subject: OptionalString = None,
        issuer: str | Sequence[str] | None = None,
        leeway: float | timedelta = 0,
    ) -> AnyToken:
        validated_token = None
        models = (TokenV1, TenantToken, SystemToken)
        for model in models:
            try:
                validated_token = model.from_string(
                    self.credentials,
                    key=key,
                    audience=audience,
                    subject=subject,
                    issuer=issuer,
                    leeway=leeway,
                )
            except ValidationError:
                continue
        if validated_token is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Failed parsing token from bearer token authorization",
            )

        if isinstance(validated_token, (TenantToken, SystemToken)):
            token = validated_token
        else:
            if validated_token.sr == "administrator":
                if (
                    validated_token.o_i is not None
                    or validated_token.o_uu is not None
                    or validated_token.o_k is not None
                    or validated_token.o_ot is not None
                    or validated_token.uor is not None
                ):
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="All organization-related claims must be None for System token",
                    )
                token = SystemToken(
                    iss=validated_token.iss,
                    sub=validated_token.u_uu,
                    aud=None,
                    exp=validated_token.exp,
                    iat=validated_token.iat,
                    r=["administrator", "user"],
                )
            elif validated_token.sr == "user":
                if (
                    validated_token.o_i is None
                    or validated_token.o_uu is None
                    or validated_token.o_k is None
                    or validated_token.o_ot is None
                    or validated_token.uor is None
                ):
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="All organization-related claims can not be None for Tenant token",
                    )
                token = TenantToken(
                    iss=validated_token.iss,
                    sub=validated_token.u_uu,
                    aud=None,
                    exp=validated_token.exp,
                    iat=validated_token.iat,
                    o=validated_token.o_uu,
                    r=validated_token.uor,
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=f"Claim 'sr' can only be either 'administrator' or 'user' but received {validated_token.sr}",
                )

        if domain is None:
            return token
        elif domain is Domain.TENANT:
            if not is_tenant(token):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Failed parsing tenant token from bearer token authorization",
                )
            return token
        elif domain is Domain.SYSTEM:
            if not is_system(token):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Failed parsing system token from bearer token authorization",
                )
            return token


AnyAuthorization = Union[BearerTokenAuthorization, APIKeyAuthorization]

AnyAuthorizationT = TypeVar("AnyAuthorizationT", bound=AnyAuthorization)
OptionalAnyAuthorization = Optional[AnyAuthorization]
OptionalAnyAuthorizationT = TypeVar(
    "OptionalAnyAuthorizationT", bound=OptionalAnyAuthorization
)


def is_bearer_token(
    authorization: AnyAuthorization,
) -> TypeGuard[BearerTokenAuthorization]:
    return (
        isinstance(authorization, BearerTokenAuthorization)
        and authorization.scheme is Scheme.BEARER_TOKEN
    )


def is_api_key(authorization: AnyAuthorization) -> TypeGuard[APIKeyAuthorization]:
    return (
        isinstance(authorization, APIKeyAuthorization)
        and authorization.scheme is Scheme.API_KEY
    )


class AuthorizationMixin(BaseModel, Generic[OptionalAnyAuthorizationT]):
    authorization: OptionalAnyAuthorizationT = Field(
        ...,
        description="Authorization",
    )


class APIKeyAuth(httpx.Auth):
    def __init__(self, api_key: str) -> None:
        self._auth_header = self._build_auth_header(api_key)

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers[Header.X_API_KEY.value] = self._auth_header
        yield request

    def _build_auth_header(self, api_key: str) -> str:
        return api_key


class BearerTokenAuth(httpx.Auth):
    def __init__(self, token: str) -> None:
        self._auth_header = self._build_auth_header(token)

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers[Header.AUTHORIZATION] = self._auth_header
        yield request

    def _build_auth_header(self, token: str) -> str:
        return f"Bearer {token}"


AnyHTTPXAuthorization = Union[APIKeyAuth, BearerTokenAuth]


class Factory:
    @overload
    @classmethod
    def extract(
        cls,
        scheme: Literal[Scheme.API_KEY],
        source: Optional[Source] = None,
        *,
        conn: HTTPConnection,
        auto_error: Literal[False],
    ) -> Optional[APIKeyAuthorization]: ...
    @overload
    @classmethod
    def extract(
        cls,
        scheme: Literal[Scheme.BEARER_TOKEN],
        source: Optional[Source] = None,
        *,
        conn: HTTPConnection,
        auto_error: Literal[False],
    ) -> Optional[BearerTokenAuthorization]: ...
    @overload
    @classmethod
    def extract(
        cls,
        scheme: Literal[Scheme.API_KEY],
        source: Optional[Source] = None,
        *,
        conn: HTTPConnection,
        auto_error: Literal[True] = True,
    ) -> APIKeyAuthorization: ...
    @overload
    @classmethod
    def extract(
        cls,
        scheme: Literal[Scheme.BEARER_TOKEN],
        source: Optional[Source] = None,
        *,
        conn: HTTPConnection,
        auto_error: Literal[True] = True,
    ) -> BearerTokenAuthorization: ...
    @classmethod
    def extract(
        cls,
        scheme: Scheme,
        source: Optional[Source] = None,
        *,
        conn: HTTPConnection,
        auto_error: bool = True,
    ) -> OptionalAnyAuthorization:
        if scheme is Scheme.API_KEY:
            if source is not None:
                return APIKeyAuthorization.extract(conn, auto_error=auto_error)
            elif source is Source.HEADER:
                return APIKeyAuthorization.from_header(conn, auto_error=auto_error)
            elif source is Source.STATE:
                return APIKeyAuthorization.from_state(conn, auto_error=auto_error)
        elif scheme is Scheme.BEARER_TOKEN:
            if source is not None:
                return BearerTokenAuthorization.extract(conn, auto_error=auto_error)
            elif source is Source.HEADER:
                return BearerTokenAuthorization.from_header(conn, auto_error=auto_error)
            elif source is Source.STATE:
                return BearerTokenAuthorization.from_state(conn, auto_error=auto_error)

    @overload
    @classmethod
    def as_dependency(
        cls, scheme: Literal[Scheme.API_KEY], *, auto_error: Literal[False]
    ) -> Callable[
        [HTTPConnection, Optional[HTTPAuthorizationCredentials], OptionalString],
        Optional[APIKeyAuthorization],
    ]: ...
    @overload
    @classmethod
    def as_dependency(
        cls, scheme: Literal[Scheme.BEARER_TOKEN], *, auto_error: Literal[False]
    ) -> Callable[
        [HTTPConnection, Optional[HTTPAuthorizationCredentials], OptionalString],
        Optional[BearerTokenAuthorization],
    ]: ...
    @overload
    @classmethod
    def as_dependency(
        cls, scheme: Literal[Scheme.API_KEY], *, auto_error: Literal[True] = True
    ) -> Callable[
        [HTTPConnection, Optional[HTTPAuthorizationCredentials], OptionalString],
        APIKeyAuthorization,
    ]: ...
    @overload
    @classmethod
    def as_dependency(
        cls, scheme: Literal[Scheme.BEARER_TOKEN], *, auto_error: Literal[True] = True
    ) -> Callable[
        [HTTPConnection, Optional[HTTPAuthorizationCredentials], OptionalString],
        BearerTokenAuthorization,
    ]: ...
    @classmethod
    def as_dependency(cls, scheme: Scheme, *, auto_error: bool = True) -> Union[
        Callable[
            [HTTPConnection, Optional[HTTPAuthorizationCredentials], OptionalString],
            OptionalAnyAuthorization,
        ],
        Callable[
            [HTTPConnection, Optional[HTTPAuthorizationCredentials], OptionalString],
            AnyAuthorization,
        ],
    ]:
        if scheme is Scheme.API_KEY:
            return APIKeyAuthorization.as_dependency(auto_error=auto_error)
        elif scheme is Scheme.BEARER_TOKEN:
            return BearerTokenAuthorization.as_dependency(auto_error=auto_error)

    @overload
    @classmethod
    def httpx_auth(
        cls,
        scheme: Literal[Scheme.API_KEY],
        *,
        authorization: Union[str, APIKeyAuthorization],
    ) -> APIKeyAuth: ...
    @overload
    @classmethod
    def httpx_auth(
        cls,
        scheme: Literal[Scheme.BEARER_TOKEN],
        *,
        authorization: Union[str, BearerTokenAuthorization],
    ) -> BearerTokenAuth: ...
    @classmethod
    def httpx_auth(
        cls,
        scheme: Scheme = Scheme.BEARER_TOKEN,
        *,
        authorization: Union[str, AnyAuthorization],
    ) -> AnyHTTPXAuthorization:
        if isinstance(authorization, str):
            token = authorization
        else:
            token = authorization.credentials
        if scheme is Scheme.API_KEY:
            return APIKeyAuth(token)
        elif scheme is Scheme.BEARER_TOKEN:
            return BearerTokenAuth(token)
