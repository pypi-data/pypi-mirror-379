from enum import StrEnum
from fastapi import status, HTTPException, Header
from fastapi.requests import HTTPConnection
from pydantic import BaseModel, Field
from typing import Annotated, Callable, Generic, Optional, TypeVar
from maleo.enums.connection import Header as HeaderEnum
from maleo.types.integer import OptionalInteger
from maleo.types.string import ListOfStrings
from ..mixins.identity import OrganizationId, UserId


class Source(StrEnum):
    HEADER = "header"
    STATE = "state"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


class Impersonation(OrganizationId[OptionalInteger], UserId[int]):
    user_id: Annotated[int, Field(..., description="User's ID", ge=1)]
    organization_id: Annotated[
        OptionalInteger, Field(None, description="Organization's ID", ge=1)
    ] = None

    @classmethod
    def extract(
        cls, source: Source = Source.STATE, *, conn: HTTPConnection
    ) -> Optional["Impersonation"]:
        if source is Source.HEADER:
            user_id = conn.headers.get(HeaderEnum.X_USER_ID, None)
            if user_id is not None:
                user_id = int(user_id)

            organization_id = conn.headers.get(HeaderEnum.X_ORGANIZATION_ID, None)
            if organization_id is not None:
                organization_id = int(organization_id)

            if user_id is not None:
                return cls(
                    user_id=user_id,
                    organization_id=organization_id,
                )

            if organization_id is not None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Organization ID must be None if User ID is None",
                )

            return None
        elif source is Source.STATE:
            impersonation = conn.state.impersonation
            if not isinstance(impersonation, Impersonation):
                return None
            return impersonation

    @classmethod
    def assign_to_state(
        cls,
        conn: HTTPConnection,
        /,
    ):
        impersonation = cls.extract(Source.HEADER, conn=conn)
        conn.state.impersonation = impersonation

    @classmethod
    def as_dependency(
        cls,
        source: Optional[Source] = Source.STATE,
        /,
    ) -> Callable[
        [HTTPConnection, OptionalInteger, OptionalInteger], Optional["Impersonation"]
    ]:
        def dependency(
            conn: HTTPConnection,
            user_id: OptionalInteger = Header(
                None,
                alias=HeaderEnum.X_USER_ID.value,
                description="User's ID",
                ge=1,
            ),
            organization_id: OptionalInteger = Header(
                None,
                alias=HeaderEnum.X_ORGANIZATION_ID.value,
                description="Organization's ID",
                ge=1,
            ),
        ) -> Optional["Impersonation"]:
            if source is None:
                if user_id is not None:
                    return cls(
                        user_id=user_id,
                        organization_id=organization_id,
                    )

                if organization_id is not None:
                    raise HTTPException(
                        status_code=400,
                        detail="Organization ID must be None if User ID is None",
                    )

                return None

            return cls.extract(source, conn=conn)

        return dependency


OptionalImpersonation = Optional[Impersonation]
OptionalImpersonationT = TypeVar("OptionalImpersonationT", bound=OptionalImpersonation)


class ImpersonationMixin(BaseModel, Generic[OptionalImpersonationT]):
    impersonation: OptionalImpersonationT = Field(..., description="Impersonation")
