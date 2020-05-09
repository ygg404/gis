from rest_framework import serializers

from apps.ManManage.ManImg.models import ManImgEntity

"""Serializer"""
class ManImgSerializer(serializers.Serializer):

    class Meta:
        model = ManImgEntity
        db_table = 'man_img'
