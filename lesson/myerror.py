# !/usr/bin/python env
# _*_ coding:utf-8 _*_
import traceback

list = [1,2,3,4,6]
it = iter(list)
while True:
    try:
        print(next(it))
    except Exception as e:
        print("out of size",Exception.__repr__(e))
        print(traceback.print_exc())
        break
    else:
        print("$"*10)
    finally:
        print('-'*30)

print('*'*50)
print('*'*50)
print('*'*50)
print('*'*50)
print('*'*50)

# while True:
#     sleep(0.5)
#     try:
#         print(next(it))
#     except Exception:
#         raise Exception("out of size" + format(Exception))
#         break
#     else:
#         print("$"*10)
#     finally:
#         print('-'*30)

# def f1():
#     print('****')
#
# class MyError(Exception):
#     def __init__(self,a):
#         self.a = a
#
#
#
# try:
#     raise MyError(6)
# except MyError as e:
#     print('myfhsafhsakfs')
#
# f1()
#
# try:
#     raise MyError('32')
# finally:
#     print('hello')



