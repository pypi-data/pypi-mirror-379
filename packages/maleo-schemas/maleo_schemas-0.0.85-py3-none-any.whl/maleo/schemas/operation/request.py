from copy import deepcopy
from typing import Any, Generic, Literal, Optional, Type, Union, overload
from uuid import UUID
from ..application import ApplicationContext
from ..connection import ConnectionContext
from ..error import OptionalAnyErrorT, AnyErrorT
from ..mixins.general import SuccessT
from ..pagination import OptionalAnyPagination
from ..response import (
    ResponseContext,
    ResponseT,
    ErrorResponseT,
    AnyDataResponse,
)
from ..security.authentication import OptionalAnyAuthenticationT
from ..security.authorization import OptionalAnyAuthorizationT
from ..security.impersonation import OptionalImpersonation
from .action.resource import (
    AnyResourceOperationActionT,
    CreateResourceOperationAction,
    ReadResourceOperationAction,
    UpdateResourceOperationAction,
    DeleteResourceOperationAction,
    ResourceOperationActions,
    AnyResourceOperationAction,
    Factory as ResourceOperationActionFactory,
)
from .base import BaseOperation
from .context import Context as OperationContext
from .enums import (
    OperationType,
    ResourceOperationType,
    ResourceOperationCreateType,
    ResourceOperationUpdateType,
    ResourceOperationDataUpdateType,
    ResourceOperationStatusUpdateType,
)
from .mixins import Timestamp


class RequestOperation(
    BaseOperation[
        AnyResourceOperationActionT,
        None,
        SuccessT,
        OptionalAnyErrorT,
        ConnectionContext,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ResponseT,
        ResponseContext,
    ],
    Generic[
        AnyResourceOperationActionT,
        SuccessT,
        OptionalAnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ResponseT,
    ],
):
    type: OperationType = OperationType.REQUEST
    resource: None = None


