from rest_framework_mongoengine import serializers
from apps.MapManage.MapPlane.models import *

class MapmodelSerializer(serializers.DocumentSerializer):
        # DocumentSerializer继承自drf中的ModelSerializer，用于代替ModelSerializer序列化mongodb中的document.
        # 具体可以到官网上查看
        class Meta:
            model = MapModel
            fields = '__all__'