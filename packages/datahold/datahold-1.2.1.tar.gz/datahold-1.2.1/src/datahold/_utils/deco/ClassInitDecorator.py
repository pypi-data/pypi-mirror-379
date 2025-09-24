import abc
from types import FunctionType
from typing import *

from datahold._utils.deco.util import *


class ClassInitDecorator:

    def __call__(self: Self, holdcls: type) -> type:
        self.setupInitFunc(holdcls=holdcls)
        abc.update_abstractmethods(holdcls)
        return holdcls

    @classmethod
    def makeInitFunc(cls: type, *, datacls: type) -> FunctionType:
        def new(self: Self, *args: Any, **kwargs: Any) -> Any:
            self.data = datacls(*args, **kwargs)

        new.__doc__ = datacls.__init__.__doc__

        return new

    @classmethod
    def setupInitFunc(cls: type, holdcls: type) -> None:
        datacls: type = holdcls.__annotations__["data"]
        new: FunctionType = cls.makeInitFunc(datacls=datacls)
        old: FunctionType = datacls.__init__
        new.__module__ = holdcls.__module__
        new.__name__ = "__init__"
        new.__qualname__ = holdcls.__qualname__ + ".__init__"
        wrap(old=old, new=new, isinit=True)
        holdcls.__init__ = new
