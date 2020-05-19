# !/usr/bin/python env
# _*_ coding:utf-8 _*_
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops = [2,4]

class MyThread(threading.Thread):
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        #super(MyThread, self).__init__()
        #super().__init__()
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)