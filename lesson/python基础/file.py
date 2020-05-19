# !/usr/bin/python3 env
# _*_ coding:utf-8 _*_
# @Author   :   ivy
# @Time     :   2020/5/17 7:37 下午
import random
import string
from random import randint
file = 'big.txt'
def writefile(file):
    with open(file,'w') as f:
        for i in range(9000000):
            len = randint(1,255)
            str = 'ab cdefg hijklmnop qrstuvwxyz!@#$%^&*()1234567890'
            str2 = ''
            for i in range(len):
                str2 += random.choice(str)
            str2 += '\r\n'
            #print(str2)
            #print(f,'_'*30)
            f.write(str2)

def readfile(file):
    with open(file,'r') as f:
        for line in f:
            print(line)


readfile(file)
str = 'ab cdefg hijklmnop qrstuvwxyz!@#$%^&*()1234567890'
print(random.choice(str))



