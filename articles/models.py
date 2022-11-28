from distutils.text_file import TextFile
from random import choices
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from multiselectfield import MultiSelectField
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    # 반려동물 이름
    name = models.CharField(max_length=20)
    content = models.TextField()
    image = ProcessedImageField(
        blank=True,
        processors=[ResizeToFill(200, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 반려동물 나이
    age = models.IntegerField()
    # 북마크
    bookmarks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='article_bookmark')
    # 성별
    gender = models.CharField(max_length=20)
    # 조회수
    hits = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 견종
    breed = models.CharField(max_length=20)
    # 특이사항
    memo = models.CharField(max_length=20)
    # 중성화 여부
    neutered = models.CharField(max_length=20)
    # 접종 여부
    vaccination = models.CharField(max_length=20)

class ArticleComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)