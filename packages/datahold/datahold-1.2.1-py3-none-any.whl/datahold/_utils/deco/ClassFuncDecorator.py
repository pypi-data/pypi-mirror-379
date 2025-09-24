import abc
from types import FunctionType
from typing import *

from datahold._utils.deco.util import *


class ClassFuncDecorator:
    _funcnames: tuple[str]

    def __call__(self: Self, holdcls: type) -> type:
        name: str
        for name in self._funcnames:
            self.setupHoldFunc(holdcls=holdcls, name=name)
        abc.update_abstractmethods(holdcls)
        return holdcls

    def __init__(self: Self, *funcnames: str) -> None:
        self._funcnames = funcnames

    @classmethod
    def makeHoldFunc(cls: type, *, old: FunctionType) -> Any:
        def new(self: Self, *args: Any, **kwargs: Any) -> Any:
            data: Any = self.data
            ans: Any = old(data, *args, **kwargs)
            self.data = data
            return ans

        new.__doc__ = old.__doc__

        return new

    @classmethod
    def setupHoldFunc(cls: type, holdcls: type, *, name: str) -> None:
        datacls: type = holdcls.__annotations__["data"]
        old: Callable = getattr(datacls, name)
        new: FunctionType = cls.makeHoldFunc(old=old)
        new.__module__ = holdcls.__module__
        new.__name__ = name
        new.__qualname__ = holdcls.__qualname__ + "." + name
        wrap(old=old, new=new, isinit=False)
        setattr(holdcls, name, new)
