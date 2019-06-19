from enum import Enum

class StatusCodeEnum(Enum):
    #请求(或处理)成功
    Success = 200

    #内部请求出错
    Error = 500

    #未授权标识
    Unauthorized = 401

    #请求参数不完整或不正确
    ParameterError = 400

    #请求TOKEN失效
    TokenInvalid = 403,

    #HTTP请求类型不合法
    HttpMehtodError = 405,

    #HTTP请求不合法,请求参数可能被篡改
    HttpRequestError = 406

    #该URL已经失效
    URLExpireError = 407