# !/usr/bin/python3 env
# _*_ coding:utf-8 _*_
# @Author   :   ivy
# @Time     :   2020/5/18 10:58 上午

from locust import Locust,TaskSet,task

class Mytasks(TaskSet):

    def one_task(self):
        print("执行一个伟大的测试任务!")

class RunTasks(Locust):
    test_set = Mytasks
    min_wait = 2000
    max_wait = 5000

