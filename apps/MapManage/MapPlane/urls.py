from django.conf.urls import url,include
from apps.MapManage.MapPlane.views import *

urlpatterns = [
    url(r'^GetMapInfo', GetMapInfo, name='GetMapInfo'),
]