# -*- coding: utf-8 -*-
from ._elementBase import CircuitBase
from ..wire import InputPin, OutputPin
from physicsLab.typehint import Optional, numType, CircuitElementData, Self, Generate

class _logicBase(CircuitBase):
    def set_HighLevelValue(self, num: numType) -> Self:
        ''' 设置高电平的值 '''
        if not isinstance(num, (int, float)) or num < self.get_LowLevelValue():
            raise TypeError

        self.data["Properties"]["高电平"] = num

        return self

    def get_HighLevelValue(self) -> numType:
        ''' 获取高电平的值 '''
        return self.data["Properties"]["高电平"]

    def set_LowLevelValue(self, num: numType) -> Self:
        ''' 设置低电平的值 '''
        if not isinstance(num, (int, float)) or num < self.get_LowLevelValue():
            raise TypeError

        self.data["Properties"]["低电平"] = num

        return self

    def get_LowLevelValue(self):
        ''' 获取低电平的值 '''
        return self.data["Properties"]["低电平"]

class Logic_Input(_logicBase):
    ''' 逻辑输入 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        self.data: CircuitElementData = {"ModelID": "Logic Input", "Identifier": Generate,
                          "IsBroken": False, "IsLocked": False,
                          "Properties": {"高电平": 3.0, "低电平": 0.0, "锁定": 1.0, "开关": 0},
                          "Statistics": {"电流": 0.0, "电压": 0.0, "功率": 0.0},
                          "Position": Generate, "Rotation": Generate, "DiagramCached": False,
                          "DiagramPosition": {"X": 0, "Y": 0, "Magnitude": 0.0},
                          "DiagramRotation": 0}

    def __repr__(self) -> str:
        res = f"Logic_Input({self._position.x}, {self._position.y}, {self._position.z}, " \
              f"elementXYZ={self.is_elementXYZ})"

        if self.data["Properties"]["开关"] == 1.0:
            res += ".set_highLevel()"
        return res

    def set_highLevel(self) -> "Logic_Input":
        ''' 将逻辑输入的状态设置为1 '''
        self.data["Properties"]["开关"] = 1.0
        return self

    @property
    def o(self) -> OutputPin:
        return OutputPin(self, 0)

class Logic_Output(_logicBase):
    ''' 逻辑输出 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        self.data: CircuitElementData = {"ModelID": "Logic Output", "Identifier": Generate,
                          "IsBroken": False, "IsLocked": False,
                          "Properties": {"状态": 0.0, "高电平": 3.0, "低电平": 0.0, "锁定": 1.0}, "Statistics": {},
                          "Position": Generate,
                          "Rotation": "0,180,0", "DiagramCached": False,
                          "DiagramPosition": {"X": 0, "Y": 0, "Magnitude": 0.0}, "DiagramRotation": 0}

    @property
    def i(self) -> InputPin:
            return InputPin(self, 0)

class _2_pin_Gate(_logicBase):
    ''' 2引脚门电路基类 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        self.data: CircuitElementData = {"ModelID": Generate, "Identifier": Generate, "IsBroken": False, "IsLocked": False,
                          "Properties": {"高电平": 3.0, "低电平": 0.0, "最大电流": 0.1, "锁定": 1.0},
                          "Statistics": {},
                          "Position": Generate, "Rotation": Generate, "DiagramCached": False,
                          "DiagramPosition": {"X": 0, "Y": 0, "Magnitude": 0.0}, "DiagramRotation": 0}

    @property
    def i(self) -> InputPin:
        return InputPin(self, 0)

    @property
    def o(self) -> OutputPin:
        return OutputPin(self, 1)

class Yes_Gate(_2_pin_Gate):
    ''' 是门 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Yes Gate"

