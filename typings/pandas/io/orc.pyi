"""
This type stub file was generated by pyright.
"""

from typing import Any
from pandas import DataFrame
from pandas._libs.lib import _NoDefaultDoNotUse
from pandas._typing import DtypeBackend, FilePath, HashableT, ReadBuffer

def read_orc(path: FilePath | ReadBuffer[bytes], columns: list[HashableT] | None = ..., dtype_backend: DtypeBackend | _NoDefaultDoNotUse = ..., filesystem: Any | None = ..., **kwargs: Any) -> DataFrame:
    ...

