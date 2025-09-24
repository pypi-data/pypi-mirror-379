import collections
from abc import ABCMeta, abstractmethod
from typing import *

import setdoc
from datarepr import datarepr
from scaevola import Scaevola
from unhash import unhash

from datahold._utils import deco

__all__ = [
    "DataABC",
    "DataDict",
    "DataList",
    "DataSet",
    "HoldABC",
    "HoldDict",
    "HoldList",
    "HoldSet",
    "OkayABC",
    "OkayDict",
    "OkayList",
    "OkaySet",
]


class DataABC(metaclass=ABCMeta):
    __slots__ = ()

    __hash__ = unhash

    @abstractmethod
    @setdoc.basic
    def __init__(self: Self, data: Any) -> None: ...

    @classmethod
    def __subclasshook__(cls: type, other: type, /) -> bool:
        "This magic classmethod can be overwritten for a custom subclass check."
        return NotImplemented

    @property
    @abstractmethod
    def data(self: Self) -> Any: ...


@deco.ClassFuncDecorator(
    "__contains__",
    "__delitem__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getitem__",
    "__gt__",
    "__ior__",
    "__iter__",
    "__le__",
    "__len__",
    "__lt__",
    "__or__",
    "__repr__",
    "__reversed__",
    "__ror__",
    "__setitem__",
    "__str__",
    "clear",
    "copy",
    "get",
    "items",
    "keys",
    "pop",
    "popitem",
    "setdefault",
    "update",
    "values",
)
@deco.ClassInitDecorator()
class DataDict(DataABC, collections.abc.MutableMapping):
    __slots__ = ()
    data: dict


@deco.ClassFuncDecorator(
    "__add__",
    "__contains__",
    "__delitem__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getitem__",
    "__gt__",
    "__iadd__",
    "__imul__",
    "__iter__",
    "__le__",
    "__len__",
    "__lt__",
    "__mul__",
    "__repr__",
    "__reversed__",
    "__rmul__",
    "__setitem__",
    "__str__",
    "append",
    "clear",
    "copy",
    "count",
    "extend",
    "index",
    "insert",
    "pop",
    "remove",
    "reverse",
    "sort",
)
@deco.ClassInitDecorator()
class DataList(DataABC, collections.abc.MutableSequence):
    __slots__ = ()
    data: list


@deco.ClassFuncDecorator(
    "__and__",
    "__contains__",
    "__eq__",
    "__format__",
    "__ge__",
    "__gt__",
    "__iand__",
    "__ior__",
    "__isub__",
    "__iter__",
    "__ixor__",
    "__le__",
    "__len__",
    "__lt__",
    "__or__",
    "__rand__",
    "__repr__",
    "__ror__",
    "__rsub__",
    "__rxor__",
    "__str__",
    "__sub__",
    "__xor__",
    "add",
    "clear",
    "copy",
    "difference",
    "difference_update",
    "discard",
    "intersection",
    "intersection_update",
    "isdisjoint",
    "issubset",
    "issuperset",
    "pop",
    "remove",
    "symmetric_difference",
    "symmetric_difference_update",
    "union",
    "update",
)
@deco.ClassInitDecorator()
class DataSet(DataABC, collections.abc.MutableSet):
    __slots__ = ()
    data: set


class HoldABC(DataABC):
    __slots__ = ("_data",)


@deco.ClassDataDecorator()
class HoldDict(DataDict, HoldABC):
    __slots__ = ()
    data: dict


@deco.ClassDataDecorator()
class HoldList(DataList, HoldABC):
    __slots__ = ()
    data: list


@deco.ClassDataDecorator()
class HoldSet(DataSet, HoldABC):
    __slots__ = ()
    data: set


class OkayABC(Scaevola, HoldABC):
    __slots__ = ()

    @setdoc.basic
    def __bool__(self: Self, /) -> bool:
        return bool(self._data)

    @setdoc.basic
    def __contains__(self: Self, other: Any, /) -> bool:
        return other in self._data

    @setdoc.basic
    def __eq__(self: Self, other: Any, /) -> bool:
        if type(self) is type(other):
            return self._data == other._data
        try:
            opp: Self = type(self)(other)
        except:
            return False
        else:
            return self._data == opp._data

    @setdoc.basic
    def __format__(self: Self, format_spec: Any = "", /) -> str:
        return format(str(self), str(format_spec))

    @setdoc.basic
    def __getitem__(self: Self, key: Any, /) -> Any:
        return self._data[key]

    @setdoc.basic
    def __gt__(self: Self, other: Any, /) -> bool:
        return not (self == other) and (self >= other)

    @setdoc.basic
    def __iter__(self: Self, /) -> Iterator:
        return iter(self._data)

    @setdoc.basic
    def __le__(self: Self, other: Any, /) -> bool:
        return self._data <= type(self._data)(other)

    @setdoc.basic
    def __len__(self: Self, /) -> int:
        return len(self._data)

    @setdoc.basic
    def __lt__(self: Self, other: Any, /) -> bool:
        return not (self == other) and (self <= other)

    @setdoc.basic
    def __ne__(self: Self, other: Any, /) -> bool:
        return not (self == other)

    @setdoc.basic
    def __repr__(self: Self, /) -> str:
        return datarepr(type(self).__name__, self._data)

    @setdoc.basic
    def __reversed__(self: Self, /) -> Self:
        return type(self)(reversed(self.data))

    def __sorted__(self: Self, /, **kwargs: Any) -> Self:
        "This magic method implements sorted(self, **kwargs)."
        data: Any = sorted(self.data)
        ans: Self = type(self)(data)
        return ans

    @setdoc.basic
    def __str__(self: Self, /) -> str:
        return repr(self)

    def copy(self: Self, /) -> Self:
        "This method creates a new holder with equivalent data."
        return type(self)(self.data)


