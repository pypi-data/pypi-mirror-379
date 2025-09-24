from enum import StrEnum
from maleo.types.string import ListOfStrings


class Status(StrEnum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "CRITICAL"
    OVERLOAD = "OVERLOAD"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]
