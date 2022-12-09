from distutils.text_file import TextFile
from random import choices
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from multiselectfield import MultiSelectField
from django.db import models
from django.conf import settings


# Create your models here.
class DogArticle(models.Model):
    title = models.CharField(max_length=20)
    # 반려동물 이름
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    content = models.TextField()
    image = ProcessedImageField(
        blank=False,
        processors=[ResizeToFill(550, 500)],
        format="JPEG",
        options={"quality": 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 반려동물 나이
    age = models.IntegerField()
    # 북마크
    bookmarks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dogarticle_bookmark')
    # 성별
    gender_list = [
        ('암컷', '암컷'),
        ('수컷', '수컷'), 
    ]
    gender = models.CharField(max_length=20, choices=gender_list)
    # 조회수
    hits = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 견종
    dog_breed = models.ForeignKey('articles.DogCategory', on_delete=models.CASCADE,)
    # 특이사항
    memo = models.CharField(max_length=20)
    # 중성화 여부
    neutered = models.BooleanField("중성화 했나요?", default=False)
    # 접종 여부
    vaccination = models.BooleanField("예방접종 했나요?", default=False)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

class DogArticleComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    dogarticle = models.ForeignKey(DogArticle, on_delete=models.CASCADE)


class CatArticle(models.Model):
    title = models.CharField(max_length=20)
    # 반려동물 이름
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    content = models.TextField()
    image = ProcessedImageField(
        blank=False,
        processors=[ResizeToFill(550, 500)],
        format="JPEG",
        options={"quality": 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 반려동물 나이
    age = models.IntegerField()
    # 북마크
    bookmarks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='catarticle_bookmark')
    # 성별
    gender_list = [
        ('암컷', '암컷'),
        ('수컷', '수컷'), 
    ]
    gender = models.CharField(max_length=20, choices=gender_list)
    # 조회수
    hits = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 견종
    cat_breed = models.ForeignKey('articles.CatCategory', on_delete=models.CASCADE)
    # 특이사항
    memo = models.CharField(max_length=20)
    # 중성화 여부
    neutered = models.BooleanField("중성화 했나요?", default=False)
    # 접종 여부
    vaccination = models.BooleanField("예방접종 했나요?", default=False)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
  


class CatArticleComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    catarticle = models.ForeignKey(CatArticle, on_delete=models.CASCADE)


class CatCategory(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
      return self.name

class DogCategory(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
      return self.name