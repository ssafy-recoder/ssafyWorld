from django.db import models
from django.conf import settings

# Create your models here.
class HomeComment(models.Model):
    content = models.CharField(max_length=20, null=False, blank=False)
    # writer는 User model에 들어가야하는 foreignKey 인데 
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="writer")
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Homepage(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    profile_content = models.TextField(max_length=100)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    
