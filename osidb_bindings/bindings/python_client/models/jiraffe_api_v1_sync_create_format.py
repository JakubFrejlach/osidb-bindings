from enum import Enum


class JiraffeApiV1SyncCreateFormat(str, Enum):
    CSV = "csv"
    JSON = "json"
    XML = "xml"

    def __str__(self) -> str:
        return str(self.value)