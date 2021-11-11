# -*- coding: utf-8 -*-
# @Time     :2021/9/17 17:14
# @Author   :Yussio
# @File     :test.py
import requests
from bs4 import BeautifulSoup
header = { 'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
           }
r = requests.get('https://book.csdn.net/?spm=1018.2226.3001.4495',headers = header,timeout = 2)
r.encoding ='utf-8'
soup = BeautifulSoup(r.text,'html.parser')
# name = soup.find_all('a', 'book-title text-left')
name = soup.select('div > div.book-content > a')
for i in name:
    print i.text.encode('utf-8')

