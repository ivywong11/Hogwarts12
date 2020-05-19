# !/usr/bin/python3 env
# _*_ coding:utf-8 _*_
# @Author   :   ivy
# @Time     :   2020/5/16 11:00 下午

"""
生成器:使用yield的函数
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时
从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。
"""
import sys


def fibo(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        tmp = b
        b = a+b
        a = tmp

f = fibo(10)

while True:
    try:
        print(next(f),end=' ')
    except:
        sys.exit()
