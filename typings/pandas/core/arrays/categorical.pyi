"""
This type stub file was generated by pyright.
"""

import numpy as np
from collections.abc import Callable, Sequence
from typing import Any, overload
from pandas import Series
from pandas.core.accessor import PandasDelegate as PandasDelegate
from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.base import NoNewAttributesMixin as NoNewAttributesMixin
from pandas.core.indexes.base import Index
from typing_extensions import Self
from pandas._typing import ArrayLike, Dtype, ListLike, Ordered, PositionalIndexerTuple, Scalar, ScalarIndexer, SequenceIndexer, TakeIndexer, np_ndarray_bool, np_ndarray_int
from pandas.core.dtypes.dtypes import CategoricalDtype as CategoricalDtype

def contains(cat, key, container):
    ...

class Categorical(ExtensionArray):
    __array_priority__: int = ...
    def __init__(self, values: ListLike, categories=..., ordered: bool | None = ..., dtype: CategoricalDtype | None = ..., fastpath: bool = ...) -> None:
        ...
    
    @property
    def categories(self):
        ...
    
    @property
    def ordered(self) -> Ordered:
        ...
    
    @property
    def dtype(self) -> CategoricalDtype:
        ...
    
    def astype(self, dtype: Dtype, copy: bool = ...) -> ArrayLike:
        ...
    
    def size(self) -> int:
        ...
    
    def tolist(self) -> list[Scalar]:
        ...
    
    to_list = ...
    @classmethod
    def from_codes(cls, codes: Sequence[int], categories: Index | None = ..., ordered: bool | None = ..., dtype: CategoricalDtype | None = ..., fastpath: bool = ...) -> Categorical:
        ...
    
    @property
    def codes(self) -> np_ndarray_int:
        ...
    
    def set_ordered(self, value) -> Categorical:
        ...
    
    def as_ordered(self) -> Categorical:
        ...
    
    def as_unordered(self) -> Categorical:
        ...
    
    def set_categories(self, new_categories, ordered: bool | None = ..., rename: bool = ...) -> Categorical:
        ...
    
    def rename_categories(self, new_categories) -> Categorical:
        ...
    
    def reorder_categories(self, new_categories, ordered: bool | None = ...) -> Categorical:
        ...
    
    def add_categories(self, new_categories) -> Categorical:
        ...
    
    def remove_categories(self, removals) -> Categorical:
        ...
    
    def remove_unused_categories(self) -> Categorical:
        ...
    
    def map(self, mapper):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    @property
    def shape(self):
        ...
    
    def shift(self, periods=..., fill_value=...):
        ...
    
    def __array__(self, dtype=...) -> np.ndarray:
        ...
    
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        ...
    
    @property
    def T(self):
        ...
    
    @property
    def nbytes(self) -> int:
        ...
    
    def memory_usage(self, deep: bool = ...):
        ...
    
    def searchsorted(self, value, side: str = ..., sorter=...):
        ...
    
    def isna(self) -> np_ndarray_bool:
        ...
    
    def isnull(self) -> np_ndarray_bool:
        ...
    
    def notna(self) -> np_ndarray_bool:
        ...
    
    def notnull(self) -> np_ndarray_bool:
        ...
    
    def dropna(self):
        ...
    
    def value_counts(self, dropna: bool = ...):
        ...
    
    def check_for_ordered(self, op) -> None:
        ...
    
    def argsort(self, *, ascending: bool = ..., kind: str = ..., **kwargs):
        ...
    
    def sort_values(self, *, inplace: bool = ..., ascending: bool = ..., na_position: str = ...):
        ...
    
    def view(self, dtype=...):
        ...
    
    def fillna(self, value=..., method=..., limit=...):
        ...
    
    def take(self, indexer: TakeIndexer, *, allow_fill: bool = ..., fill_value=...) -> Categorical:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self):
        ...
    
    def __contains__(self, key) -> bool:
        ...
    
    @overload
    def __getitem__(self, key: ScalarIndexer) -> Any:
        ...
    
    @overload
    def __getitem__(self, key: SequenceIndexer | PositionalIndexerTuple) -> Self:
        ...
    
    def __setitem__(self, key, value) -> None:
        ...
    
    def min(self, *, skipna: bool = ...):
        ...
    
    def max(self, *, skipna: bool = ...):
        ...
    
    def unique(self):
        ...
    
    def equals(self, other):
        ...
    
    def describe(self):
        ...
    
    def repeat(self, repeats, axis=...):
        ...
    
    def isin(self, values):
        ...
    


class CategoricalAccessor(PandasDelegate, NoNewAttributesMixin):
    def __init__(self, data) -> None:
        ...
    
    @property
    def codes(self) -> Series[int]:
        ...
    
    @property
    def categories(self) -> Index:
        ...
    
    @property
    def ordered(self) -> bool | None:
        ...
    
    def rename_categories(self, new_categories: ListLike | dict[Any, Any] | Callable[[Any], Any]) -> Series:
        ...
    
    def reorder_categories(self, new_categories: ListLike, ordered: bool = ...) -> Series:
        ...
    
    def add_categories(self, new_categories: Scalar | ListLike) -> Series:
        ...
    
    def remove_categories(self, removals: Scalar | ListLike) -> Series:
        ...
    
    def remove_unused_categories(self) -> Series:
        ...
    
    def set_categories(self, new_categories: ListLike, ordered: bool | None = ..., rename: bool = ...) -> Series:
        ...
    
    def as_ordered(self) -> Series:
        ...
    
    def as_unordered(self) -> Series:
        ...
    


