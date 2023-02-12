#coding=utf-8
from random import sample
from string import ascii_letters, digits
from typing import Callable
from _fileGlobals import *
from electricity._elementPin import *

# 原件装饰器
def element_Method(cls):
    # 设置原件的角度
    def set_Rotation(self, xRotation: Union[int, float] = 0, yRotation: Union[int, float] = 0, zRotation: Union[int, float] = 180) -> None:
        if not (isinstance(xRotation, (int, float)) and isinstance(yRotation, (int, float)) and isinstance(zRotation, (int, float))):
            raise RuntimeError('illegal argument')
        self._arguments["Rotation"] = f"{myRound(xRotation)},{myRound(zRotation)},{myRound(yRotation)}"
        return self._arguments["Rotation"]
    cls.set_Rotation = set_Rotation

    # 重新设置元件的坐标
    def set_Position(self, x : Union[int, float], y : Union[int, float], z : Union[int, float]) -> None:
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float)) and isinstance(z, (int, float))):
            raise RuntimeError('illegal argument')
        x, y, z = myRound(x), myRound(y), myRound(z)
        del elements_Address[self._position]
        self._position = (x, y, z)
        self._arguments['Position'] = f"{x},{z},{y}"
        elements_Address[self._position] = self
    cls.set_Position = set_Position

    # 格式化坐标参数，主要避免浮点误差
    def format_Position(self) -> tuple:
        if not isinstance(self._position, tuple) or self._position.__len__() != 3:
            raise RuntimeError("Position must be a tuple of length three but gets some other value")
        self._position = (myRound(self._position[0]), myRound(self._position[1]), myRound(self._position[2]))
        return self._position
    cls.format_Position = format_Position

    # 获取原件的坐标
    def get_Position(self) -> tuple:
        return self._position
    cls.get_Position = get_Position

    # 获取父类的类型
    def father_type(self) -> str:
        return 'element'
    cls.father_type = father_type

    # 获取子类的类型（也就是ModelID）
    def type(self) -> str:
        return self._arguments['ModelID']
    cls.type = type

    # 打印参数
    def print_arguments(self) -> None:
        print(self._arguments)
    cls.print_arguments = print_arguments

    return cls

# __init__ 装饰器
def element_Init_HEAD(func : Callable) -> Callable:
    def result(self, x : Union[int, float] = 0, y : Union[int, float] = 0, z : Union[int, float] = 0) -> None:
        if not isinstance(x, (float, int)) and isinstance(y, (float, int)) and isinstance(z, (float, int)):
            raise RuntimeError('illegal argument')
        global Elements
        x, y, z = myRound(x), myRound(y), myRound(z)
        self._position = (x, y, z)
        if self._position in elements_Address.keys():
            raise RuntimeError("The position already exists")
        func(self, x, y, z)
        self._arguments["Identifier"] = ''.join(sample(ascii_letters + digits, 32))
        self._arguments["Position"] = f"{self._position[0]},{self._position[2]},{self._position[1]}"
        Elements.append(self._arguments)
        elements_Address[self._position] = self
        self.set_Rotation()
    return result

# 逻辑电路类装饰器
def logic_Circuit_Method(cls):
    # 设置高电平的值
    def set_HighLeaveValue(self, num: Union[int, float]) -> None:
        if not isinstance(num, (int, float)):
            raise RuntimeError('illegal argument')
        self._arguments['Properties']['高电平'] = num
    cls.set_HighLeaveValue = set_HighLeaveValue

    # 设置低电平的值
    def set_LowLeaveValue(self, num : Union[int, float]) -> None:
        if not isinstance(num, (int, float)):
            raise RuntimeError('illegal argument')
        self._arguments['Properties']['低电平'] = num
    cls.set_LowLeaveValue = set_LowLeaveValue

    # end decorator
    return cls

# 双引脚模拟电路原件的引脚
def two_pin_ArtificialCircuit_Pin(cls):
    @property
    def red(self):
        return element_Pin(self, 0)
    cls.red, cls.l = red, red

    @property
    def black(self):
        return element_Pin(self, 1)
    cls.black, cls.r = black, black

    return cls