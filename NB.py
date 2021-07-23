# -*- coneding = utf-8 -*-
# [url=home.php?mod=space&uid=238618]@Time[/url] : 2021/7/19 21:39
# @Author:phoenix
# [url=home.php?mod=space&uid=267492]@file[/url] : 5. 百度爱采购ajax.py
# @Softwara : PyCharm
import condition as condition
import requests
import re
import csv
from time import sleep
import os

kw = input("请输入一个查询关键词：")
file_name = '百度爱采购-%s.csv' % kw
f = open(file_name, mode='a', encoding='gbk')
cscwrite = csv.writer(f)
num = 0
for i in range(1, 100):
    params = {
        'ajax': '1',
        'q': kw,
        'p': i,
        'sa': '',
        'mk': '全部结果',
        's': '30',
        'adn': '0',
        'resType': 'product',
        'from': 'search'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    response = requests.get('https://b2b.baidu.com/s/a', params=params, headers=headers).json()
    name_list = response['data']['productList']
    list_num = len(name_list)
    print(len(name_list))
    for name in name_list:
        corporate_name = name.get('fullProviderName')  # 获取到公司名称
        # 构造公司联系页链接
        url = f'https://b2b.baidu.com/shop?name={corporate_name}&tpath=contact'
        resp = requests.get(url=url, headers=headers).text
        phoneNumber = re.findall('"phoneNumber":"(.*?)"', resp, re.S)  # 手机
        telNumber = re.findall('"telNumber":"(.*?)"', resp, re.S)  # 电话
        faxNumber = re.findall('"faxNumber":"(.*?)"', resp, re.S)  # 传真
        qqNumber = re.findall('"qqNumber":"(.*?)"', resp, re.S)  # qq号码
        wechatNumber = re.findall('"wechatNumber":"(.*?)"', resp, re.S)  # 微信
        email = re.findall('"email":"(.*?)"', resp, re.S)  # 电子邮箱
        print(corporate_name, phoneNumber, telNumber, telNumber, faxNumber, qqNumber, wechatNumber, email)
        cscwrite.writerow([corporate_name, phoneNumber, telNumber, telNumber, faxNumber, qqNumber, wechatNumber, email])
        sleep(0.05)
        num += 1
    print('---第%s页采集完成---' % i)
    if (list_num == 0):
        f.close()
        print('---爬取完毕,共获取到%d条数据---' % num)
        os._exit(0)