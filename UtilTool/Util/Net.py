#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/06/18 16:55
# @Author  : YGG
# @File    : Net.py
# @Description    :  网络帮助类

class Net:
    @staticmethod
    def GetLanIp(request):
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        return ip
