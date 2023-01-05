from django.db import models

# Create your models here.
class DiaryArticle(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    hashtag = models.CharField(max_length=30, blank=True)