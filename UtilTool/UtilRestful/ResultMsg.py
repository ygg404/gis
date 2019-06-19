#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/06/18 10:44
# @Author  : YGG
# @File    : ResultMsg.py
# @Description    : 请求结果

class ResultMsg():
    def __init__(self):
        #状态码
        self.StatusCode = int
        #操作信息
        self.Info = ''
        #返回数据
        self.Data = object
        #服务器端返回的发送信息编号
        self.MSGID = ''

    def toJsonDist(self):
        json_dict = \
            {
                'StatusCode' : self.StatusCode.value,
                'Info' : self.Info,
                'Data' : self.Data,
                'MSGID' : self.MSGID
            }
        return json_dict



