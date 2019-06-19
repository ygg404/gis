from django.test import TestCase

# Create your tests here.
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import mongoengine
import datetime
# conn = MongoClient('127.0.0.1', 27017)
# db = conn.gis  #连接mydb数据库，没有则自动创建
# my_set = db.test #使用test_set集合，没有则自动创建
# #查询全部
# for i in my_set.find():
#     print(i)
# 如需验证和指定主机名
# connect('blog', host='192.168.3.1', username='root', password='1234')

class MapModel(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    x = mongoengine.IntField(default=0)
    y = mongoengine.IntField(default=0)
    z = mongoengine.IntField(default=0)


class TModel(mongoengine.Document):
    num = mongoengine.IntField(default = 0,unique=True)
    expireTime = mongoengine.DateTimeField(default=datetime.datetime.utcnow() - datetime.timedelta(seconds = 60) )
    meta = {
           'indexes': [
               {'fields': ['expireTime'], 'expireAfterSeconds': 0}
           ]
       }
mongoengine.connect('gis')
mydict = { "num": 1, "expireTime": datetime.datetime.utcnow() - datetime.timedelta(seconds = 30) }


TModel(num = 3 , expireTime = datetime.datetime.utcnow()).save()
TModel(num = 3 , expireTime = datetime.datetime.utcnow() + datetime.timedelta(seconds = 60) ).save()
# TModel(num = 4 , expireTime = datetime.datetime.utcnow() + datetime.timedelta(seconds = 20) ).save()
