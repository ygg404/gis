#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/06/18 10:38
# @Author  : YGG
# @File    : Token.py
# @Description    : Token 认证类
import uuid
import datetime

class Token:
    def __init__(self,userId):
        #用户ID
        self.userId = userId
        #用户名对应签名Token
        self.SignToken = str(uuid.uuid1())
        #Token过期时间
        self.ExpireTime = datetime.datetime.now() + datetime.timedelta( hours = 6 )

