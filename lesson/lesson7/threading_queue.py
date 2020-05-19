# !/usr/bin/python env
# _*_ coding:utf-8 _*_
"""
queue队列
队列：非常重要
功能：
1、提高效率
2、完成了程序的解耦
可以理解为一个容器，这个容器里面存放数据
既然有列表、元组这种容器为什么需要队列？
区别：列表中取数据，相当于复制一份数据，而队列中，数据只有一份，取走了就没了
先入先出,后进先出，优先级队列

下面这个程序是一个典型的生产者消费者模型。
生产者消费者模型是经典的在开发架构中使用的模型
运维中的集群就是生产者消费者模型，生活中很多都是

作者：ivan_cq
链接：https://www.jianshu.com/p/a4aedd66af7c
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

import threading
import queue,time

q=queue.Queue(maxsize=10)

def Producer(name):
    count=1
    while True:
        q.put("骨头 %s"%count)
        print("生产了骨头",count)
        count+=1
        time.sleep(1)
def Consumer(name):
    while True:
        print("[%s] 取到  [%s] 并且吃了它。。。"%(name,q.get()))
        time.sleep(1)
# p=threading.Thread(target=Producer,args=('cq',))
# c=threading.Thread(target=Consumer,args=("dog",))
# c1=threading.Thread(target=Consumer,args=("cc",))
#
# p.start()
# c.start()
# c1.start()

q = queue.Queue(50)
print(q.qsize())