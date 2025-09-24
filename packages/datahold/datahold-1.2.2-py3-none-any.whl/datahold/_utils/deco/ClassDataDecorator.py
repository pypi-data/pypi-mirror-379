import abc
from typing import *

import setdoc

from datahold._utils.deco.util import *


class ClassDataDecorator:
    def __call__(self: Self, holdcls: type) -> type:
        self.setupDataProperty(holdcls=holdcls)
        abc.update_abstractmethods(holdcls)
        return holdcls

    @classmethod
    def setupDataProperty(cls: type, holdcls: type) -> None:
        datacls: type = holdcls.__annotations__["data"]
        holdcls.data = cls.makeDataProperty(datacls=datacls)

    @classmethod
    def makeDataProperty(cls: type, *, datacls: type) -> property:
        def fget(self: Self) -> Any:
            return datacls(self._data)

        def fset(self: Self, value: Any) -> None:
            self._data = datacls(value)

        def fdel(self: Self) -> None:
            self._data = datacls()

        ans: property = property(
            fget=fget,
            fset=fset,
            fdel=fdel,
            doc=setdoc.getbasicdoc("data"),
        )
        return ans
