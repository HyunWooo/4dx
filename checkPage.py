# -*- coding: utf-8 -*-

import requests
import telegram
from datetime import datetime
from bs4 import BeautifulSoup

dir(telegram)
now = datetime.now()
my_token = '777785450:AAGS9m-hWIYg7_eYW8ZxdP85eDYHQ64JSsE'
bot = telegram.Bot(token = my_token)

url = 'http://m.cgv.co.kr/Schedule/cont/ajaxMovieSchedule.aspx'

dataList = [{'theaterCd': '0013', 'playYMD': '20190706', 'theaterNm': '용산'}, {'theaterCd': '0107', 'playYMD': '20190706', 'theaterNm': '청담'}]

for data in dataList:
    response = requests.post(url, data=data)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser', from_encoding='euc-kr')
    list = soup.select('.movieTime')

    for movie in list:
        if '알라딘' in str(movie) and '4DX' in str(movie):
            print('오픈!')
            bot.sendMessage(chat_id= '@moviegazza', text=data['theaterNm'] + ' 예매 가즈아~~~~')
            break 

if(now.minute == 35 and now.second < 10):
    bot.sendMessage(chat_id= '@moviegazza', text='정상 작동중')