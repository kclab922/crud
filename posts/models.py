from django.db import models

# Create your models here.

# 장고에 내장된 model 기능을 부모로 데려와서 상속
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


