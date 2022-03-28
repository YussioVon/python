# -*- coding: utf-8 -*-
# @Time     :2022/3/28 10:18
# @Author   :Yussio
# @File     :niuke.py
myinput = str(input())
newlist1,newlist2 = [],[]
newlist1 = myinput.split(' ')

for i in list(reversed(newlist1)):
    newlist2.append(i+' ')
res = ''.join(newlist2)
print(res)