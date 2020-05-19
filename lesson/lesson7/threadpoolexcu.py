# !/usr/bin/python3 env
# _*_ coding:utf-8 _*_
# @Author   :   ivy
# @Time     :   2020/5/17 2:15 下午
from concurrent.futures import ThreadPoolExecutor,as_completed
from random import random, randint
from queue import Queue
from time import sleep


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

def hello(a):
    print('hello',a)

def main():
    nloops = randint(2,5)
    q = Queue(5)
    # 传入max_workers参数来设置线程池中最多能同时运行的线程数目
    executor = ThreadPoolExecutor(max_workers=5)
    threads = []

    for i in n_funcs:
        # 通过submit函数提交需要执行的函数到线程池中，submit函数立即返回，不阻塞
        res = executor.submit(funcs[i],q,nloops)
        threads.append(res)

    print(threads)

    '''
    as_completed()方法是一个生成器，在没有任务完成的时候，会阻塞，在有某个任务完成的时候，会yield这个任务，
    就能执行for循环下面的语句，然后继续阻塞住，循环到所有的任务结束。从结果也可以看出，先完成的任务会先通知主线程。
    '''
    for i in as_completed(threads):
        data = i.result()
        print(data)
    print("___all done___")

if __name__ == '__main__':
    main()