class FailedRequestOperation(
    RequestOperation[
        AnyResourceOperationActionT,
        Literal[False],
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
    Generic[
        AnyResourceOperationActionT,
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
):
    success: Literal[False] = False
    summary: str = "Failed processing request"


class CreateFailedRequestOperation(
    FailedRequestOperation[
        CreateResourceOperationAction,
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
    Generic[
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
):
    pass


class ReadFailedRequestOperation(
    FailedRequestOperation[
        ReadResourceOperationAction,
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
    Generic[
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
):
    pass


class UpdateFailedRequestOperation(
    FailedRequestOperation[
        UpdateResourceOperationAction,
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
    Generic[
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
):
    pass


class DeleteFailedRequestOperation(
    FailedRequestOperation[
        DeleteResourceOperationAction,
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
    Generic[
        AnyErrorT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        ErrorResponseT,
    ],
):
    pass


class SuccessfulRequestOperation(
    RequestOperation[
        AnyResourceOperationActionT,
        Literal[True],
        None,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
        AnyDataResponse[Any, OptionalAnyPagination, Any],
    ],
    Generic[
        AnyResourceOperationActionT,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
    ],
):
    success: Literal[True] = True
    error: None = None
    summary: str = "Successfully processed request"


class CreateSuccessfulRequestOperation(
    SuccessfulRequestOperation[
        CreateResourceOperationAction,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
    ],
    Generic[
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
    ],
):
    pass


class ReadSuccessfulRequestOperation(
    SuccessfulRequestOperation[
        ReadResourceOperationAction,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
    ],
    Generic[
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
    ],
):
    pass


class UpdateSuccessfulRequestOperation(
    SuccessfulRequestOperation[
        UpdateResourceOperationAction,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
    ],
    Generic[
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
    ],
):
    pass


class DeleteSuccessfulRequestOperation(
    SuccessfulRequestOperation[
        DeleteResourceOperationAction,
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
    ],
    Generic[
        OptionalAnyAuthenticationT,
        OptionalAnyAuthorizationT,
    ],
):
    pass


class FailedFactory(
    Generic[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, ErrorResponseT
    ]
):
    @overload
    @classmethod
    def operation_cls_from_action(cls, action: CreateResourceOperationAction) -> Type[
        CreateFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_action(cls, action: ReadResourceOperationAction) -> Type[
        ReadFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_action(cls, action: UpdateResourceOperationAction) -> Type[
        UpdateFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_action(cls, action: DeleteResourceOperationAction) -> Type[
        DeleteFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_action(cls, action: AnyResourceOperationAction) -> Union[
        Type[
            CreateFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
        Type[
            ReadFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
        Type[
            UpdateFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
        Type[
            DeleteFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
    ]: ...
    @classmethod
    def operation_cls_from_action(cls, action: AnyResourceOperationAction) -> Union[
        Type[
            CreateFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
        Type[
            ReadFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
        Type[
            UpdateFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
        Type[
            DeleteFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
    ]:
        if isinstance(action, CreateResourceOperationAction):
            operation_cls = CreateFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        elif isinstance(action, ReadResourceOperationAction):
            operation_cls = ReadFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        elif isinstance(action, UpdateResourceOperationAction):
            operation_cls = UpdateFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        elif isinstance(action, DeleteResourceOperationAction):
            operation_cls = DeleteFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        return operation_cls

    @overload
    @classmethod
    def operation_cls_from_type(
        cls,
        type_: Literal[ResourceOperationType.CREATE],
    ) -> Type[
        CreateFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_type(
        cls,
        type_: Literal[ResourceOperationType.READ],
    ) -> Type[
        ReadFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_type(
        cls,
        type_: Literal[ResourceOperationType.UPDATE],
    ) -> Type[
        UpdateFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_type(
        cls,
        type_: Literal[ResourceOperationType.DELETE],
    ) -> Type[
        DeleteFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ]
    ]: ...
    @classmethod
    def operation_cls_from_type(
        cls,
        type_: ResourceOperationType,
    ) -> Union[
        Type[
            CreateFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
        Type[
            ReadFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
        Type[
            UpdateFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
        Type[
            DeleteFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        ],
    ]:
        if type_ is ResourceOperationType.CREATE:
            operation_cls = CreateFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        elif type_ is ResourceOperationType.READ:
            operation_cls = ReadFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        elif type_ is ResourceOperationType.UPDATE:
            operation_cls = UpdateFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        elif type_ is ResourceOperationType.DELETE:
            operation_cls = DeleteFailedRequestOperation[
                AnyErrorT,
                OptionalAnyAuthenticationT,
                OptionalAnyAuthorizationT,
                ErrorResponseT,
            ]
        return operation_cls

    @overload
    @classmethod
    def generate(
        cls,
        action: CreateResourceOperationAction,
        *,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> CreateFailedRequestOperation[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, ErrorResponseT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        action: ReadResourceOperationAction,
        *,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> ReadFailedRequestOperation[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, ErrorResponseT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        action: UpdateResourceOperationAction,
        *,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> UpdateFailedRequestOperation[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, ErrorResponseT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        action: DeleteResourceOperationAction,
        *,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> DeleteFailedRequestOperation[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, ErrorResponseT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        action: AnyResourceOperationAction,
        *,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> Union[
        CreateFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
        ReadFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
        UpdateFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
        DeleteFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        *,
        type_: Literal[ResourceOperationType.CREATE],
        create_type: Optional[ResourceOperationCreateType] = ...,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> CreateFailedRequestOperation[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, ErrorResponseT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        *,
        type_: Literal[ResourceOperationType.READ],
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> ReadFailedRequestOperation[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, ErrorResponseT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        *,
        type_: Literal[ResourceOperationType.UPDATE],
        update_type: Optional[ResourceOperationUpdateType] = ...,
        data_update_type: Optional[ResourceOperationDataUpdateType] = ...,
        status_update_type: Optional[ResourceOperationStatusUpdateType] = ...,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> UpdateFailedRequestOperation[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, ErrorResponseT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        *,
        type_: Literal[ResourceOperationType.DELETE],
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> DeleteFailedRequestOperation[
        AnyErrorT, OptionalAnyAuthenticationT, OptionalAnyAuthorizationT, ErrorResponseT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        *,
        type_: ResourceOperationType,
        create_type: Optional[ResourceOperationCreateType] = None,
        update_type: Optional[ResourceOperationUpdateType] = None,
        data_update_type: Optional[ResourceOperationDataUpdateType] = None,
        status_update_type: Optional[ResourceOperationStatusUpdateType] = None,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> Union[
        CreateFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
        ReadFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
        UpdateFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
        DeleteFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
    ]: ...
    @classmethod
    def generate(
        cls,
        action: Optional[AnyResourceOperationAction] = None,
        *,
        type_: Optional[ResourceOperationType] = None,
        create_type: Optional[ResourceOperationCreateType] = None,
        update_type: Optional[ResourceOperationUpdateType] = None,
        data_update_type: Optional[ResourceOperationDataUpdateType] = None,
        status_update_type: Optional[ResourceOperationStatusUpdateType] = None,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        error: AnyErrorT,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: ErrorResponseT,
        response_context: ResponseContext,
    ) -> Union[
        CreateFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
        ReadFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
        UpdateFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
        DeleteFailedRequestOperation[
            AnyErrorT,
            OptionalAnyAuthenticationT,
            OptionalAnyAuthorizationT,
            ErrorResponseT,
        ],
    ]:
        if (action is None and type_ is None) or (
            action is not None and type_ is not None
        ):
            raise ValueError("Only either 'action' or 'type' must be given")

        common_kwargs = {
            "application_context": application_context,
            "id": id,
            "context": context,
            "timestamp": timestamp,
            "summary": summary,
            "error": error,
            "connection_context": connection_context,
            "authentication": authentication,
            "authorization": authorization,
            "impersonation": impersonation,
            "response": response,
            "response_context": response_context,
        }

        if action is not None:
            if not isinstance(action, ResourceOperationActions):
                raise ValueError(f"Invalid 'action' type: '{type(action)}'")

            kwargs = deepcopy(common_kwargs)
            kwargs["action"] = action

            return cls.operation_cls_from_action(action).model_validate(kwargs)

        elif type_ is not None:
            action = ResourceOperationActionFactory.generate(
                type_,
                create_type=create_type,
                update_type=update_type,
                data_update_type=data_update_type,
                status_update_type=status_update_type,
            )
            kwargs = deepcopy(common_kwargs)
            kwargs["action"] = action
            return cls.operation_cls_from_type(type_).model_validate(kwargs)

        # This should never happen due to initial validation,
        # but type checker needs to see all paths covered
        raise ValueError("Neither 'action' nor 'type' provided")


class SuccessfulFactory(Generic[OptionalAnyAuthenticationT, OptionalAnyAuthorizationT]):
    @overload
    @classmethod
    def operation_cls_from_action(
        cls, action: CreateResourceOperationAction
    ) -> Type[
        CreateSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_action(
        cls, action: ReadResourceOperationAction
    ) -> Type[
        ReadSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_action(
        cls, action: UpdateResourceOperationAction
    ) -> Type[
        UpdateSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_action(
        cls, action: DeleteResourceOperationAction
    ) -> Type[
        DeleteSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_action(cls, action: AnyResourceOperationAction) -> Union[
        Type[
            CreateSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
        Type[
            ReadSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
        Type[
            UpdateSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
        Type[
            DeleteSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
    ]: ...
    @classmethod
    def operation_cls_from_action(cls, action: AnyResourceOperationAction) -> Union[
        Type[
            CreateSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
        Type[
            ReadSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
        Type[
            UpdateSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
        Type[
            DeleteSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
    ]:
        if isinstance(action, CreateResourceOperationAction):
            operation_cls = CreateSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        elif isinstance(action, ReadResourceOperationAction):
            operation_cls = ReadSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        elif isinstance(action, UpdateResourceOperationAction):
            operation_cls = UpdateSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        elif isinstance(action, DeleteResourceOperationAction):
            operation_cls = DeleteSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        return operation_cls

    @overload
    @classmethod
    def operation_cls_from_type(
        cls,
        type_: Literal[ResourceOperationType.CREATE],
    ) -> Type[
        CreateSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_type(
        cls,
        type_: Literal[ResourceOperationType.READ],
    ) -> Type[
        ReadSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_type(
        cls,
        type_: Literal[ResourceOperationType.UPDATE],
    ) -> Type[
        UpdateSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ]
    ]: ...
    @overload
    @classmethod
    def operation_cls_from_type(
        cls,
        type_: Literal[ResourceOperationType.DELETE],
    ) -> Type[
        DeleteSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ]
    ]: ...
    @classmethod
    def operation_cls_from_type(
        cls,
        type_: ResourceOperationType,
    ) -> Union[
        Type[
            CreateSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
        Type[
            ReadSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
        Type[
            UpdateSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
        Type[
            DeleteSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        ],
    ]:
        if type_ is ResourceOperationType.CREATE:
            operation_cls = CreateSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        elif type_ is ResourceOperationType.READ:
            operation_cls = ReadSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        elif type_ is ResourceOperationType.UPDATE:
            operation_cls = UpdateSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        elif type_ is ResourceOperationType.DELETE:
            operation_cls = DeleteSuccessfulRequestOperation[
                OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
            ]
        return operation_cls

    @overload
    @classmethod
    def generate(
        cls,
        action: CreateResourceOperationAction,
        *,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> CreateSuccessfulRequestOperation[
        OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        action: ReadResourceOperationAction,
        *,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> ReadSuccessfulRequestOperation[
        OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        action: UpdateResourceOperationAction,
        *,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> UpdateSuccessfulRequestOperation[
        OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        action: DeleteResourceOperationAction,
        *,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> DeleteSuccessfulRequestOperation[
        OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        action: AnyResourceOperationAction,
        *,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> Union[
        CreateSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
        ReadSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
        UpdateSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
        DeleteSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        *,
        type_: Literal[ResourceOperationType.CREATE],
        create_type: Optional[ResourceOperationCreateType] = ...,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> CreateSuccessfulRequestOperation[
        OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        *,
        type_: Literal[ResourceOperationType.READ],
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> ReadSuccessfulRequestOperation[
        OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        *,
        type_: Literal[ResourceOperationType.UPDATE],
        update_type: Optional[ResourceOperationUpdateType] = ...,
        data_update_type: Optional[ResourceOperationDataUpdateType] = ...,
        status_update_type: Optional[ResourceOperationStatusUpdateType] = ...,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> UpdateSuccessfulRequestOperation[
        OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        *,
        type_: Literal[ResourceOperationType.DELETE],
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> DeleteSuccessfulRequestOperation[
        OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
    ]: ...
    @overload
    @classmethod
    def generate(
        cls,
        *,
        type_: ResourceOperationType,
        create_type: Optional[ResourceOperationCreateType] = None,
        update_type: Optional[ResourceOperationUpdateType] = None,
        data_update_type: Optional[ResourceOperationDataUpdateType] = None,
        status_update_type: Optional[ResourceOperationStatusUpdateType] = None,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> Union[
        CreateSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
        ReadSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
        UpdateSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
        DeleteSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
    ]: ...
    @classmethod
    def generate(
        cls,
        action: Optional[AnyResourceOperationAction] = None,
        *,
        type_: Optional[ResourceOperationType] = None,
        create_type: Optional[ResourceOperationCreateType] = None,
        update_type: Optional[ResourceOperationUpdateType] = None,
        data_update_type: Optional[ResourceOperationDataUpdateType] = None,
        status_update_type: Optional[ResourceOperationStatusUpdateType] = None,
        application_context: ApplicationContext,
        id: UUID,
        context: OperationContext,
        timestamp: Timestamp,
        summary: str,
        connection_context: ConnectionContext,
        authentication: OptionalAnyAuthenticationT,
        authorization: OptionalAnyAuthorizationT,
        impersonation: OptionalImpersonation = None,
        response: AnyDataResponse[Any, OptionalAnyPagination, Any],
        response_context: ResponseContext,
    ) -> Union[
        CreateSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
        ReadSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
        UpdateSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
        DeleteSuccessfulRequestOperation[
            OptionalAnyAuthenticationT, OptionalAnyAuthorizationT
        ],
    ]:
        if (action is None and type_ is None) or (
            action is not None and type_ is not None
        ):
            raise ValueError("Only either 'action' or 'type' must be given")

        common_kwargs = {
            "application_context": application_context,
            "id": id,
            "context": context,
            "timestamp": timestamp,
            "summary": summary,
            "connection_context": connection_context,
            "authentication": authentication,
            "authorization": authorization,
            "impersonation": impersonation,
            "response": response,
            "response_context": response_context,
        }

        if action is not None:
            if not isinstance(action, ResourceOperationActions):
                raise ValueError(f"Invalid 'action' type: '{type(action)}'")

            kwargs = deepcopy(common_kwargs)
            kwargs["action"] = action

            return cls.operation_cls_from_action(action).model_validate(kwargs)

        if type_ is not None:
            action = ResourceOperationActionFactory.generate(
                type_,
                create_type=create_type,
                update_type=update_type,
                data_update_type=data_update_type,
                status_update_type=status_update_type,
            )
            kwargs = deepcopy(common_kwargs)
            kwargs["action"] = action
            return cls.operation_cls_from_type(type_).model_validate(kwargs)

        # This should never happen due to initial validation,
        # but type checker needs to see all paths covered
        raise ValueError("Neither 'action' nor 'type' provided")
