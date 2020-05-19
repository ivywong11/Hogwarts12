# !/usr/bin/python env
# _*_ coding:utf-8 _*_
import sys
from time import sleep, time

from lesson.lesson7.loop_threading import MyThread


def count_time(func):
    def wrapper(*args):
        start = time()
        print(func(*args))
        end = time()
        print(func.__name__,"花费时间：",end-start)
    return wrapper

@count_time
def fib(x):
    def _fib(x):
        if x<=2:
            return 1
        else:
            return (_fib(x-2)+_fib(x-1))
    return _fib(x)

@count_time
def fib2(n):
    def _fib(n):
        f1 = f2 = 1
        for k in range(3, n+1):
            a = f2
            f2 = f2 + f1
            f1 = a
        return f2
    return _fib(n)

@count_time
def fib3(n):
    def _fib(n):
        if n < 3:
            return 1
        list = [1,1]
        for k in range(2, n):
            list.append(list[k-2]+list[k-1])
        return list[-1]
    return _fib(n)


def fac(x):
    if x < 2:
        return x
    else:
        return x*fac(x-1)

def test_fib():
    threads = []
    for i in range(50,51):
        print('*'*10 + 'f(%d)' % i + '*'*10 )
        f1 = MyThread(fib,(i,))
        f2 = MyThread(fib2,(i,))
        f3 = MyThread(fib3,(i,))
        threads.append(f1)
        threads.append(f2)
        threads.append(f3)

    for i in threads:
        i.start()





