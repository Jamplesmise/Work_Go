# Create your models here.
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    assigned_to = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=50)
    # 其他字段
