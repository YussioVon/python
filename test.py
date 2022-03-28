# -*- coding: utf-8 -*-
# @Time     :2021/9/17 17:14
# @Author   :Yussio
# @File     :test.py
'''
import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time

url = 'http://www.biquzi.com/'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)  # 使用headers避免访问受限
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find_all('img')
folder_path = './photo/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)  # 创建文件夹

for index, item in enumerate(items):
    if item:
        html = requests.get(item.get('src'))  # get函数获取图片链接地址，requests发送访问请求
        img_name = folder_path + str(index + 1) + '.png'
        with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
            file.write(html.content)
            file.flush()
        file.close()  # 关闭文件
        print('第%d张图片下载完成' % (index + 1))
        time.sleep(1)  # 自定义延时
print('抓取完成')
'''
# -*- coding:utf-8 -*-
import re
import requests
import os
from bs4 import BeautifulSoup

url = 'https://pixabay.com/'
html = requests.get(url).text  # 获取网页内容
print(html)
# 这里由于有些图片可能存在网址打不开的情况，加个5秒超时控制。
# data-objurl="http://pic38.nipic.com/20140218/17995031_091821599000_2.jpg"获取这种类型链接
soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
# ^abc.*?qwe$
pic_url = soup.find_all('img', src=re.compile(r'^https://cdn.pixabay.com/photo/.*?jpg$'))
# pic_url = pic_node.get_text()
# pic_url = re.findall('"https://cdn.pixabay.com/photo/""(.*?)",',html,re.S)
print(pic_url)
i = 0
# 判断image文件夹是否存在，不存在则创建
if not os.path.exists('image'):
    os.makedirs('image')
for url in pic_url:
    img = url['src']
    try:
        pic = requests.get(img, timeout=5)  # 超时异常判断 5秒超时
    except requests.exceptions.ConnectionError:
        print('当前图片无法下载')
        continue
    file_name = "image/" + str(i) + ".jpg"  # 拼接图片名
    print(file_name)
    # 将图片存入本地
    fp = open(file_name, 'wb')
    fp.write(pic.content)  # 写入图片
    fp.close()
    i += 1