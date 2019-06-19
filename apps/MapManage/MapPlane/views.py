from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from apps.MapManage.MapPlane.models import *
from apps.MapManage.MapPlane.serializers import *

# Create your views here.
@api_view(['GET'])
def GetMapInfo(request):
    mapList = MapModel.objects.all()
    mapListSerial = MapmodelSerializer(mapList , many = True)
    return JsonResponse(mapListSerial.data,safe = False )