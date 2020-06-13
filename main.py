from bs4.element import Tag
from bs4 import BeautifulSoup
import requests
import re
import sqlite3
from collections import namedtuple

proxies = {'https': 'https://127.0.0.1:8888'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}


def create_product(product):
    try:
        with sqlite3.connect(r'E:\Tutorial\Python\wildberries.db') as conn:
            cursor = conn.cursor()
            # print(product.price)
            # price = product.price[:-1]
            # #price = price.replace(' ', '')
            # price = price.replace(chr(160), '')
            # price = int(price)
            cursor.execute('insert into recorders values(?,?,?)', (product.brand.strip(' /'), product.good, int(product.price.replace(chr(160), '').replace(chr(8381), ''))))
    except sqlite3.OperationalError as e:
        print(product, e)


def clear_db():
    with sqlite3.connect(r'E:\Tutorial\Python\wildberries.db') as conn:
        cursor = conn.cursor()
        cursor.execute('delete from recorders')


# class Good:
#     def __init__(self, e):
#         self.brand = e.select_one('strong.brand-name').text
#         self.good = e.select_one('span.goods-name').text
#         self.price = e.select_one('.lower-price').text
#
#     def __repr__(self):
#         return f'Good({self.brand}, {self.good}, {self.price})'


def main():
    clear_db()
    s = requests.Session()
    s.proxies = proxies
    s.headers.update(headers)
    s.verify = False

    r = s.get('https://www.wildberries.ru/catalog/elektronika/avtoelektronika')
    soup = BeautifulSoup(r.content)
    # print(re.sub(r'\n+', r'\n', soup.text))
    count_pages = len(soup.select('.pagination-item'))
    for i in range(1, 2):
        r = s.get(f'https://www.wildberries.ru/catalog/elektronika/avtoelektronika?page={i}')
        soup = BeautifulSoup(r.content)
        goods = (Good(e) for e in soup.select('div.dtList.i-dtList.j-card-item'))
        for good in goods:
            create_product(good)


if __name__ == '__main__':
    main()

# for e in soup.select('div.dtList.i-dtList.j-card-item'):
#     # print(e.select_one('.lower-price').text)
#     # print(e.select_one('strong.brand-name').text, e.select_one('span.goods-name').text, e.select_one('.lower-price').text)
#     # print(list(e.select_one('strong.brand-name')))
#     brand = e.select_one('strong.brand-name')
#     good = e.select_one('span.goods-name')
#     price = e.select_one('.lower-price')
