from enum import StrEnum
from fastapi import status, HTTPException
from fastapi.requests import HTTPConnection
from pydantic import BaseModel, Field
from starlette.authentication import (
    AuthCredentials as StarletteCredentials,
    BaseUser as StarletteUser,
)
from typing import (
    Annotated,
    Callable,
    Generic,
    Literal,
    Optional,
    TypeGuard,
    TypeVar,
    Union,
    overload,
)
from uuid import UUID
from maleo.types.string import (
    ListOfStrings,
    OptionalListOfStrings,
    OptionalSequenceOfStrings,
)
from maleo.types.uuid import OptionalUUID
from .enums import Domain


class ConversionDestination(StrEnum):
    BASE = "base"
    TENANT = "tenant"
    SYSTEM = "system"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


class RequestCredentials(StarletteCredentials):
    def __init__(
        self,
        domain: Optional[Domain] = None,
        user_id: OptionalUUID = None,
        organization_id: OptionalUUID = None,
        roles: OptionalSequenceOfStrings = None,
        scopes: OptionalSequenceOfStrings = None,
    ):
        super().__init__(scopes)
        self.domain = domain
        self.user_id = user_id
        self.organization_id = organization_id
        self.roles = [] if roles is None else list(roles)


class RequestUser(StarletteUser):
    def __init__(
        self, authenticated: bool = False, username: str = "", email: str = ""
    ) -> None:
        self._authenticated = authenticated
        self._username = username
        self._email = email

    @property
    def is_authenticated(self) -> bool:
        return self._authenticated

    @property
    def display_name(self) -> str:
        return self._username

    @property
    def identity(self) -> str:
        return self._email


DomainT = TypeVar("DomainT", bound=Optional[Domain])
UserIdT = TypeVar("UserIdT", bound=OptionalUUID)
OrganizationIdT = TypeVar("OrganizationIdT", bound=OptionalUUID)
RolesT = TypeVar("RolesT", bound=OptionalListOfStrings)
ScopesT = TypeVar("ScopesT", bound=OptionalListOfStrings)


class GenericCredentials(
    BaseModel, Generic[DomainT, UserIdT, OrganizationIdT, RolesT, ScopesT]
):
    domain: DomainT = Field(..., description="Domain")
    user_id: UserIdT = Field(..., description="User")
    organization_id: OrganizationIdT = Field(..., description="Organization")
    roles: RolesT = Field(..., description="Roles")
    scopes: ScopesT = Field(..., description="Scopes")


class BaseCredentials(
    GenericCredentials[
        Optional[Domain],
        OptionalUUID,
        OptionalUUID,
        OptionalListOfStrings,
        OptionalListOfStrings,
    ]
):
    domain: Annotated[Optional[Domain], Field(None, description="Domain")] = None
    user_id: Annotated[OptionalUUID, Field(None, description="User")] = None
    organization_id: Annotated[
        OptionalUUID, Field(None, description="Organization")
    ] = None
    roles: Annotated[OptionalListOfStrings, Field(None, description="Roles")] = None
    scopes: Annotated[OptionalListOfStrings, Field(None, description="Scopes")] = None


class TenantCredentials(
    GenericCredentials[Literal[Domain.TENANT], UUID, UUID, ListOfStrings, ListOfStrings]
):
    domain: Literal[Domain.TENANT] = Domain.TENANT
    user_id: Annotated[UUID, Field(..., description="User")]
    organization_id: Annotated[UUID, Field(..., description="Organization")]
    roles: Annotated[ListOfStrings, Field(..., description="Roles")]
    scopes: Annotated[ListOfStrings, Field(..., description="Scopes")]


class SystemCredentials(
    GenericCredentials[Literal[Domain.SYSTEM], UUID, None, ListOfStrings, ListOfStrings]
):
    domain: Literal[Domain.SYSTEM] = Domain.SYSTEM
    user_id: Annotated[UUID, Field(..., description="User")]
    organization_id: Annotated[None, Field(None, description="Organization")] = None
    roles: Annotated[ListOfStrings, Field(..., description="Roles")]
    scopes: Annotated[ListOfStrings, Field(..., description="Scopes")]


AnyCredentials = Union[BaseCredentials, TenantCredentials, SystemCredentials]
AnyCredentialsT = TypeVar("AnyCredentialsT", bound=AnyCredentials)


class CredentialsMixin(BaseModel, Generic[AnyCredentialsT]):
    credentials: AnyCredentialsT = Field(..., description="Credentials")


IsAuthenticatedT = TypeVar("IsAuthenticatedT", bound=bool)


class GenericUser(BaseModel, Generic[IsAuthenticatedT]):
    is_authenticated: IsAuthenticatedT = Field(..., description="Authenticated")
    display_name: str = Field("", description="Username")
    identity: str = Field("", description="Email")


class BaseUser(GenericUser[bool]):
    is_authenticated: bool = Field(..., description="Authenticated")


class AuthenticatedUser(GenericUser[Literal[True]]):
    is_authenticated: Literal[True] = True