class No_Gate(_2_pin_Gate):
    ''' 非门 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "No Gate"

class _3_pin_Gate(_logicBase):
    ''' 3引脚门电路基类 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        self.data: CircuitElementData = {"ModelID": "", "Identifier": Generate, "IsBroken": False, "IsLocked": False,
                          "Properties": {"高电平": 3.0, "低电平": 0.0, "最大电流": 0.1, "锁定": 1.0},
                          "Statistics": {},
                          "Position": Generate, "Rotation": Generate, "DiagramCached": False,
                          "DiagramPosition": {"X": 0, "Y": 0, "Magnitude": 0.0}, "DiagramRotation": 0}

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 0)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 1)

    @property
    def o(self) -> OutputPin:
        return OutputPin(self, 2)

class Or_Gate(_3_pin_Gate):
    ''' 或门 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Or Gate"

class And_Gate(_3_pin_Gate):
    ''' 与门 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "And Gate"

class Nor_Gate(_3_pin_Gate):
    ''' 或非门 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Nor Gate"

class Nand_Gate(_3_pin_Gate):
    ''' 与非门 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Nand Gate"

class Xor_Gate(_3_pin_Gate):
    ''' 异或门 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Xor Gate"

class Xnor_Gate(_3_pin_Gate):
    ''' 同或门 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Xnor Gate"

class Imp_Gate(_3_pin_Gate):
    ''' 蕴含门 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Imp Gate"

class Nimp_Gate(_3_pin_Gate):
    ''' 蕴含非门 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Nimp Gate"

class _big_element(_logicBase):
    ''' 2体积元件父类 '''
    is_bigElement = True

    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        self.data: CircuitElementData = {"ModelID": "", "Identifier": Generate, "IsBroken": False,
                          "IsLocked": False, "Properties": {"高电平": 3.0, "低电平": 0.0, "锁定": 1.0},
                          "Statistics": {},
                          "Position": Generate, "Rotation": Generate, "DiagramCached": False,
                          "DiagramPosition": {"X": 0, "Y": 0, "Magnitude": 0.0}, "DiagramRotation": 0}

class Half_Adder(_big_element):
    ''' 半加器 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Half Adder"

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 2)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 3)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 0)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 1)

class Full_Adder(_big_element):
    ''' 全加器 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Full Adder"

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 2)

    @property
    def i_mid(self) -> InputPin:
        return InputPin(self, 3)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 4)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 0)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 1)

class Multiplier(_big_element):
    ''' 二位乘法器 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Multiplier"

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 4)

    @property
    def i_upmid(self) -> InputPin:
        return InputPin(self, 5)

    @property
    def i_lowmid(self) -> InputPin:
        return InputPin(self, 6)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 7)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 0)

    @property
    def o_upmid(self) -> OutputPin:
        return OutputPin(self, 1)

    @property
    def o_lowmid(self) -> OutputPin:
        return OutputPin(self, 2)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 3)

class D_Flipflop(_big_element):
    ''' D触发器 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "D Flipflop"

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 2)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 3)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 0)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 1)

class T_Flipflop(_big_element):
    ''' T'触发器 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "T Flipflop"

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 2)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 3)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 0)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 1)

class Real_T_Flipflop(_big_element):
    ''' T触发器 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Real-T Flipflop"

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 2)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 3)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 0)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 1)

class JK_Flipflop(_big_element):
    ''' JK触发器 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "JK Flipflop"

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 2)

    @property
    def i_mid(self) -> InputPin:
        return InputPin(self, 3)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 4)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 0)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 1)

class Counter(_big_element):
    ''' 计数器 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Counter"

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 4)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 5)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 0)

    @property
    def o_upmid(self) -> OutputPin:
        return OutputPin(self, 1)

    @property
    def o_lowmid(self) -> OutputPin:
        return OutputPin(self, 2)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 3)

