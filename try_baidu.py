import requests

parameter_baidu = {'wd' : 'wechat'}
url = 'https://www.baidu.com'
r = requests.get(url, params = parameter_baidu)
print(r.url)