from typing import Generic, Literal
from ..connection import OptionalConnectionContext
from ..error import (
    OptionalAnyErrorT,
    AnyErrorT,
)
from ..mixins.general import SuccessT
from ..response import ResponseT, ErrorResponseT, SuccessResponseT
from ..security.authentication import OptionalAnyAuthenticationT
from ..security.authorization import OptionalAuthorizationT
from .action.system import SystemOperationAction
from .base import BaseOperation
from .enums import OperationType


class SystemOperation(
    BaseOperation[
        SystemOperationAction,
        None,
        SuccessT,
        OptionalAnyErrorT,
        OptionalConnectionContext,
        OptionalAnyAuthenticationT,
        OptionalAuthorizationT,
        ResponseT,
        None,
    ],
    Generic[
        SuccessT,
        OptionalAnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAuthorizationT,
        ResponseT,
    ],
):
    type: OperationType = OperationType.SYSTEM
    resource: None = None
    response_context: None = None


class FailedSystemOperation(
    SystemOperation[
        Literal[False],
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAuthorizationT,
        ErrorResponseT,
    ],
    Generic[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAuthorizationT, ErrorResponseT
    ],
):
    success: Literal[False] = False


class SuccessfulSystemOperation(
    SystemOperation[
        Literal[True],
        None,
        OptionalAnyAuthenticationT,
        OptionalAuthorizationT,
        SuccessResponseT,
    ],
    Generic[OptionalAnyAuthenticationT, OptionalAuthorizationT, SuccessResponseT],
):
    success: Literal[True] = True
    error: None = None
