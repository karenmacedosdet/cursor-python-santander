"""
This type stub file was generated by pyright.
"""

import numpy as np
from typing import overload
from pandas import Index, Series
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from typing_extensions import Self, TypeAlias
from pandas._libs.interval import Interval as Interval, IntervalMixin as IntervalMixin
from pandas._typing import Axis, Scalar, ScalarIndexer, SequenceIndexer, TakeIndexer, np_ndarray_bool

IntervalOrNA: TypeAlias = Interval | float
class IntervalArray(IntervalMixin, ExtensionArray):
    can_hold_na: bool = ...
    def __new__(cls, data, closed=..., dtype=..., copy: bool = ..., verify_integrity: bool = ...):
        ...
    
    @classmethod
    def from_breaks(cls, breaks, closed: str = ..., copy: bool = ..., dtype=...):
        ...
    
    @classmethod
    def from_arrays(cls, left, right, closed: str = ..., copy: bool = ..., dtype=...):
        ...
    
    @classmethod
    def from_tuples(cls, data, closed: str = ..., copy: bool = ..., dtype=...):
        ...
    
    def __iter__(self):
        ...
    
    def __len__(self) -> int:
        ...
    
    @overload
    def __getitem__(self, key: ScalarIndexer) -> IntervalOrNA:
        ...
    
    @overload
    def __getitem__(self, key: SequenceIndexer) -> Self:
        ...
    
    def __setitem__(self, key, value) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def fillna(self, value=..., method=..., limit=...):
        ...
    
    @property
    def dtype(self):
        ...
    
    def astype(self, dtype, copy: bool = ...):
        ...
    
    def copy(self):
        ...
    
    def isna(self):
        ...
    
    @property
    def nbytes(self) -> int:
        ...
    
    @property
    def size(self) -> int:
        ...
    
    def shift(self, periods: int = ..., fill_value: object = ...) -> IntervalArray:
        ...
    
    def take(self: Self, indices: TakeIndexer, *, allow_fill: bool = ..., fill_value=..., axis=..., **kwargs) -> Self:
        ...
    
    def value_counts(self, dropna: bool = ...):
        ...
    
    @property
    def left(self) -> Index:
        ...
    
    @property
    def right(self) -> Index:
        ...
    
    @property
    def closed(self) -> bool:
        ...
    
    def set_closed(self, closed):
        ...
    
    @property
    def length(self) -> Index:
        ...
    
    @property
    def mid(self) -> Index:
        ...
    
    @property
    def is_non_overlapping_monotonic(self) -> bool:
        ...
    
    def __array__(self, dtype=...) -> np.ndarray:
        ...
    
    def __arrow_array__(self, type=...):
        ...
    
    def to_tuples(self, na_tuple: bool = ...):
        ...
    
    def repeat(self, repeats, axis: Axis | None = ...):
        ...
    
    @overload
    def contains(self, other: Series) -> Series[bool]:
        ...
    
    @overload
    def contains(self, other: Scalar | ExtensionArray | Index | np.ndarray) -> np_ndarray_bool:
        ...
    
    def overlaps(self, other: Interval) -> bool:
        ...
    


