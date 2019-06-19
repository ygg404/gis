#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/06/18 16:55
# @Author  : YGG
# @File    : ValidateUtil.py
# @Description    : 输入辅助类
import re

class ValidateUtil:
    #手机号码有效性
    @staticmethod
    def IsValidMobile(mobile):
        return re.match(r"^1[35678]\d{9}$", mobile) != None

    #IP地址有效性
    @staticmethod
    def IsValidIP(ip):
        return  re.match(r"^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$" , ip) != None

    #邮箱有效性
    @staticmethod
    def IsEmail(email):
        return re.match(r"^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$", email) != None

