#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests #用来抓取网页的html源码
import random   #取随机数
import time #时间相关操作
from bs4 import BeautifulSoup #用于代替正则式 取源码中相应标签中的内容
from list import get_content

if __name__ == '__main__':
    serverurl = 'https://www.iimanhua.com'
    url = 'https://www.iimanhua.com/comic/2362/'

    html = get_content(url + '343603.html?page=1')
    soup = BeautifulSoup( html ,'html.parser')
    # 小说图片
    sectionList = soup.find(attrs={'id':'play_0'}).ul.find_all('li')

