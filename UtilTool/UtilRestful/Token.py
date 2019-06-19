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

class Token(mongoengine.Document):
    userId = mongoengine.StringField(unique=True)   #用户ID
    SignToken = mongoengine.StringField(max_length= 40)  #用户名对应签名Token
    expireTime = mongoengine.DateTimeField(default=datetime.datetime.utcnow() + datetime.timedelta(hours = 6) ) #过期时间
    meta = {
           'indexes': [
               {'fields': ['expireTime'], 'expireAfterSeconds': 0}
           ]
       }

    #获取jwt签发认证
    def _generate_jwt_token(self):
        token = jwt.encode({
            'userId' : self.userId,
            'SignToken' : self.SignToken
        }, 'secret_key_ygg')
        return token



if __name__ == '__main__':

    mongoengine.connect('gis')
    token = Token(userId = '1122',SignToken = str(uuid.uuid1()) ).save()
    jwtTokenstr = token._generate_jwt_token().decode('utf-8')
    print ( jwtTokenstr )

    try:
        #解密Token
        jwtToken = jwt.decode(jwtTokenstr,'secret_key_ygg')
        #查找
        TokenList = Token.objects(userId='1122')
        if len( TokenList ) < 1:
            raise Exception('Token过期，重新登录！')
        else:
            token = TokenList[0]
            if( token.SignToken != jwtToken['SignToken'] or token.userId != jwtToken['userId']):
                raise Exception('Token令牌有误!')
    except Exception:
        print(Exception)

