from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

def image_upload_to(instance, filename):
    return f'workspace/media/users/{filename}'


class User(AbstractUser):
    role = models.CharField(max_length=255)
    team = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to=image_upload_to, null=True, default='users/default.jpg')
    nickname = models.CharField(max_length=55, null=True)
