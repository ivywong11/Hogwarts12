# !/usr/bin/python env
# _*_ coding:utf-8 _*_
import os
import unittest

import math


print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.exists('/app'))

a = 1
def c_a(a):
    a = 3
    return a


print(c_a(a))
print(a)