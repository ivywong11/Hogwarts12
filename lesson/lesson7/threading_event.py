# !/usr/bin/python env
# _*_ coding:utf-8 _*_
"""
event
通过event来实现两个或者多个线程之间的交互。
通过全局变量的设置
下面这个例子，一个红绿灯线程，多个车线程，车辆按红绿灯规则行驶。
"""
import time,threading

event=threading.Event()
def lighter():
    count=0
    event.set()
    while True:
        if count > 5 and count <10:
            event.clear()
            print("\033[41;1mred light is on ...\033[0m")
        elif count > 10:
            event.set()
            print("\033[42;1mgreen light is on ...\033[0m")
            count=0
        else:
            print("\033[42;1mgreen light is on ...\033[0m")
        time.sleep(1)
        count+=1

def car(name):
    while True:
        if event.is_set():
            print("[%s] running ......"%name )
            time.sleep(1)
        else:
            print("[%s]  sees red light.."%name)
            event.wait()
            print("[%s] green light is on, start going...")




light = threading.Thread(target=lighter,)
light.start()


car1=threading.Thread(target=car,args=("tesla",))
car1.start()