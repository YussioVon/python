import requests
from bs4 import  BeautifulSoup
header = { 'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
           }
r = requests.get('http://bj.xiaozhu.com/',headers = header)

# print(r.encoding)
# print(r.status_code)
