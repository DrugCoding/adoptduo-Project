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
    # 자원봉사 여부
    volunteer_choice = (
        ('가능', '지원'),
        ('불가능', '미지원'),
    )
    volunteer_c = models.CharField(null=True, max_length=3, choices=volunteer_choice)
    area = models.CharField(max_length=20, default='서울')
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    name = models.CharField(max_length=20)

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_KAKAO, "Kakao"),
    )

    login_method = models.CharField(
        max_length=6, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )