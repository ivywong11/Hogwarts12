# !/usr/bin/python3 env
# _*_ coding:utf-8 _*_
# @Author   :   ivy
# @Time     :   2020/5/18 11:54 下午

"""
用例设计
add()
1.正数相加  2.0相加   3.负数相加
4.浮点数相加    5.混合数值类型相加  6.大数相加
7.空 8.字符类型  9.字符类型加数值类型

div()
1.正数  2.0被除   3.负数
4.浮点数    5.混合数值类型  6.大数
7.无法被除尽的数值
8.空 9.字符类型  10.字符类型加数值类型

"""
import pytest

from python.calc import Calc


class TestCalc():
    def setup_class(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a,b,expect",[
        (2,4,6),
        (0,0,0),
        (0,2,2),
        (-4,0,-4),
        (-1,-5,-6),
        (-4,5,1),
        (-6,4,-2),
        (467326257823564756432834785623895,5237582785238954732895732495,467331495406349995387567681356390)
    ])
    def test_add_digital(self,a,b,expect):
        ret = self.calc.add(a,b)
        assert ret == expect

    @pytest.mark.parametrize("a,b,expect", [
        (4.2, 4.2, 8.4),
        (4,6.3,10.3),
        (0, 0.5, 0.5),
        (-4.2, -0.2, -4.4),
        (-4.4, 0.4343, -3.9657),
        (5.0, -5, 0.0),
    ])
    def test_add_float(self,a,b,expect):
        ret = self.calc.add(a, b)
        assert ret == expect

    @pytest.mark.xfail
    #@pytest.mark.parametrize("a,b",[(3,,)])
    def test_add_empty(self,a,b):
        with pytest.raises(Exception) as e:
            self.calc.div(a,b)
        print(e.type,e.traceback)

    @pytest.mark.parametrize("a,b",[
        ("23","as"),
        (42,"23"),
    ])
    def test_add_letters(self, a, b):
        with pytest.raises(Exception) as e:
            self.calc.add(a, b)
        print(e.type, e.traceback)


    @pytest.mark.parametrize("a,b,expect", [
        (4, 2, 2),
        (0, 45, 0),
        (-4, 2, -2),
        (-9, -3, 3),
        (43, -1, -43),
        (2, 5, 0.4),
        (1, 3, 1/3),
        (467326257823564756432834785623895, 2, 467326257823564756432834785623895/2),
        (32,3.43434,32/3.43434)
    ])
    def test_div_digit(self, a, b, expect):
        ret = self.calc.div(a, b)
        assert ret == expect

    @pytest.mark.parametrize("a,b",[
        ("23","as"),
        (42,"23"),
    ])
    def test_div_letters(self, a, b):
        with pytest.raises(TypeError) as e:
            self.calc.div(a, b)
        print(e.type, e.traceback)


    # @pytest.mark.xfail(raises=ZeroDivisionError)
    # def test_div_0(self):
    #     self.calc.div(4,0)

    def test_div_0_2(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(3,0)
        print("除数不能为0")

if __name__ == '__main__':
    pytest.main('-vs','test_calc.py::TestCalc::test_div_0_2')




