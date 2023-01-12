from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings
# Create your models here.
class DiaryArticle(models.Model):
    # article_id = models.BigAutoField(primary_key=True, default=1)
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
    
class Comments(models.Model):
    # comment_id = models.ForeignKey(DiaryArticle, related_name='article', on_delete=models.CASCADE, db_column='comment_id')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    diary_article = models.ForeignKey(DiaryArticle, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(max_length=150)
    likes = models.PositiveIntegerField(default=0, verbose_name='공감')
    comment_created_date = models.DateTimeField(auto_now_add=True)
    comment_updated_date = models.DateTimeField(auto_now=True)