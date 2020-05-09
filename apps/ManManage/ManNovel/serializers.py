from rest_framework import serializers
from apps.ManManage.ManNovel.models import ManNovelEntity

"""Serializer"""
class ManNovel(serializers.Serializer):

    class Meta:
        model = ManNovelEntity
        db_table = 'man_novel'
