from django.shortcuts import render,HttpResponse
from rest_framework import serializers
from apps.BaseManage.BaseUser.models import BaseUserEntity

class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model  = BaseUserEntity
        fields = ('UserId', 'EnCode')
