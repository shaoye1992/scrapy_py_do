import requests
import re
from bs4 import BeautifulSoup
import json
import xlrd
import xlsxwriter

DATA = []

goods = '暗黑3 switch'

url = 'https://s.taobao.com/search?q={}&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0'.format(goods)

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

r = requests.get(url, timeout = 30, headers = headers)

html = r.text

content = re.findall(r'g_page_config = (.+?)g_srp_loadCss', html, re.S)[0].strip()[:-1]

content = json.loads(content)

datalist = content['mods']['itemlist']['data']['auctions']

for item in datalist:
    temp = {

    }