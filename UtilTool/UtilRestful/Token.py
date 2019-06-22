#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/06/18 10:38
# @Author  : YGG
# @File    : Token.py
# @Description    : Token 认证类
import uuid
import datetime
import jwt
import mongoengine
import base64
import json
from UtilTool.Util.Config import Conf

class Token(mongoengine.Document):
    userId = mongoengine.StringField(unique=True)   #用户ID
    tokenSecret = mongoengine.StringField(max_length= 50) #密钥
    expireTime = mongoengine.DateTimeField(default=datetime.datetime.utcnow() + datetime.timedelta(hours = 6) ) #过期时间
    meta = {
           'indexes': [
               {'fields': ['expireTime'], 'expireAfterSeconds': 0}
           ]
       }

class jwtHelper:
    #获取jwt签发认证
    @staticmethod
    def _generate_jwt_token(userId , signToken = str(uuid.uuid1())):
        jwtToken = jwt.encode({
            'userId' : userId,
            'SignToken' : signToken
        }, Conf.getSysValue('jwtKey')).decode('utf-8').split('.')
        #保存token
        Token(userId = userId,tokenSecret = jwtToken[2]).save()
        return  jwtToken[1]

    @staticmethod
    def _jwt_isValid(TokenStr):
        payBase64 = TokenStr
        if(len(TokenStr)%3 == 1):
            payBase64 = TokenStr + "=="
        elif(len(TokenStr)%3 == 2):
            payBase64 = TokenStr + "="
        UserPayload = json.loads(base64.b64decode(payBase64).decode('utf-8'))
        userId = UserPayload['userId']
        signToken = UserPayload['SignToken']
        #查找
        TokenList = Token.objects( userId = userId)
        if len( TokenList ) < 1:
            raise Exception('令牌过期，重新登录！')
        else:
            tokenSecret = TokenList[0]['tokenSecret']
            #解密Token
            jwtToken = jwt.decode( Conf.getSysValue('jwtHeader') + '.' +  TokenStr + '.' + tokenSecret , Conf.getSysValue('jwtKey'))
            if( signToken != jwtToken['SignToken']):
                 raise Exception('令牌校验有误!')







if __name__ == '__main__':
    mongoengine.connect('gis')

    token = jwtHelper._generate_jwt_token(userId = '111psspddp121sss')
    try:
        jwtHelper._jwt_isValid(token)
    except Exception as e:
        print(e)

