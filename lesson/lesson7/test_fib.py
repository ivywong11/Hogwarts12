# !/usr/bin/python env
# _*_ coding:utf-8 _*_
import pytest

from lesson.lesson7.fib import *


@pytest.mark.parametrize("fibx,x",[
    (5,1),
    (10,1),
    (20,1)
])
def test_fib(fibx,x):
    fib(fibx)
    assert x == 1