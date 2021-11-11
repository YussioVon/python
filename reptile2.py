import requests
header = { 'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
           }
r = requests.get('http://www.santostang.com/',headers = header)
print(r.encoding)
print(r.status_code)
print r