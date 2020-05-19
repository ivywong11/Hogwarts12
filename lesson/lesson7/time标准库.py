# !/usr/bin/python env
# _*_ coding:utf-8 _*_

import time
# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y%m%d %H:%M:%S",time.localtime()))
#

#获取两天前的时间
now = time.time()
twodays_ago = now - 60*60*24*2

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(twodays_ago)))