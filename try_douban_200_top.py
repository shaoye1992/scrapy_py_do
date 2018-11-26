import requests
from bs4 import BeautifulSoup

test_url = 'http://movie.douban.com/top250/'

def down_web(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    data = requests.get(url, headers = headers).content
    return data

movie_name_list = []

def parse_html(html):
    soup = BeautifulSoup(html,'lxml')
    movie_list_soup = soup.find('ol', attrs={'class':'grid_view'})
    if movie_list_soup != None:
        for movie_li in movie_list_soup.find_all('li'):
            detail = movie_li.find('div', attrs={'class':'hd'})
            movie_name = detail.find('span', attrs={'class':'title'}).getText()
            movie_name_list.append(movie_name)

        next_page = soup.find('span', attrs={'class':'next'}).find('a')
        if next_page:
            parse_html(down_web(test_url + next_page['href']))
        return movie_name_list


def main():
    handle = parse_html(down_web(test_url))
    if handle != None:
        handle = list(handle)
        for elf in handle:
            print(elf)

if __name__ == '__main__':
    main()