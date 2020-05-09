from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.ManManage.ManImg.models import ManImgEntity
from apps.ManManage.ManImg.serializers import ManImgSerializer
from UtilTool.UtilRestful.ResultMsg import *
from UtilTool.UtilRestful.ApiEnum import *

# Create your views here.
@api_view(['GET'])
def index(request):
    manlist = ManImgEntity.objects.all()
    manlistSerializer = ManImgSerializer(manlist, many=True)
    result = ResultMsg();
    result.Data = manlistSerializer.data
    result.StatusCode = StatusCodeEnum.Success
    return JsonResponse(result.toJsonDist() ,safe=False)

@api_view(['GET'])
def getlist(request):
    manlist = ManImgEntity.objects.all()
    manlistSerializer = ManImgSerializer(manlist, many=True)
    result = ResultMsg();
    result.Data = manlistSerializer.data
    result.StatusCode = StatusCodeEnum.Success
    return JsonResponse(result.toJsonDist() ,safe=False)