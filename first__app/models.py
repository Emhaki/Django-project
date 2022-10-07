from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField((""), auto_now_add=True)