class OkayDict(OkayABC, HoldDict):
    __slots__ = ()

    @setdoc.basic
    def __init__(self: Self, data: Iterable = (), /, **kwargs: Any) -> None:
        self.data = dict(data, **kwargs)

    @setdoc.basic
    def __or__(self: Self, other: Any, /) -> Self:
        return type(self)(self._data | dict(other))

    @classmethod
    def fromkeys(cls: type, iterable: Iterable, value: Any = None, /) -> Self:
        "This classmethod creates a new instance with keys from iterable and values set to value."
        return cls(dict.fromkeys(iterable, value))

    def get(self: Self, /, *args: Any) -> Any:
        "This method returns self[key] if key is in the dictionary, and default otherwise."
        return self._data.get(*args)

    def items(self: Self, /) -> collections.abc.ItemsView:
        "This method returns a view of the items of the current instance."
        return self._data.items()

    def keys(self: Self, /) -> collections.abc.KeysView:
        "This method returns a view of the keys of the current instance."
        return self._data.keys()

    def values(self: Self, /) -> collections.abc.ValuesView:
        "This method returns a view of the values of the current instance."
        return self._data.values()


class OkayList(OkayABC, HoldList):
    __slots__ = ()

    @setdoc.basic
    def __add__(self: Self, other: Any, /) -> Self:
        return type(self)(self._data + list(other))

    @setdoc.basic
    def __init__(self: Self, data: Iterable = ()) -> None:
        self.data = data

    @setdoc.basic
    def __mul__(self: Self, value: SupportsIndex, /) -> Self:
        return type(self)(self.data * value)

    @setdoc.basic
    def __rmul__(self: Self, value: SupportsIndex, /) -> Self:
        return self * value

    def count(self: Self, value: Any, /) -> int:
        "This method returns the number of occurences of value."
        return self._data.count(value)

    def index(self: Self, /, *args: Any) -> int:
        "This method returns the index of the first occurence of value, or raises a ValueError if value is not present."
        return self._data.index(*args)


class OkaySet(OkayABC, HoldSet):
    __slots__ = ()

    @setdoc.basic
    def __and__(self: Self, other: Any, /) -> Self:
        return type(self)(self._data & set(other))

    @setdoc.basic
    def __init__(self: Self, data: Iterable = ()) -> None:
        self.data = data

    @setdoc.basic
    def __or__(self: Self, other: Any, /) -> Self:
        return type(self)(self._data | set(other))

    @setdoc.basic
    def __sub__(self: Self, other: Any, /) -> Self:
        return type(self)(self._data - set(other))

    @setdoc.basic
    def __xor__(self: Self, other: Any, /) -> Self:
        return type(self)(self._data ^ set(other))

    def difference(self: Self, /, *others: Any) -> Self:
        "This method returns a copy of self without the items also found in any of the others."
        return type(self)(self._data.difference(*others))

    def intersection(self: Self, /, *others: Any) -> set:
        "This method returns a copy of self without the items not found in all of the others."
        return type(self)(self._data.intersection(*others))

    def isdisjoint(self: Self, other: Any, /) -> bool:
        "This method determines if self and other have no intersection."
        return self._data.isdisjoint(other)

    def issubset(self: Self, other: Any, /) -> bool:
        "This method determines if self is a subset of other."
        return self._data.issubset(other)

    def issuperset(self: Self, other: Any, /) -> bool:
        "This method determines if self is a superset of other."
        return self._data.issuperset(other)

    def symmetric_difference(self: Self, other: Any, /) -> Self:
        "This method returns the symmetric difference between self and other."
        return type(self)(self._data.symmetric_difference(other))

    def union(self: Self, /, *others: Any) -> Self:
        "This method returns a copy of self with all the items in the others added."
        return type(self)(self._data.union(*others))