AnyUser = Union[BaseUser, AuthenticatedUser]
AnyUserT = TypeVar("AnyUserT", bound=AnyUser)


class UserMixin(BaseModel, Generic[AnyUserT]):
    user: AnyUserT = Field(..., description="User")


class GenericAuthentication(
    UserMixin[AnyUserT],
    CredentialsMixin[AnyCredentialsT],
    Generic[AnyCredentialsT, AnyUserT],
):
    @classmethod
    def _validate_request_credentials(cls, conn: HTTPConnection):
        if not isinstance(conn.auth, RequestCredentials):
            raise HTTPException(
                status_code=401,
                detail=f"Invalid type of request's credentials: '{type(conn.auth)}'",
            )

    @classmethod
    def _validate_request_user(cls, conn: HTTPConnection):
        if not isinstance(conn.user, RequestUser):
            raise HTTPException(
                status_code=401,
                detail=f"Invalid type of request's user: '{type(conn.user)}'",
            )


class BaseAuthentication(GenericAuthentication[BaseCredentials, BaseUser]):
    @classmethod
    def extract(
        cls,
        conn: HTTPConnection,
        /,
    ) -> "BaseAuthentication":
        try:
            # validate credentials
            cls._validate_request_credentials(conn=conn)
            credentials = BaseCredentials.model_validate(
                conn.auth, from_attributes=True
            )

            # validate user
            cls._validate_request_user(conn=conn)
            user = BaseUser.model_validate(conn.user, from_attributes=True)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Unable to validate {cls.__name__}: '{str(e)}'",
            )

        return cls(credentials=credentials, user=user)

    @classmethod
    def as_dependency(cls) -> Callable[[HTTPConnection], "BaseAuthentication"]:
        """Create a FastAPI dependency for this authentication."""

        def dependency(conn: HTTPConnection) -> "BaseAuthentication":
            return cls.extract(conn)

        return dependency


class TenantAuthentication(GenericAuthentication[TenantCredentials, AuthenticatedUser]):
    @classmethod
    def extract(
        cls,
        conn: HTTPConnection,
        /,
    ) -> "TenantAuthentication":
        try:
            # validate credentials
            cls._validate_request_credentials(conn=conn)
            credentials = TenantCredentials.model_validate(
                conn.auth, from_attributes=True
            )

            # validate user
            cls._validate_request_user(conn=conn)
            user = AuthenticatedUser.model_validate(conn.user, from_attributes=True)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Unable to validate {cls.__name__}: '{str(e)}'",
            )

        return cls(credentials=credentials, user=user)

    @classmethod
    def as_dependency(cls) -> Callable[[HTTPConnection], "TenantAuthentication"]:
        """Create a FastAPI dependency for this authentication."""

        def dependency(conn: HTTPConnection) -> "TenantAuthentication":
            return cls.extract(conn)

        return dependency

    def to_base(self) -> BaseAuthentication:
        return BaseAuthentication.model_validate(self.model_dump())


class SystemAuthentication(GenericAuthentication[SystemCredentials, AuthenticatedUser]):
    @classmethod
    def extract(
        cls,
        conn: HTTPConnection,
        /,
    ) -> "SystemAuthentication":
        try:
            # validate credentials
            cls._validate_request_credentials(conn=conn)
            credentials = SystemCredentials.model_validate(
                conn.auth, from_attributes=True
            )

            # validate user
            cls._validate_request_user(conn=conn)
            user = AuthenticatedUser.model_validate(conn.user, from_attributes=True)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Unable to validate {cls.__name__}: '{str(e)}'",
            )

        return cls(credentials=credentials, user=user)

    @classmethod
    def as_dependency(cls) -> Callable[[HTTPConnection], "SystemAuthentication"]:
        """Create a FastAPI dependency for this authentication."""

        def dependency(conn: HTTPConnection) -> "SystemAuthentication":
            return cls.extract(conn)

        return dependency

    def to_base(self) -> BaseAuthentication:
        return BaseAuthentication.model_validate(self.model_dump())


AuthenticatedAuthentication = Union[TenantAuthentication, SystemAuthentication]
AuthenticatedAuthenticationT = TypeVar(
    "AuthenticatedAuthenticationT", bound=AuthenticatedAuthentication
)
OptionalAuthenticatedAuthentication = Optional[AuthenticatedAuthentication]
OptionalAuthenticatedAuthenticationT = TypeVar(
    "OptionalAuthenticatedAuthenticationT", bound=OptionalAuthenticatedAuthentication
)


AnyAuthentication = Union[
    BaseAuthentication, TenantAuthentication, SystemAuthentication
]
AnyAuthenticationT = TypeVar("AnyAuthenticationT", bound=AnyAuthentication)
OptionalAnyAuthentication = Optional[AnyAuthentication]
OptionalAnyAuthenticationT = TypeVar(
    "OptionalAnyAuthenticationT", bound=OptionalAnyAuthentication
)


