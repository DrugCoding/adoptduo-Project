from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail
from django.conf import settings

class User(AbstractUser):
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(200, 300)],
        format="JPEG",
        options={"quality": 50},
    )
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    area = models.CharField(max_length=20, default='서울')
