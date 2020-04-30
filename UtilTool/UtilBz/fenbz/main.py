#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/04/25 09:47
# @Author  : YGG
# @File    : main.py
# @Description:

import  threading
import os
import re
import time
import random
import bs4
import execjs
import fake_useragent
import requests
from bs4 import BeautifulSoup #用于代替正则式 取源码中相应标签中的内容
from DownloadPage import *


save_path = 'F:/doman'

def thread1():
    downloadPage = DownloadPage('thread1')
    content = downloadPage.get_page_chapter('https://manhua.fzdm.com/132/', save_path)

def thread2():
    downloadPage = DownloadPage('thread2')
    content = downloadPage.get_page_chapter('https://manhua.fzdm.com/151/', save_path)

def thread3():
    downloadPage = DownloadPage('thread3')
    content = downloadPage.get_page_chapter('https://manhua.fzdm.com/150/', save_path)

def thread4():
    downloadPage = DownloadPage('thread4')
    content = downloadPage.get_page_chapter('https://manhua.fzdm.com/39/', save_path)

if __name__ == '__main__':
    # t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    # t3 = threading.Thread(target=thread3)
    # t4 = threading.Thread(target=thread4)
    # t1.start()
    t2.start()
    # t3.start()
    # t4.start()
