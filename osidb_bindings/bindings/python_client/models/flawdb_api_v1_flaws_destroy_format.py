from enum import Enum


class FlawdbApiV1FlawsDestroyFormat(str, Enum):
    CSV = "csv"
    JSON = "json"
    XML = "xml"

    def __str__(self) -> str:
        return str(self.value)