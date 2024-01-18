# -*- coding: utf-8 -*-
import unittest
from physicsLab import *
from physicsLab.union import *
from physicsLab.experiment import stack_Experiment
#from viztracer import VizTracer

class TestError(Exception):
    def __init__(self, no_pop: bool=False) -> None:
        self.no_pop = no_pop

    def __str__(self) -> str:
        if not self.no_pop:
            exit_Experiment()
        return "Test Fail"

def my_test_dec(method: Callable):
    def result(*args, **kwarg):
        method(*args, **kwarg)

        if len(stack_Experiment.data) != 0:
            print(f"method \"{method.__code__.co_name}\" test fail due to len(stack_Experiment) != 0")
            raise TestError
    return result

class MyTestCase(unittest.TestCase):
    # init unittest class
    # @classmethod
    # def setUpClass(cls):
    #     tracer = VizTracer()
    #     tracer.start()
    #
    #     cls.tracer = tracer
    #
    # @classmethod
    # def tearDownClass(cls):
    #     tracer = cls.tracer
    #     tracer.stop()
    #     tracer.save() # also takes output_file as an optional argument

    @my_test_dec
    def test_experiment1(self):
        crt_Experiment("__test__", force_crt=True)
        a = Yes_Gate()
        self.assertEqual(count_Elements(), 1)
        self.assertEqual(a.get_Position(), (0, 0, 0))
        crt_Wire(a.o, a.i)
        self.assertEqual(count_Wires(), 1)
        clear_Wires()
        self.assertEqual(count_Wires(), 0)
        self.assertEqual(count_Elements(), 1)
        crt_Wire(a.o, a.i)
        crt_Element('Logic Input')
        self.assertEqual(count_Elements(), 2)
        get_Element(0, 0, 0)
        exit_Experiment()

    @my_test_dec
    def test_read_Experiment(self):
        crt_Experiment("__test__", force_crt=True)

        self.assertEqual(count_Elements(), 0)
        self.assertEqual(count_Wires(), 0)
        Logic_Input()
        write_Experiment()

        open_Experiment("__test__")
        read_Experiment()
        self.assertEqual(count_Elements(), 1)
        exit_Experiment()

    @my_test_dec
    def test_crt_Experiment(self):
        try:
            crt_Experiment("__test__", force_crt=True)
            write_Experiment()
            crt_Experiment("__test__") # will fail
        except crtExperimentFailError:
            Experiment("__test__").delete()
        else:
            raise TestError

    @my_test_dec
    def test_crt_wire(self):
        with experiment("__test__", write=False, force_crt=True):
            a = Or_Gate()
            crt_Wire(a.o, a.i_up, "red")

    @my_test_dec
    def test_union_Sum(self):
        crt_Experiment("__test__", force_crt=True)
        union.Sum(0, -1, 0, 64)
        self.assertEqual(count_Elements(), 64)
        self.assertEqual(count_Wires(), 63)
        clear_Elements()
        self.assertEqual(count_Wires(), 0)
        self.assertEqual(count_Elements(), 0)
        exit_Experiment()

    @my_test_dec
    def test_get_Element(self):
        crt_Experiment("__test__", force_crt=True)
        Or_Gate(0, 0, 0)
        crt_Wire(
            get_Element(x=0, y=0, z=0).o,
            get_Element(1).i_up
        )
        crt_Wire(get_Element(0,0,0).i_low, get_Element(index=1).o)
        self.assertEqual(count_Wires(), 2)
        exit_Experiment()

    # 测逝用例未写完
    @my_test_dec
    def test_set_O(self):
        crt_Experiment("__test__", force_crt=True)
        set_O(-1, -1, 0)
        for x in range(10):
            for y in range(10):
                Yes_Gate(x, y, 0, True)
        self.assertEqual(count_Elements(), 100)
        exit_Experiment()

    @my_test_dec
    def test_errors(self):
        try:
            with experiment("__test__", delete=True, force_crt=True):
                pass
            open_Experiment('__test__') # do not exist
        except OpenExperimentError:
            pass
        else:
            raise TestError

    # 测试元件坐标系2
    @my_test_dec
    def test_aTest(self):
        crt_Experiment("__test__", force_crt=True)
        set_elementXYZ(True)
        set_O(-1, -1, 0)
        for x in range(10):
            for y in range(10):
                Yes_Gate(x, y, 0)
        for x in range(10):
            for y in [y * 2 + 10 for y in range(5)]:
                Multiplier(x, y, 0)

        crt_Wire(get_Element(1).o, get_Element(0, 1, 0).i)
        get_Element(2).i - get_Element(3).o - get_Element(4).i
        self.assertEqual(count_Wires(), 3)
        self.assertEqual(count_Elements(), 150)
        exit_Experiment()

    @my_test_dec
    def test_open_many_Experiment(self):
        crt_Experiment("_Test", force_crt=True)
        with experiment('__test__', write=False, force_crt=True):
            Logic_Input()
            self.assertEqual(1, count_Elements())
        exit_Experiment()

    @my_test_dec
    def test_with_and_coverPosition(self):
        with experiment("__test__", write=False, force_crt=True):
            Logic_Input()
            Or_Gate()
            self.assertEqual(len(get_Element(0, 0, 0)), 2)

    @my_test_dec
    def test_del_Element(self):
        with experiment("__test__", write=False, force_crt=True):
            Logic_Input().o - Or_Gate().o
            del_Element(get_Element(2))
            self.assertEqual(count_Elements(), 1)
            self.assertEqual(count_Wires(), 0)

    # 测逝模块化电路连接导线
    @my_test_dec
    def test_wires(self):
        with experiment("__test__", write=False, elementXYZ=True, force_crt=True):
            a = union.Inputs(0, 0, 0, 8)
            b = union.Outputs(0.6, 0, 0, 8, elementXYZ=False)
            Logic_Output(0.6, 0, 0.1, elementXYZ=False)
            c = union.D_WaterLamp(1, 0, 0, bitLength=8)
            crt_Wires(b.data_Input, c.data_Output)
            self.assertEqual(25, count_Elements())
            self.assertEqual(23, count_Wires())
            del_Wires(c.data_Output, b.data_Input)
            self.assertEqual(15, count_Wires())

    # 测逝模块化加法电路
    @my_test_dec
    def test_union_Sum2(self):
        with experiment("__test__", write=False, elementXYZ=True, force_crt=True):
            a = union.Inputs(-1, 0, 0, 8)
            b = union.Inputs(-2, 0, 0, 8)
            c = union.Sum(0, 0, 0, 8)
            d = union.Outputs(1, 0, 0, 8)
            a.data_Output - c.data_Input1
            b.data_Output - c.data_Input2
            c.data_Output - d.data_Input

    # 测试打开实验类型与文件不吻合
    @my_test_dec
    def test_experimentType(self):
        with experiment("__test__", experiment_type=experimentType.Electromagnetism, write=False, force_crt=True):
            try:
                Positive_Charge()
                Logic_Input()
            except ExperimentTypeError:
                pass
            else:
                raise TestError

    @my_test_dec
    def test_experimentType3(self):
        with experiment("__test__", experiment_type=experimentType.Circuit, write=False, force_crt=True):
            Logic_Input()
        with experiment("__test__", experiment_type=experimentType.Celestial, write=False, force_crt=True):
            pass
        with experiment("__test__", experiment_type=experimentType.Electromagnetism, write=False, force_crt=True):
            pass

    @my_test_dec
    def test_electromagnetism(self):
        with experiment("__test__", write=False, experiment_type=experimentType.Electromagnetism, force_crt=True):
            Negative_Charge(-0.1, 0, 0)
            Positive_Charge(0.1, 0, 0)
            self.assertEqual(count_Elements(), 2)
            try:
                count_Wires()
            except ExperimentTypeError:
                pass
            else:
                raise TestError

    @my_test_dec
    def test_union_Sub(self):
        with experiment("__test__", write=False, elementXYZ=True, force_crt=True):
            a = union.Sub(bitLength=8, fold=False)
            crt_Wires(union.Inputs(-3, 0, 0, 8).data_Output, a.minuend)
            crt_Wires(union.Inputs(-2, 0, 0, 8).data_Output, a.subtrahend)
            crt_Wires(union.Outputs(2, 0, 0, 9).data_Input, a.outputs)
            self.assertEqual(count_Elements(), 42)
            self.assertEqual(count_Wires(), 41)

            union.Sub(-5, 0, 0)

    # 测试简单乐器设置音高的三种方法
    @my_test_dec
    def test_Simple_Instrument(self):
        with experiment("__test__", write=False, elementXYZ=True, force_crt=True):
            a = Simple_Instrument(pitch=48)
            a = Simple_Instrument().set_Tonality(48)
            a = Simple_Instrument(pitch="C3")
            a = Simple_Instrument().set_Tonality("C3")
            Logic_Input(-1, 0, 0).o - a.i
            a.o - Ground_Component(1, 0, 0).i

    @my_test_dec
    def test_getElementError(self):
        with experiment("__test__", write=False, force_crt=True):
            Logic_Input()
            try:
                get_Element(2)
            except getElementError:
                pass
            else:
                raise TestError
    
    @my_test_dec
    def test_unionMusic(self):
        music.Note(2)
        try:
            music.Note(0)
        except TypeError:
            pass

    @my_test_dec
    def test_const_is_bigElement(self):
        with experiment("__test__", force_crt=True, write=False):
            a = Multiplier()
            try:
                a.is_bigElement = False
            except AttributeError:
                pass
            else:
                raise TestError

    @my_test_dec
    def test_musicPlayer(self):
        with experiment("__test__", write=False, force_crt=True):
            l = (0, 2, 4, 5, 7, 9, 11)

            t = music.Piece()
            for i in range(7):
                for j in l:
                    n = music.Note(1, pitch=12 * i + j + 21)
                    t.append(n)
                    n.append(music.Note(1, pitch=12 * i + j + 23))
            #t.notes[-1] = None
            #print(t)
            t.release(-1, -1, 0)
    
    @my_test_dec
    def test_mutiple_notes_in_Simple_Instrument(self):
        with experiment("__test__", force_crt=True, write=False):
            Simple_Instrument().add_note(67) # type: ignore

if __name__ == '__main__':
    unittest.main()
