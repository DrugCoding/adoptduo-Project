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
    content = models.TextField()
    image = ProcessedImageField(
        blank=True,
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
    breed_list = [
        ('포메라니안', '포메라니안'),
        ('웰시코기', '웰시코기'), 
        ('말티즈', '말티즈'), 
        ('시츄', '시츄'), 
        ('푸들', '푸들'), 
        ('비숑', '비숑'), 
        ('시바견', '시바견'), 
        ('골든 리트리버', '골든 리트리버'), 
    ]
    breed = models.CharField(max_length=20, choices=breed_list)
    # 특이사항
    memo = models.CharField(max_length=20)
    # 중성화 여부
    neutered_list = [
        ('Yes', 'Yes'),
    ]
    neutered = models.CharField(max_length=20, choices=neutered_list)
    # 접종 여부
    vaccination_list = [
        ('Yes', 'Yes'),
    ]
    vaccination = models.CharField(max_length=20, choices=vaccination_list)

class DogArticleComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    dogarticle = models.ForeignKey(DogArticle, on_delete=models.CASCADE)


class CatArticle(models.Model):
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
    breed_list = [
        ('페르시안', '페르시안'),
        ('러시안블루', '러시안블루'), 
        ('샴', '샴'), 
        ('렉돌', '렉돌'), 
        ('스코티쉬폴드', '스코티쉬폴드'), 
    ]
    breed = models.CharField(max_length=20, choices=breed_list)
    # 특이사항
    memo = models.CharField(max_length=20)
    # 중성화 여부
    neutered_list = [
        ('Yes', 'Yes'),
    ]
    neutered = models.CharField(max_length=20, choices=neutered_list)
    # 접종 여부
    vaccination_list = [
        ('Yes', 'Yes'),
    ]
    vaccination = models.CharField(max_length=20, choices=vaccination_list)


class CatArticleComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    catarticle = models.ForeignKey(CatArticle, on_delete=models.CASCADE)
