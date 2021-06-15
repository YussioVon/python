# -*-coding:utf-8 -*
# @Time : 2021/6/15 11:23
# @Author :Yussio
# @FileName : reptile

from __future__ import unicode_literals
import requests
import json
from lxml import etree
import time
from bs4 import BeautifulSoup
import pandas
'''

url = 'https://movie.douban.com/subject/1292722/?tag=%E7%BB%8F%E5%85%B8&from=gaia_video'
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
html = requests.get(url,headers = header).text
s = etree.HTML(html)
title = s.xpath('//*[@id="content"]/h1/span[1]/text()')
actor = s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
print(title)
print(actor)
'''
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={}&limit=20'


filminfolist = []
for i in range(0,300,20):
    aimurl = url.format(i)
    res = requests.get(aimurl,headers = header)
    jd = json.loads(res.text)
    for j in jd:
        filminfo = {}
        filminfo['title'] = j['title']
        filminfo['score'] = j['score']
        filminfo['url'] = j['url']
        filminfolist.append(filminfo)
print(filminfolist)
df = pandas.DataFrame(filminfolist)
df.to_excel('G:\\douban.xlsx')