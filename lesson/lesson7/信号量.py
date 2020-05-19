# !/usr/bin/python env
# _*_ coding:utf-8 _*_
import threading
import time
"""
信号量
互斥锁，同时允许一个线程更改数据，而信号量同时允许一定数量的线程更改数据
"""


def run():
    semaphore.acquire()
    print(threading.current_thread().name)
    time.sleep(1)
    print(threading.current_thread().name + 'end')
    semaphore.release()

semaphore = threading.BoundedSemaphore(5)
threads = []
for i in range(10):
    t = threading.Thread(target=run)
    threads.append(t)
    t.start()
if i in range(10):
    threads[i].join()
if threading.active_count() != 1:
    pass
else:
    print('----all threads done---')