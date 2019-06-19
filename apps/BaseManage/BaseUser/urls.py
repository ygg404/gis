from django.conf.urls import url,include
from apps.BaseManage.BaseUser.views import *

urlpatterns = [
    url(r'^GetUserInfo', GetUserInfo, name='GetUserInfo'),
    url(r'^hello_world', hello_world, name='hello_world'),
    url(r'^myjson', myjson, name='myjson'),
]