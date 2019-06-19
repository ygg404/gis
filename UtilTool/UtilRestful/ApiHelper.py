#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/06/19 15:02
# @Author  : YGG
# @File    : ApiHelper.py
# @Description    : Http 请求帮助类
import requests
import json
import jwt

class ApiHelper:
    @staticmethod
    def HttpGet(url):
        headers = {
            'Accept':'application/json',
            'Connection':'keep-alive'
        }
        respone = requests.get( url ,headers = headers )
        return respone

    # @staticmethod
    # def HttpPost(url):


if __name__ == '__main__':
    response =  ApiHelper.HttpGet('http://ip.taobao.com/service/getIpInfo.php?ip=192.168.1.12')
    print ( json.loads(response.text)['code'] )