from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    send_massage = models.ManyToManyField('self', symmetrical = False, related_name = 'get_message')
