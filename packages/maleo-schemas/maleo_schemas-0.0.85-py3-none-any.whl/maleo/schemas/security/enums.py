from enum import StrEnum
from maleo.types.string import ListOfStrings


class Domain(StrEnum):
    TENANT = "tenant"
    SYSTEM = "system"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]
