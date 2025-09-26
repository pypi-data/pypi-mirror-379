from enum import StrEnum
from fastapi import Header
from fastapi.requests import HTTPConnection
from pydantic import BaseModel, Field
from typing import Annotated, Callable, Generic, Optional, TypeVar
from uuid import UUID
from maleo.enums.connection import Header as HeaderEnum
from maleo.types.string import ListOfStrings
from maleo.types.uuid import OptionalUUID


class Source(StrEnum):
    HEADER = "header"
    STATE = "state"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


class Impersonation(BaseModel):
    user_id: Annotated[UUID, Field(..., description="User's ID", ge=1)]
    organization_id: Annotated[
        OptionalUUID, Field(None, description="Organization's ID", ge=1)
    ] = None

    @classmethod
    def extract(cls, conn: HTTPConnection) -> Optional["Impersonation"]:
        impersonation = conn.state.impersonation
        if isinstance(impersonation, Impersonation):
            return impersonation

        user_id = conn.headers.get(HeaderEnum.X_USER_ID, None)
        if user_id is not None:
            user_id = UUID(user_id)

        organization_id = conn.headers.get(HeaderEnum.X_ORGANIZATION_ID, None)
        if organization_id is not None:
            organization_id = UUID(organization_id)

        if user_id is not None:
            return cls(
                user_id=user_id,
                organization_id=organization_id,
            )

        return None

    @classmethod
    def assign_to_state(
        cls,
        conn: HTTPConnection,
        /,
    ):
        impersonation = cls.extract(conn)
        conn.state.impersonation = impersonation

    @classmethod
    def as_dependency(
        cls,
    ) -> Callable[
        [HTTPConnection, OptionalUUID, OptionalUUID], Optional["Impersonation"]
    ]:
        def dependency(
            conn: HTTPConnection,
            # These are for documentation purpose only
            user_id: OptionalUUID = Header(
                None,
                alias=HeaderEnum.X_USER_ID.value,
                description="User's ID",
            ),
            organization_id: OptionalUUID = Header(
                None,
                alias=HeaderEnum.X_ORGANIZATION_ID.value,
                description="Organization's ID",
            ),
        ) -> Optional["Impersonation"]:
            return cls.extract(conn)

        return dependency


OptionalImpersonation = Optional[Impersonation]
OptionalImpersonationT = TypeVar("OptionalImpersonationT", bound=OptionalImpersonation)


class ImpersonationMixin(BaseModel, Generic[OptionalImpersonationT]):
    impersonation: OptionalImpersonationT = Field(..., description="Impersonation")
