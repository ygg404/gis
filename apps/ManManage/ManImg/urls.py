from django.conf.urls import url,include
from apps.ManManage.ManImg import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^getlist/$', views.getlist),
]