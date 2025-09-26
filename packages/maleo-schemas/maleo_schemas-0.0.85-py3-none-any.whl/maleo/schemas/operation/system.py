from typing import Generic, Literal
from ..connection import OptionalConnectionContext
from ..error import (
    OptionalAnyErrorT,
    AnyErrorT,
)
from ..mixins.general import SuccessT
from ..response import ResponseT, ErrorResponseT, SuccessResponseT
from ..security.authentication import OptionalAnyAuthenticationT
from ..security.authorization import OptionalAnyAuthorizationT
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
        OptionalAnyAuthorizationT,
        ResponseT,
        None,
    ],
    Generic[
        SuccessT,
        OptionalAnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
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
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
    Generic[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, ErrorResponseT
    ],
):
    success: Literal[False] = False


class SuccessfulSystemOperation(
    SystemOperation[
        Literal[True],
        None,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        SuccessResponseT,
    ],
    Generic[OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, SuccessResponseT],
):
    success: Literal[True] = True
    error: None = None
