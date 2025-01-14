# -*- coding: utf-8 -*-
from typing import Union, Callable, Tuple, Optional

from physicsLab import errors
from physicsLab.circuit.wire import crt_Wire, del_Wire, Pin

# 模块化电路的“引脚”，输入输出都是数据
class unitPin:
    __slots__ = ("lib_self", "elementPins")
    def __init__(self, lib_self, *elementPins):
        self.lib_self = lib_self
        self.elementPins: Tuple[Pin] = tuple(elementPins)

    # 通过unionPin[num]来索引单个bit
    def __getitem__(self, item: Union[int, slice]) -> Pin:
        if isinstance(item, int):
            return self.elementPins[item]
        elif isinstance(item, slice):
            return unitPin(self.lib_self, *self.elementPins[item])
        else:
            raise TypeError

    def __sub__(self, other: Union[Pin, "unitPin"]):
        crt_Wires(self, other)
        return other

    def __iter__(self):
        return iter(self.elementPins)

    def __next__(self):
        for i in self.elementPins:
            yield i

def check_TypeUnionPin(func: Callable):
    def result(
        sourcePin: Union[unitPin, Pin],
        targetPin: Union[unitPin, Pin],
        warning_status: Optional[bool] = None,
        *args, **kwargs
    ) -> None:
        if isinstance(sourcePin, Pin):
            sourcePin = unitPin(sourcePin.element_self, sourcePin)
        if isinstance(targetPin, Pin):
            targetPin = unitPin(targetPin.element_self, targetPin)

        if not isinstance(sourcePin, unitPin) or not isinstance(targetPin, unitPin):
            raise TypeError

        if len(sourcePin.elementPins) != len(targetPin.elementPins):
            errors.warning(
                f"The number of {sourcePin.lib_self.__class__.__name__}'s output pin "
                f"is {len(sourcePin.elementPins)}, "
                f"but the number of {targetPin.lib_self.__class__.__name__}'s input pin "
                f"is {len(targetPin.elementPins)}.",
                warning_status=warning_status
            )

        func(sourcePin, targetPin, *args, **kwargs)
    return result

# 为unionPin连接导线，相当于自动对数据进行连接导线
@check_TypeUnionPin
def crt_Wires(sourcePin: Union[unitPin, Pin],
              targetPin: Union[unitPin, Pin],
              warning_status: Optional[bool] = None,
              color="蓝"
              ) -> None:
    for i, o in zip(sourcePin.elementPins, targetPin.elementPins):
        crt_Wire(i, o, color)

# 删除unionPin的导线
@check_TypeUnionPin
def del_Wires(sourcePin: Union[unitPin, Pin],
              targetPin: Union[unitPin, Pin],
              warning_status: Optional[bool] = None,
              ) -> None:
    for i, o in zip(sourcePin.elementPins, targetPin.elementPins):
        del_Wire(i, o)