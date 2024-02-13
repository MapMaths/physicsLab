# -*- coding: utf-8 -*-
from physicsLab import errors

from physicsLab.experiment import stack_Experiment
from physicsLab.experimentType import experimentType

# 电学元件引脚类, 模电元件引脚无明确的输入输出之分, 因此用这个
class Pin:
    __slots__ = ("element_self", "pinLabel")
    is_input = False
    is_output = False
    def __init__(self, input_self, pinLabel: int) -> None:
        self.element_self = input_self
        self.pinLabel: int = pinLabel

    # 重载减法运算符作为连接导线的语法
    def __sub__(self, obj: "Pin") -> "Pin":
        crt_Wire(self, obj)
        return obj

# 只用于输入的引脚
class InputPin(Pin):
    is_input = True
    def __init__(self, input_self, pinLabel: int) -> None:
        super().__init__(input_self, pinLabel)

# 只用于输出的引脚
class OutputPin(Pin):
    is_output = True
    def __init__(self, input_self, pinLabel: int) -> None:
        super().__init__(input_self, pinLabel)

# 检查函数参数是否是导线
def _check_typeWire(func: callable):
    def result(SourcePin: Pin, TargetPin: Pin, *args, **kwargs) -> None:
        if not (
                isinstance(SourcePin, Pin) and
                isinstance(TargetPin, Pin)
        ):
            raise TypeError

        if stack_Experiment.top().ExperimentType != experimentType.Circuit:
            raise errors.ExperimentTypeError

        func(SourcePin, TargetPin, *args, **kwargs)

    return result

# 原始的连接导线的方式
def primitive_crt_wire(Source: str, SourcePin: str, Target: str, TargetPin: str, color: str = '蓝'):
    stack_Experiment.top().Wires.append({
        "Source": Source, "SourcePin": SourcePin,
        "Target": TargetPin, "TargetPin": TargetPin,
        "ColorName": f"{color}色导线"
    })

# 连接导线
@_check_typeWire
def crt_Wire(SourcePin: Pin, TargetPin: Pin, color: str = '蓝') -> None:
    if color in ("black", "blue", "red", "green", "yellow"):
        color = {"black": "黑", "blue": "蓝", "red": "红", "green": "绿", "yellow": "黄"}[color]

    if (color not in ("黑", "蓝", "红", "绿", "黄")):
        raise errors.WireColorError

    stack_Experiment.top().Wires.append({"Source": SourcePin.element_self._arguments["Identifier"], "SourcePin": SourcePin.pinLabel,
                   "Target": TargetPin.element_self._arguments["Identifier"], "TargetPin": TargetPin.pinLabel,
                   "ColorName": f"{color}色导线"})

# 删除导线
@_check_typeWire
def del_Wire(SourcePin: Pin, TargetPin: Pin) -> None:
    def _wire_is_equal(SourcePin: Pin, TargetPin: Pin, a_wire: dict) -> bool:
        if a_wire["Source"] == SourcePin.element_self._arguments["Identifier"] and a_wire["SourcePin"] == SourcePin.pinLabel \
           and a_wire["Target"] == TargetPin.element_self._arguments["Identifier"] and a_wire["TargetPin"] == TargetPin.pinLabel:
                return True
        elif a_wire["Source"] == TargetPin.element_self._arguments["Identifier"] and a_wire["SourcePin"] == TargetPin.pinLabel \
             and a_wire["Target"] == SourcePin.element_self._arguments["Identifier"] and a_wire["TargetPin"] == SourcePin.pinLabel:
                return True
        return False

    i: int = 0
    while i < len(stack_Experiment.top().Wires):
        a_wire = stack_Experiment.top().Wires[i]
        if _wire_is_equal(SourcePin, TargetPin, a_wire):
            stack_Experiment.top().Wires.pop(i)
        else:
            i += 1

# 删除所有导线
def clear_Wires() -> None:
    if stack_Experiment.top().ExperimentType != experimentType.Circuit:
        raise errors.ExperimentTypeError
    stack_Experiment.top().Wires.clear()

# 获取当前导线数
def count_Wires() -> int:
    if stack_Experiment.top().ExperimentType != experimentType.Circuit:
        raise errors.ExperimentTypeError
    return len(stack_Experiment.top().Wires)