class Random_Generator(_big_element):
    ''' 随机数发生器 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        super().__init__(x, y, z, elementXYZ)
        self.data["ModelID"] = "Random Generator"

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 4)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 5)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 0)

    @property
    def o_upmid(self) -> OutputPin:
        return OutputPin(self, 1)

    @property
    def o_lowmid(self) -> OutputPin:
        return OutputPin(self, 2)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 3)

class eight_bit_Input(_logicBase):
    ''' 八位输入器 '''
    is_bigElement = True

    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        self.data: CircuitElementData = {"ModelID": "8bit Input", "Identifier": Generate,
                           "IsBroken": False, "IsLocked": False,
                           "Properties": {"高电平": 3.0, "低电平": 0.0, "十进制": 0.0, "锁定": 1.0},
                           "Statistics": {},
                           "Position": Generate, "Rotation": Generate, "DiagramCached": False,
                           "DiagramPosition": {"X": 0, "Y": 0, "Magnitude": 0.0}, "DiagramRotation": 0}

    def __repr__(self) -> str:
        res = f"eight_bit_Input({self._position.x}, {self._position.y}, {self._position.z}, " \
              f"elementXYZ={self.is_elementXYZ})"

        if self.data["Properties"]["十进制"] != 0:
            res += f".set_num({self.data['Properties']['十进制']})"
        return res

    def set_num(self, num : int):
        if 0 <= num <= 255:
            self.data["Properties"]["十进制"] = num
        else:
            raise RuntimeError("The number range entered is incorrect")

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 0)

    @property
    def i_upmid(self) -> InputPin:
        return InputPin(self, 1)

    @property
    def i_lowmid(self) -> InputPin:
        return InputPin(self, 2)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 3)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 4)

    @property
    def o_upmid(self) -> OutputPin:
        return OutputPin(self, 5)

    @property
    def o_lowmid(self) -> OutputPin:
        return OutputPin(self, 6)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 7)

class eight_bit_Display(_logicBase):
    ''' 八位显示器 '''
    is_bigElement = True

    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        self.data: CircuitElementData = {"ModelID": "8bit Display", "Identifier": Generate,
                          "IsBroken": False, "IsLocked": False,
                          "Properties": {"高电平": 3.0, "低电平": 0.0, "状态": 0.0, "锁定": 1.0},
                          "Statistics": {"7": 0.0, "6": 0.0, "5": 0.0, "4": 0.0,
                                         "3": 0.0, "2": 0.0, "1": 0.0, "0": 0.0, "十进制": 0.0},
                          "Position": Generate, "Rotation": Generate, "DiagramCached": False,
                          "DiagramPosition": {"X": 0, "Y": 0, "Magnitude": 0.0}, "DiagramRotation": 0}

    @property
    def i_up(self) -> InputPin:
        return InputPin(self, 0)

    @property
    def i_upmid(self) -> InputPin:
        return InputPin(self, 1)

    @property
    def i_lowmid(self) -> InputPin:
        return InputPin(self, 2)

    @property
    def i_low(self) -> InputPin:
        return InputPin(self, 3)

    @property
    def o_up(self) -> OutputPin:
        return OutputPin(self, 4)

    @property
    def o_upmid(self) -> OutputPin:
        return OutputPin(self, 5)

    @property
    def o_lowmid(self) -> OutputPin:
        return OutputPin(self, 6)

    @property
    def o_low(self) -> OutputPin:
        return OutputPin(self, 7)

class Schmitt_Trigger(CircuitBase):
    ''' 施密特触发器 '''
    def __init__(self, x: numType, y: numType, z: numType, elementXYZ: Optional[bool] = None):
        self.data: CircuitElementData = {"ModelID": "Schmitt Trigger", "Identifier": Generate,
                           "IsBroken": False, "IsLocked": False,
                           "Properties": {"工作模式": 0.0, "切变速率": 0.5, "高电准位": 5.0, "锁定": 1.0,
                                          "正向阈值": 3.33333334, "低电准位": 0.0, "负向阈值": 1.66666666},
                            "Statistics": {"输入电压": 0.0, "输出电压": 0.0, "1": 0.0},
                            "Position": Generate, "Rotation": Generate, "DiagramCached": False,
                            "DiagramPosition": {"X": 0, "Y": 0, "Magnitude": 0.0}, "DiagramRotation": 0}

    @property
    def i(self) -> InputPin:
        return InputPin(self, 0)

    @property
    def o(self) -> OutputPin:
        return OutputPin(self, 1)