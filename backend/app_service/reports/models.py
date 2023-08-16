# Create your models here.
from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=100)
    data = models.JSONField() # 储存报告数据
    created_at = models.DateTimeField(auto_now_add=True)
    # 其他字段
