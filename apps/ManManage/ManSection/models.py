from django.db import models

""""""
class ManSectionEntity(models.Model):
    #自增id
    sectionId = models.IntegerField(db_column='sectionId', blank=True, null=True)  
    #章节ID
    manId = models.IntegerField(db_column='manId', blank=True, null=True)  
    #漫画书名Id
    title = models.CharField(max_length=255, blank=True, null=True)
    #章节名

    class Meta:
        managed = False
        db_table = 'man_section'
