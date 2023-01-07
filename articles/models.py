from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class DiaryArticle(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    # saved to 'MEDIA_ROOT/images'
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(150,180)],
        format='JPEG',
        options={'quality': 80},
    )
    hashtag = models.CharField(max_length=30, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0, verbose_name='좋아요')
    hearts = models.PositiveIntegerField(default=0, verbose_name='하트')
    funny = models.PositiveIntegerField(default=0, verbose_name='웃겨요')
    sad = models.PositiveIntegerField(default=0, verbose_name='슬퍼요')
    hits = models.PositiveIntegerField(default=0, verbose_name='조회수')