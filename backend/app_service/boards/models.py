# Create your models here.
from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=100)

class Column(models.Model):
    name = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    # 其他如截止日期、责任人等字段
    deadline = models.DateField()
    assigned_to = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
