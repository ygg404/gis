# coding:utf-8

import os
import re
import time
import random
import bs4
import execjs
import fake_useragent
import requests
from bs4 import BeautifulSoup #用于代替正则式 取源码中相应标签中的内容

class DownloadPage:
    def __init__(self,threadname = ''):
        self.threadName = threadname
        self.novelName = ''

    def get_content(self, url):
        while True:
            try:
                ua = fake_useragent.UserAgent()
                headers = {
                    'User_Agent': ua.random}
                response = requests.get(url, headers=headers)
                a = response.content.decode('utf-8','ignore')
                break
            except Exception as e:
                print(self.threadName + ':异常 睡眠---'  )
                time.sleep(random.choice(range(2, 4)))
        return a

    def get_page_chapter(self, url, dir_path):
        html = self.get_content(url)
        soup = BeautifulSoup( html ,'html.parser')
        self.novelName = soup.find('meta', property="og:title")['content']
        print ( '漫画名称：' + self.novelName)
        sectionList =  soup.find_all(attrs={'class':'pure-u-1-2 pure-u-lg-1-4'})
        for section in sectionList:
            manurl = section.a['href']
            title = section.a.next
            print( manurl)
            print( title)
            self.download_chapter(url + manurl , title ,dir_path)

    def get_image(self, img_urls):
        #设置一个超时时间 取随机数 是为了防止网站被认定为爬虫
        timeout = random.choice(range(50,130))
        while True:
            try:
                req = requests.get(url=img_urls, timeout = timeout,)
                break
            except Exception as e:
                print(self.threadName + ':异常 睡眠---'  )
                time.sleep(random.choice(range(2, 4)))

        if req.status_code == 200:
            return req.content

    def download_chapter(self, url, chapter_name, dir_path):
        for page in range(0,100):
            html = self.get_content(url + 'index_' + str(page) + '.html')
            if html == '404!':
                break
            else:
                list = re.findall('var mhurl="(.*?)"',html)
                if list.__len__() > 0:
                    if isinstance(url, str):
                        if url:
                            image_path = dir_path +  '/' + self.novelName + '/' + chapter_name + '/P-%s.jpg' % str(page)
                            if not os.path.exists(dir_path + '/' + self.novelName + '/' + chapter_name):
                                os.makedirs(dir_path + '/' + self.novelName + '/' + chapter_name)
                            if not os.path.exists(image_path):
                                image = self.get_image("http://p2.manhuapan.com/" + list[0])
                                if image:
                                    with open(image_path, 'wb') as f:
                                        f.write(image)
                                        print( self.threadName + ":" + image_path )

        # search_obj = re.findall(r'packed="(.+)";eval', content, re.S)
        # count = 1
        # for url2 in self.base_64_decode(search_obj[0]):
        #     if isinstance(url2, str):
        #         if url2:
        #             image_path = dir_path +  '/' + self.novelName + '/' + chapter_name + '/P-%s.jpg' % count
        #             if not os.path.exists(dir_path + '/' + self.novelName + '/' + chapter_name):
        #                 os.makedirs(dir_path + '/' + self.novelName + '/' + chapter_name)
        #             if not os.path.exists(image_path):
        #                 image = self.get_image("http://res.img.fffimage.com/" + url2)
        #                 if image:
        #                     with open(image_path, 'wb') as f:
        #                         f.write(image)
        #                         print( self.threadName + ":" + image_path )
        #                         count += 1
