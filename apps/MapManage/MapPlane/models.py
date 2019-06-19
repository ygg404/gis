from django.db import models
import mongoengine

# Create your models here.
class MapModel(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    x = mongoengine.IntField(default=0)
    y = mongoengine.IntField(default=0)
    z = mongoengine.IntField(default=0)