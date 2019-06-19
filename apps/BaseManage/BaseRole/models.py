from django.db import models

"""角色信息表"""
class BaseRole(models.Model):
    #角色主键
    RoleId = models.CharField(db_column='RoleId', primary_key=True, max_length=50)  
    #机构主键
    OrganizeId = models.CharField(db_column='OrganizeId', max_length=50, blank=True, null=True)  
    #分类1-角色2-岗位3-职位4-工作组
    Category = models.IntegerField(db_column='Category', blank=True, null=True)  
    #角色编码
    EnCode = models.CharField(db_column='EnCode', max_length=50, blank=True, null=True)  
    #角色名称
    FullName = models.CharField(db_column='FullName', max_length=50, blank=True, null=True)  
    #公共角色
    IsPublic = models.IntegerField(db_column='IsPublic', blank=True, null=True)  
    #过期时间
    OverdueTime = models.DateTimeField(db_column='OverdueTime', blank=True, null=True)  
    #排序码
    SortCode = models.IntegerField(db_column='SortCode', blank=True, null=True)  
    #删除标记
    DeleteMark = models.IntegerField(db_column='DeleteMark', blank=True, null=True)  
    #有效标志
    EnabledMark = models.IntegerField(db_column='EnabledMark', blank=True, null=True)  
    #备注
    Description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  
    #创建日期
    CreateDate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  
    #创建用户主键
    CreateUserId = models.CharField(db_column='CreateUserId', max_length=50, blank=True, null=True)  
    #创建用户
    CreateUserName = models.CharField(db_column='CreateUserName', max_length=50, blank=True, null=True)  
    #修改日期
    ModifyDate = models.DateTimeField(db_column='ModifyDate', blank=True, null=True)  
    #修改用户主键
    ModifyUserId = models.CharField(db_column='ModifyUserId', max_length=50, blank=True, null=True)  
    #修改用户
    ModifyUserName = models.CharField(db_column='ModifyUserName', max_length=50, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'base_role'
