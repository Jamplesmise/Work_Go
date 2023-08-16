# Create your models here.
from django.db import models

class Notification(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    # 其他订阅选项



