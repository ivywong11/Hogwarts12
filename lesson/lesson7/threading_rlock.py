# !/usr/bin/python env
# _*_ coding:utf-8 _*_

import threading, time
def run1():
    print(threading.current_thread().name + ": run1")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num


def run2():
    print(threading.current_thread().name + ": run2")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2


def run3():
    print("thread strat : " + threading.current_thread().name + '\n')
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(threading.current_thread().name, res, res2,'\n')
    print(threading.current_thread().name + " is done. " + '\n')


if __name__ == '__main__':

    num, num2 = 0, 0
    lock = threading.RLock()  #RLOCK
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:
    pass
else:
    print('----all threads done---')
    print(num, num2)