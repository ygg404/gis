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
    signToken = mongoengine.StringField(max_length= 40)  #用户名对应签名Token
    secret = mongoengine.StringField(max_length= 50) #密钥
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
        Token(userId = userId,signToken = signToken, secret = jwtToken[2]).save()
        return  jwtToken[1]

    @staticmethod
    def _jwt_isValid(TokenStr):
        if(len(TokenStr)%3 == 1):
            TokenStr += "=="
        elif(len(TokenStr)%3 == 2):
            TokenStr += "="
        base64.b64decode(TokenStr).decode('utf-8')
        #解密Token
        jwtToken = jwt.decode( Conf.getSysValue('jwtHeader') + TokenStr, Conf.getSysValue('jwtKey'))







if __name__ == '__main__':
    mongoengine.connect('gis')
    jwtHelper._jwt_isValid('eyJ1c2VySWQiOiIxMTExMjEiLCJTaWduVG9rZW4iOiI5YzExN2ExZS05MzA3LTExZTktOGYwMC0wNGQ0YzQwNmIxYjMifQ')
    token = jwtHelper._generate_jwt_token(userId = '111121')

    token = Token(userId = '11211sssss2222',SignToken = str(uuid.uuid1()) ).save()
    jwtTokenstr = token._generate_jwt_token().decode('utf-8')
    print ( jwtTokenstr )

    try:
        # raise Exception('test')
        #解密Token
        jwtToken = jwt.decode(jwtTokenstr,'secret_key_ygg')
        #查找
        TokenList = Token.objects( userId = jwtToken['userId'])
        if len( TokenList ) < 1:
            raise Exception('令牌过期，重新登录！')
        else:
            token = TokenList[0]
            if( token.SignToken != jwtToken['SignToken'] or token.userId != jwtToken['userId']):
                raise Exception('令牌有误!')
    except Exception as e:
        print(e)

