from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ## 주로 다니는 지역
    group = models.CharField(max_length=255)
    like_language = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='ssafyWorld', blank=True, null=True)
    residence = models.CharField(max_length=255)