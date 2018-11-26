import requests
import re
from bs4 import BeautifulSoup
import json

test_url = 'https://item.jd.com/7437380.html'

def url_down(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    data = requests.get(url, headers = headers).content
    return data

def url_num_get(url):
    r_get = re.findall(r'\d{7}',url)
    return r_get[0]

def price_get(url_num):
    url = 'https://p.3.cn/prices/mgets?skuIds=J_' + url_num
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    price = json.loads(requests.get(url,headers=headers).content)[0]['p']
    return price

def item_name(url):
    soup = BeautifulSoup(url, 'lxml')
    name = soup.find('div',attrs={'class':'sku-name'}).getText()
    return name.strip()

def main():

    price = price_get(url_num_get(test_url))
    item_name_1 = item_name(url_down(test_url))
    print(item_name_1+'的价格：')
    print(price)

if __name__ == '__main__':
    main()