def is_authenticated(
    authentication: AnyAuthentication,
) -> TypeGuard[AuthenticatedAuthentication]:
    return (
        authentication.user.is_authenticated
        and authentication.credentials.domain is not None
        and authentication.credentials.user_id is not None
        and authentication.credentials.roles is not None
        and authentication.credentials.scopes is not None
    )


def is_tenant(
    authentication: AnyAuthentication,
) -> TypeGuard[TenantAuthentication]:
    return (
        authentication.user.is_authenticated
        and authentication.credentials.domain is Domain.TENANT
        and authentication.credentials.user_id is not None
        and authentication.credentials.organization_id is not None
        and authentication.credentials.roles is not None
        and authentication.credentials.scopes is not None
    )


def is_system(
    authentication: AnyAuthentication,
) -> TypeGuard[SystemAuthentication]:
    return (
        authentication.user.is_authenticated
        and authentication.credentials.domain is Domain.SYSTEM
        and authentication.credentials.user_id is not None
        and authentication.credentials.organization_id is None
        and authentication.credentials.roles is not None
        and authentication.credentials.scopes is not None
    )


class AuthenticationMixin(BaseModel, Generic[OptionalAnyAuthenticationT]):
    authentication: OptionalAnyAuthenticationT = Field(
        ..., description="Authentication"
    )


class OptionalAuthenticationMixin(BaseModel, Generic[AnyAuthenticationT]):
    authentication: Optional[AnyAuthenticationT] = Field(
        ..., description="Authentication. (Optional)"
    )


class Factory:
    @overload
    @classmethod
    def extract(
        cls,
        domain: Literal[Domain.TENANT],
        *,
        conn: HTTPConnection,
    ) -> TenantAuthentication: ...
    @overload
    @classmethod
    def extract(
        cls,
        domain: Literal[Domain.SYSTEM],
        *,
        conn: HTTPConnection,
    ) -> SystemAuthentication: ...
    @overload
    @classmethod
    def extract(
        cls,
        domain: Domain,
        *,
        conn: HTTPConnection,
    ) -> AuthenticatedAuthentication: ...
    @overload
    @classmethod
    def extract(
        cls,
        domain: None = None,
        *,
        conn: HTTPConnection,
    ) -> BaseAuthentication: ...
    @classmethod
    def extract(
        cls,
        domain: Optional[Domain] = None,
        *,
        conn: HTTPConnection,
    ) -> AnyAuthentication:
        if domain is None:
            return BaseAuthentication.extract(conn)
        elif domain is Domain.TENANT:
            return TenantAuthentication.extract(conn)
        elif domain is Domain.SYSTEM:
            return SystemAuthentication.extract(conn)

    @overload
    @classmethod
    def as_dependency(
        cls,
        domain: Literal[Domain.TENANT],
    ) -> Callable[[HTTPConnection], TenantAuthentication]: ...
    @overload
    @classmethod
    def as_dependency(
        cls,
        domain: Literal[Domain.SYSTEM],
    ) -> Callable[[HTTPConnection], SystemAuthentication]: ...
    @overload
    @classmethod
    def as_dependency(
        cls,
        domain: Domain,
    ) -> Callable[[HTTPConnection], AuthenticatedAuthentication]: ...
    @overload
    @classmethod
    def as_dependency(
        cls,
        domain: None = None,
    ) -> Callable[[HTTPConnection], BaseAuthentication]: ...
    @classmethod
    def as_dependency(
        cls,
        domain: Optional[Domain] = None,
    ) -> Callable[[HTTPConnection], AnyAuthentication]:

        def dependency(conn: HTTPConnection) -> AnyAuthentication:
            return cls.extract(domain, conn=conn)

        return dependency

    @overload
    @classmethod
    def convert(
        cls,
        destination: Literal[ConversionDestination.BASE],
        *,
        authentication: Union[TenantAuthentication, SystemAuthentication],
    ) -> BaseAuthentication: ...
    @overload
    @classmethod
    def convert(
        cls,
        destination: Literal[ConversionDestination.TENANT],
        *,
        authentication: BaseAuthentication,
    ) -> TenantAuthentication: ...
    @overload
    @classmethod
    def convert(
        cls,
        destination: Literal[ConversionDestination.SYSTEM],
        *,
        authentication: BaseAuthentication,
    ) -> BaseAuthentication: ...
    @classmethod
    def convert(
        cls, destination: ConversionDestination, *, authentication: AnyAuthentication
    ) -> AnyAuthentication:
        if destination is ConversionDestination.BASE:
            return BaseAuthentication.model_validate(authentication.model_dump())
        elif destination is ConversionDestination.TENANT:
            if isinstance(authentication, SystemAuthentication):
                raise TypeError(
                    "Failed converting SystemAuthentication to TenantAuthentication",
                    "Both authentications can not be converted into one another",
                )
            return TenantAuthentication.model_validate(authentication.model_dump())
        elif destination is ConversionDestination.SYSTEM:
            if isinstance(authentication, TenantAuthentication):
                raise TypeError(
                    "Failed converting TenantAuthentication to SystemAuthentication",
                    "Both authentications can not be converted into one another",
                )
            return SystemAuthentication.model_validate(authentication.model_dump())
