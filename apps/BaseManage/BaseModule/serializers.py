from rest_framework import serializers
import Models.BaseModule.models as BaseModuleModel

"""系统功能表Serializer"""
class BaseModule(serializers.Serializer):
    #功能主键
    ModuleId = serializers.CharField(db_column='ModuleId', primary_key=True, max_length=50)  
    #父级主键
    ParentId = serializers.CharField(db_column='ParentId', max_length=50, blank=True, null=True)  
    #编码
    EnCode = serializers.CharField(db_column='EnCode', max_length=50, blank=True, null=True)  
    #名称
    FullName = serializers.CharField(db_column='FullName', max_length=50, blank=True, null=True)  
    #图标
    Icon = serializers.CharField(db_column='Icon', max_length=50, blank=True, null=True)  
    #导航地址
    UrlAddress = serializers.CharField(db_column='UrlAddress', max_length=200, blank=True, null=True)  
    #导航目标
    Target = serializers.CharField(db_column='Target', max_length=20, blank=True, null=True)  
    #菜单选项
    IsMenu = serializers.IntegerField(db_column='IsMenu', blank=True, null=True)  
    #允许展开
    AllowExpand = serializers.IntegerField(db_column='AllowExpand', blank=True, null=True)  
    #是否公开
    IsPublic = serializers.IntegerField(db_column='IsPublic', blank=True, null=True)  
    #允许编辑
    AllowEdit = serializers.IntegerField(db_column='AllowEdit', blank=True, null=True)  
    #允许删除
    AllowDelete = serializers.IntegerField(db_column='AllowDelete', blank=True, null=True)  
    #排序码
    SortCode = serializers.IntegerField(db_column='SortCode', blank=True, null=True)  
    #删除标记
    DeleteMark = serializers.IntegerField(db_column='DeleteMark', blank=True, null=True)  
    #有效标志
    EnabledMark = serializers.IntegerField(db_column='EnabledMark', blank=True, null=True)  
    #备注
    Description = serializers.CharField(db_column='Description', max_length=200, blank=True, null=True)  
    #创建日期
    CreateDate = serializers.DateTimeField(db_column='CreateDate', blank=True, null=True)  
    #创建用户主键
    CreateUserId = serializers.CharField(db_column='CreateUserId', max_length=50, blank=True, null=True)  
    #创建用户
    CreateUserName = serializers.CharField(db_column='CreateUserName', max_length=50, blank=True, null=True)  
    #修改日期
    ModifyDate = serializers.DateTimeField(db_column='ModifyDate', blank=True, null=True)  
    #修改用户主键
    ModifyUserId = serializers.CharField(db_column='ModifyUserId', max_length=50, blank=True, null=True)  
    #修改用户
    ModifyUserName = serializers.CharField(db_column='ModifyUserName', max_length=50, blank=True, null=True)  

    class Meta:
        model = BaseModuleModel
        db_table = 'base_module'
