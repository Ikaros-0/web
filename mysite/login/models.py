from email.policy import default
from random import choices
from secrets import choice
from django.db import models

# Create your models here.
# 创建用户表
# @name: 用户名/账号
# @password: 密码
# @email: 邮箱
# @sex: 性别
# @c_time: 创建时间  
class User(models.Model):
    
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True, default=None)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField('创建时间', auto_now_add=True)


    class Meta:
        ordering = ['-c_time']
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.name
