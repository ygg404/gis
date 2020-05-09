from django.db import models

""""""
class ManImgEntity(models.Model):
    #自增Id
    id = models.IntegerField(blank=True,primary_key=True)
    # 章节ID
    sectionId = models.IntegerField(db_column='sectionId', blank=True, null=True)  
    #图片路径
    imgurl = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'man_img'
