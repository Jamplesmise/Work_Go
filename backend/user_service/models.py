from django.db import models

class CustomUser(models.Model):
    # 根据需求添加额外的字段
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    # 其他自定义字段...
    user_name = models.CharField(max_length=50, verbose_name='User Name')
    email = models.CharField(max_length=50,verbose_name='Email')
    password = models.CharField(max_length=50,verbose_name='Password')

    def set_password(self, password):
        pass