# -*-coding:utf-8 -*
# @Time : 2021/6/15 11:23
# @Author :Yussio
# @FileName : reptile

from __future__ import unicode_literals
import requests
import json

import pandas

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

url = 'https://b2b.baidu.com/c?q=%E5%AE%81%E6%B3%A2'


firms = []
for i in range(0,300,20):
    aimurl = url.format(i)
    res = requests.get(aimurl,headers = header)
    jd = json.loads(res.text)
    print(jd)
    for j in jd:
        filminfo = {}
        filminfo['title'] = j['title']
        filminfo['score'] = j['score']
        filminfo['url'] = j['url']
        filminfolist.append(filminfo)
print(filminfolist)
df = pandas.DataFrame(filminfolist)
# df.to_excel('G:\\douban.xlsx')