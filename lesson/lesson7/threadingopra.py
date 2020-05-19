# !/usr/bin/python env
# _*_ coding:utf-8 _*_

import threading


class MyThread(threading.Thread):
    def __init__(self,func,arg):
        super().__init__()
        self.x = 10
        self.func = func
        self.arg = arg

    def run(self):
        self.func(*self.arg)

class Account:
    def __init__(self,account_no,balance):
        # 账户号与与余额
        self.account_no = account_no
        self.balance = balance
lock = threading.Lock()
#模拟取钱操作
def draw(account,draw_amount):
    lock.acquire()
    #print(lock.locked())
    if account.balance > draw_amount:
        print(threading.current_thread().name + "取钱成功，您取钱" + str(draw_amount))

        account.balance -= draw_amount
        print("余额为 " + str(account.balance))
    else:
        print(threading.current_thread().name + "余额不足，取钱失败")
    lock.release()
    #print(lock.locked())


acct = Account('21121',1000)

print(threading.current_thread().name + "   start")
t1 = MyThread(draw,(acct,800))
t1.start()
t1.join()
t2 = MyThread(draw,(acct,800))
t2.start()
t2.join()
print(threading.current_thread().name + "   end")

