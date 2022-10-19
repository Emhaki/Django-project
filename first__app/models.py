from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField((""), auto_now_add=True)
    coin = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    coin = models.IntegerField(default=1)
    user = models.ForeignKey(Post, on_delete=models.CASCADE)
