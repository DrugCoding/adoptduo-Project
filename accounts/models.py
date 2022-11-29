from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail
from django.conf import settings

class User(AbstractUser):
    image = ProcessedImageField(
        upload_to='images/',
        blank=True,
        processors=[ResizeToFill(360, 360)],
        format="JPEG",
        options={"quality": 80},
    )
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    area = models.CharField(max_length=20, default='서울')
