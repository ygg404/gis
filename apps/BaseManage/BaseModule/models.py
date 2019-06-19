from django.db import models

"""系统功能表"""
class BaseModule(models.Model):
    #功能主键
    ModuleId = models.CharField(db_column='ModuleId', primary_key=True, max_length=50)  
    #父级主键
    ParentId = models.CharField(db_column='ParentId', max_length=50, blank=True, null=True)  
    #编码
    EnCode = models.CharField(db_column='EnCode', max_length=50, blank=True, null=True)  
    #名称
    FullName = models.CharField(db_column='FullName', max_length=50, blank=True, null=True)  
    #图标
    Icon = models.CharField(db_column='Icon', max_length=50, blank=True, null=True)  
    #导航地址
    UrlAddress = models.CharField(db_column='UrlAddress', max_length=200, blank=True, null=True)  
    #导航目标
    Target = models.CharField(db_column='Target', max_length=20, blank=True, null=True)  
    #菜单选项
    IsMenu = models.IntegerField(db_column='IsMenu', blank=True, null=True)  
    #允许展开
    AllowExpand = models.IntegerField(db_column='AllowExpand', blank=True, null=True)  
    #是否公开
    IsPublic = models.IntegerField(db_column='IsPublic', blank=True, null=True)  
    #允许编辑
    AllowEdit = models.IntegerField(db_column='AllowEdit', blank=True, null=True)  
    #允许删除
    AllowDelete = models.IntegerField(db_column='AllowDelete', blank=True, null=True)  
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
        db_table = 'base_module'
