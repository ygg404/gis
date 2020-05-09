from django.db import models

""""""
class ManNovelEntity(models.Model):
    #漫画ID
    manId = models.AutoField(db_column='manId', primary_key=True)  
    #漫画名
    manName = models.CharField(db_column='manName', max_length=255, blank=True, null=True)  
    #作者
    author = models.CharField(max_length=255, blank=True, null=True)
    #关键字
    keys = models.CharField(max_length=255, blank=True, null=True)
    #简介
    content = models.CharField(max_length=255, blank=True, null=True)
    #类别
    category = models.CharField(max_length=255, blank=True, null=True)
    #爬虫地址
    paurl = models.CharField(max_length=255, blank=True, null=True)
    #是否有效（0、无效；1、有效）
    isEnable = models.IntegerField(db_column='isEnable', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'man_novel'
