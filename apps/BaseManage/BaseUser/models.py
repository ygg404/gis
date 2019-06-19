from django.db import models

"""用户信息表"""
class BaseUserEntity(models.Model):
    #用户主键
    UserId = models.CharField(db_column='UserId', primary_key=True, max_length=50)  
    #用户编码
    EnCode = models.CharField(db_column='EnCode', max_length=50, blank=True, null=True)  
    #登录账户
    Account = models.CharField(db_column='Account', max_length=50, blank=True, null=True)  
    #登录密码
    Password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  
    #PDA帐号
    PdaAccount = models.CharField(db_column='PdaAccount', max_length=50, blank=True, null=True)  
    #PDA密码
    PdaPassword = models.CharField(db_column='PdaPassword', max_length=50, blank=True, null=True)  
    #移动帐号
    MobileAccount = models.CharField(db_column='MobileAccount', max_length=50, blank=True, null=True)  
    #移动密码
    MobilePassword = models.CharField(db_column='MobilePassword', max_length=50, blank=True, null=True)  
    #密码秘钥
    Secretkey = models.CharField(db_column='Secretkey', max_length=50, blank=True, null=True)  
    #真实姓名
    RealName = models.CharField(db_column='RealName', max_length=50, blank=True, null=True)  
    #呢称
    NickName = models.CharField(db_column='NickName', max_length=50, blank=True, null=True)  
    #头像
    HeadIcon = models.CharField(db_column='HeadIcon', max_length=200, blank=True, null=True)  
    #快速查询
    QuickQuery = models.CharField(db_column='QuickQuery', max_length=200, blank=True, null=True)  
    #简拼
    SimpleSpelling = models.CharField(db_column='SimpleSpelling', max_length=200, blank=True, null=True)  
    #性别
    Gender = models.IntegerField(db_column='Gender', blank=True, null=True)  
    #生日
    Birthday = models.DateTimeField(db_column='Birthday', blank=True, null=True)  
    #手机
    Mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  
    #电话
    Telephone = models.CharField(db_column='Telephone', max_length=50, blank=True, null=True)  
    #电子邮件
    Email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  
    #QQ号
    OICQ = models.CharField(db_column='OICQ', max_length=50, blank=True, null=True)  
    #微信号
    WeChat = models.CharField(db_column='WeChat', max_length=50, blank=True, null=True)  
    #MSN
    MSN = models.CharField(db_column='MSN', max_length=50, blank=True, null=True)  
    #主管主键
    ManagerId = models.CharField(db_column='ManagerId', max_length=50, blank=True, null=True)  
    #主管
    Manager = models.CharField(db_column='Manager', max_length=50, blank=True, null=True)  
    #机构主键
    OrganizeId = models.CharField(db_column='OrganizeId', max_length=50, blank=True, null=True)  
    #部门主键
    DepartmentId = models.CharField(db_column='DepartmentId', max_length=50, blank=True, null=True)  
    #角色主键
    RoleId = models.CharField(db_column='RoleId', max_length=50, blank=True, null=True)  
    #岗位主键
    DutyId = models.CharField(db_column='DutyId', max_length=50, blank=True, null=True)  
    #岗位名称
    DutyName = models.CharField(db_column='DutyName', max_length=50, blank=True, null=True)  
    #职位主键
    PostId = models.CharField(db_column='PostId', max_length=50, blank=True, null=True)  
    #职位名称
    PostName = models.CharField(db_column='PostName', max_length=50, blank=True, null=True)  
    #工作组主键
    WorkGroupId = models.CharField(db_column='WorkGroupId', max_length=50, blank=True, null=True)  
    #安全级别
    SecurityLevel = models.IntegerField(db_column='SecurityLevel', blank=True, null=True)  
    #在线状态
    UserOnLine = models.IntegerField(db_column='UserOnLine', blank=True, null=True)  
    #单点登录标识(微信系统代表微信OpenId)
    OpenId = models.CharField(db_column='OpenId', max_length=50, blank=True, null=True)  
    #密码提示问题
    Question = models.CharField(db_column='Question', max_length=50, blank=True, null=True)  
    #密码提示答案
    AnswerQuestion = models.CharField(db_column='AnswerQuestion', max_length=50, blank=True, null=True)  
    #允许多用户同时登录
    CheckOnLine = models.IntegerField(db_column='CheckOnLine', blank=True, null=True)  
    #允许登录时间开始
    AllowStartTime = models.DateTimeField(db_column='AllowStartTime', blank=True, null=True)  
    #允许登录时间结束
    AllowEndTime = models.DateTimeField(db_column='AllowEndTime', blank=True, null=True)  
    #暂停用户开始日期
    LockStartDate = models.DateTimeField(db_column='LockStartDate', blank=True, null=True)  
    #暂停用户结束日期
    LockEndDate = models.DateTimeField(db_column='LockEndDate', blank=True, null=True)  
    #第一次访问时间
    FirstVisit = models.DateTimeField(db_column='FirstVisit', blank=True, null=True)  
    #上一次访问时间
    PreviousVisit = models.DateTimeField(db_column='PreviousVisit', blank=True, null=True)  
    #最后访问时间
    LastVisit = models.DateTimeField(db_column='LastVisit', blank=True, null=True)  
    #登录次数
    LogOnCount = models.IntegerField(db_column='LogOnCount', blank=True, null=True)  
    #排序码
    SortCode = models.IntegerField(db_column='SortCode', blank=True, null=True)  
    #删除标记
    DeleteMark = models.IntegerField(db_column='DeleteMark', blank=True, null=True)  
    #有效标志
    EnabledMark = models.IntegerField(db_column='EnabledMark', blank=True, null=True)  
    #窜货通知标记（0：不通知，1：通知）
    FeeingNoticeMark = models.IntegerField(db_column='FeeingNoticeMark', blank=True, null=True)  
    #通知绑定
    NoticeMark = models.IntegerField(db_column='NoticeMark', blank=True, null=True)  
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
        db_table = 'base_user'
