# -*- coding:utf-8 -*-
# Created By zl

# 3.2 Python简单爬虫
# conda install requests
# conda install bs4

import requests
from bs4 import BeautifulSoup

url = 'https://bj.lianjia.com/zufang/'


# 获取url下的页面内容, 返回soup对象
def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


# 获取列表页下所有的租房链接, 返回一个链接列表
def get_links(url):
    soup = get_page(url)
    links_div = soup.find_all('div', class_='pic-panel')
    links = [link.a.get('href') for link in links_div]
    return links


house_url = 'https://bj.lianjia.com/zufang/BJ0004562484.html'
soup = get_page(house_url)
price = soup.find('span', class_='total').text
unit = soup.find('span', class_='unit').text.strip()
print(price, unit)

house_info = soup.find_all('p', class_='lf')
area = house_info[0].text[3:]
layout = house_info[1].text[5:]
floor = house_info[2].text[3:]
dirction = house_info[3].text[5:]
print(area, layout, floor, dirction)

# 获取信息后插入表中
# pass