# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, gender, password=None):
        if not email:
            raise ValueError('用户必须有一个电子邮件地址')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            gender=gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, gender, password=None):
        user = self.create_user(
            email,
            password=password,
            username=username,
            gender=gender,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='电子邮件地址', max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True, verbose_name='用户名')
    gender = models.CharField(max_length=10, verbose_name='性别')
    # 其他的字段

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'gender']

    def __str__(self):
        return self.email


class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField('Permission')

class Permission(models.Model):
    name = models.CharField(max_length=50)
