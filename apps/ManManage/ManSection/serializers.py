from rest_framework import serializers

from apps.ManManage.ManSection.models import ManSectionEntity

"""Serializer"""
class ManSection(serializers.Serializer):

    class Meta:
        model = ManSectionEntity
        db_table = 'man_section'
