# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = 'http://m.cgv.co.kr/Schedule/cont/ajaxMovieSchedule.aspx'

data = {'theaterCd': '0013', 'playYMD': '20190630'}
response = requests.post(url, data=data)
html = response.content
soup = BeautifulSoup(html, 'html.parser', from_encoding='euc-kr')
list = soup.select('.movieTime')

for movie in list:
    if '알라딘' in str(movie) and '4DX' in str(movie):
        print('오픈!')
        break
