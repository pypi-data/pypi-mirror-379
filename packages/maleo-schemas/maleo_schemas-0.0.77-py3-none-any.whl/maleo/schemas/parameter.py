from pydantic import Field
from typing import Annotated, Generic
from maleo.enums.status import ListOfDataStatuses, FULL_DATA_STATUSES
from maleo.mixins.filter import DateFilters
from maleo.mixins.identity import (
    IdentifierTypeT,
    IdentifierValueT,
    IdentifierTypeValue,
)
from maleo.mixins.parameter import (
    Search,
    UseCache,
)
from maleo.mixins.sort import SortColumns
from maleo.mixins.status import DataStatuses
from .operation.action.status import StatusUpdateOperationAction
from .pagination import BaseFlexiblePagination, BaseStrictPagination


class ReadSingleParameter(
    DataStatuses[ListOfDataStatuses],
    UseCache,
    IdentifierTypeValue[IdentifierTypeT, IdentifierValueT],
    Generic[IdentifierTypeT, IdentifierValueT],
):
    statuses: Annotated[
        ListOfDataStatuses,
        Field(list(FULL_DATA_STATUSES), description="Data statuses", min_length=1),
    ] = list(FULL_DATA_STATUSES)


class BaseReadMultipleParameter(
    SortColumns,
    Search,
    DataStatuses[ListOfDataStatuses],
    DateFilters,
    UseCache,
):
    statuses: Annotated[
        ListOfDataStatuses,
        Field(list(FULL_DATA_STATUSES), description="Data statuses", min_length=1),
    ] = list(FULL_DATA_STATUSES)


class ReadUnpaginatedMultipleParameter(
    BaseFlexiblePagination,
    BaseReadMultipleParameter,
):
    pass


class ReadPaginatedMultipleParameter(
    BaseStrictPagination,
    BaseReadMultipleParameter,
):
    pass


class StatusUpdateParameter(
    StatusUpdateOperationAction,
    IdentifierTypeValue[IdentifierTypeT, IdentifierValueT],
    Generic[IdentifierTypeT, IdentifierValueT],
):
    pass
