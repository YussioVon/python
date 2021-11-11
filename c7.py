# -*- coding: UTF-8 -*-
import json
import io
from bs4 import BeautifulSoup
import urllib,urllib2
from lxml import etree
import re
url = 'https://spcjsac.gsxt.gov.cn/api/goods/data'
formdata = {
    'food_type':'',
    'order_by': 'time',
    'pageNumber': '1',
    'pageSize': '10',
    'goods_enterprise': '浙江',
    'sampling_province': '',
    'name_first_letter': '',
    'food_name': '',
    'bar_code': '',
    'check_flag': 'uq'
}

#UA伪装
headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53'
                  '7.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
}
data = urllib.urlencode(formdata)
requests = urllib2.Request(url = url ,data =data,headers = headers)
response = urllib2.urlopen(requests).read()
print response
ret2 = re.findall('(me").*?,',str(response))
print ret2