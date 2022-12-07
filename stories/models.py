from distutils.text_file import TextFile
from random import choices
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from multiselectfield import MultiSelectField
from django.db import models
from django.conf import settings

# Create your models here.
class Stories(models.Model):
    title = models.CharField(max_length=20)
    # 반려동물 이름
    name = models.CharField(max_length=20)
    content = models.TextField()
    image = ProcessedImageField(
        blank=True,
        processors=[ResizeToFill(900, 600)],
        format="JPEG",
        options={"quality": 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 좋아요
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='stories_like')
    # 성별
    gender = models.CharField(max_length=20)
    # 조회수
    hits = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 견종
    breed = models.CharField(max_length=20)

class StoryComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='comment_like')
    stories = models.ForeignKey(Stories, on_delete=models.CASCADE)