# !/usr/bin/python3 env
# _*_ coding:utf-8 _*_
# @Author   :   ivy
# @Time     :   2020/5/16 11:19 下午
from random import random, randint
from queue import Queue
from time import sleep

from lesson.lesson7.mythread import MyThread


def writeQ(q):
    print("\033[31mproducing object for Q...\033[0m")
    q.put('xxx',1)
    print("\033[31mqueue size:{}\033[0m".format(q.qsize()))

def readQ(q):
    val = q.get(1)
    print("\033[32mcustomed object for Q...,queue size:{}\033[0m".format(q.qsize()))

def writer(q,loops):
    for i in range(loops):
        writeQ(q)
        #sleep(randint(1,3))

def reader(q,loops):
    for i in range(loops):
        readQ(q)
        sleep(randint(1,3))

funcs = [writer,reader]
n_funcs = range(len(funcs))
#print(len(funcs))

def main():
    nloops = randint(2,5)
    q = Queue(5)

    threads = []
    for i in n_funcs:
        t = MyThread(funcs[i],(q,nloops))
        threads.append(t)

    for i in n_funcs:
        threads[i].start()

    for i in n_funcs:
        threads[i].join()

    print("___all done___")

if __name__ == '__main__':
    main()