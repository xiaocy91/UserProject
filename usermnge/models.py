from django.db import models


from django.db import models

#系统管理员表 <-> 普通管理员表 <-> 运维、运维plus、开发、开发plus、测试、测试plus


class Menu(models.Model):
    '''
    1 :  新增用户
    2： 修改用户
    3： 删除用户
    4： 新增项目
    5： 修改项目
    6： 删除项目
    7： 新增-用户项目管理
    8： 修改-用户项目管理
    9： 删除-用户项目管理
    '''
    name = models.CharField(max_length=255)
    menuId = models.IntegerField()


class Role(models.Model):
    '''
    角色分类：
    运维：1
    运维plus: 2
    开发：3
    开发plus: 4
    测试： 5
    测试plus: 6
    '''
    name = models.CharField(max_length=255)
    roleId = models.IntegerField()
    menus = models.ManyToManyField(Menu)


class Pro(models.Model):
    name = models.CharField(max_length=255)
    detail = models.CharField(max_length= 255)



class NmlUser(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=10)
    roles = models.ManyToManyField( Role )
    pros = models.ManyToManyField(Pro)


class Group(models.Model):
    name = models.CharField(max_length=255)
    nmlusers = models.ManyToManyField( NmlUser )
    roles = models.ManyToManyField( Role )
    pros = models.ManyToManyField(Pro)


class GenrAdmin(models.Model):
    # 普通管理员表，用于管理用户、用户组、角色、项目
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=10)
    nmlusers = models.ManyToManyField( NmlUser )
    groups = models.ManyToManyField(Group)
    roles = models.ManyToManyField(Role)
    pros = models.ManyToManyField(Pro)

class SysAdmin(models.Model):
    #系统管理员表，只能用于，管理普通管理员
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=10)
    genradmins = models.ManyToManyField( GenrAdmin )
















