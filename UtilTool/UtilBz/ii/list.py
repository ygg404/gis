#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests #用来抓取网页的html源码
import random   #取随机数
import time #时间相关操作
from bs4 import BeautifulSoup #用于代替正则式 取源码中相应标签中的内容

def get_content(url, data = None):
    #设置headers是为了模拟浏览器访问 否则的话可能会被拒绝 可通过浏览器获取
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'br, gzip, deflate',
        'Accept-Language':'zh-cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15'
    }
    #设置一个超时时间 取随机数 是为了防止网站被认定为爬虫
    timeout = random.choice(range(80,180))

    while True:
        try:
            req = requests.get(url=url, headers = header, timeout = timeout,)
            break
        except Exception as e:
            time.sleep(random.choice(range(8, 15)))
    return req.content.decode('gb2312','ignore').encode('utf-8')

if __name__ == '__main__':
    serverurl = 'https://www.iimanhua.com'
    url = 'https://www.iimanhua.com/comic/2362/'
    html = get_content(url)
    soup = BeautifulSoup( html ,'html.parser')
    # 小说图片
    sectionList = soup.find(attrs={'id':'play_0'}).ul.find_all('li')
    for section in sectionList:
        print(section.a["href"])
        print(section.a["title"])
