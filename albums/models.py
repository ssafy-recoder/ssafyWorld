from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return f'{self.name}'


class Photo(models.Model):
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='host')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.content}'


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'
