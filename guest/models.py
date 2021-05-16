from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings

# Create your models here.
class Guest(models.Model):
    # user: 현재 사용자, person: 해당 미니홈피 주인
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='person')
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
