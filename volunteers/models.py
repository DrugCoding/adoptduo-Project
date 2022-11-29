from distutils.text_file import TextFile
from random import choices
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from multiselectfield import MultiSelectField
from django.db import models
from django.conf import settings

# Create your models here.
class Volunteer(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = ProcessedImageField(
        blank=True,
        processors=[ResizeToFill(200, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 북마크
    bookmarks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='volunteer_bookmark')
    # 조회수
    hits = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 견종
    breed = models.CharField(max_length=20)
    # 지역
    adopt_location = models.CharField(max_length=20)
    # 날짜
    adopt_date = models.DateField()

class VolunteerComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    article = models.ForeignKey(Volunteer, on_delete=models.CASCADE)