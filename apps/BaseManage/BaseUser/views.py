from django.shortcuts import render,HttpResponse
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.BaseManage.BaseUser.models import BaseUserEntity
from apps.BaseManage.BaseUser.serializers import BaseUserSerializer
from UtilTool.UtilRestful.ResultMsg import *
from UtilTool.UtilRestful.ApiEnum import *

@api_view(['GET'])
def hello_world(request):
    userlist = BaseUserEntity.objects.all()
    userlistSerializer = BaseUserSerializer(userlist, many=True)
    return JsonResponse(userlistSerializer.data,safe = False )

@api_view(['GET'])
def myjson(request):
    userlist = BaseUserEntity.objects.all()
    userlistSerializer = BaseUserSerializer(userlist, many=True)
    result = ResultMsg();
    result.Data = userlistSerializer.data
    result.StatusCode = StatusCodeEnum.Success
    return JsonResponse(result.toJsonDist() ,safe=False)

# """注册"""
# @api_view(['GET'])
# def Register(request):


class GetUserInfo(APIView):
    def get(self,request,format = None):
        userlist = BaseUserEntity.objects.all()
        userlistSerializer = BaseUserSerializer(userlist)
        return HttpResponse(userlistSerializer.data)
