from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Teams(models.Model):
    group = models.CharField(unique=True, max_length=255)
    image = models.ImageField(upload_to='media/groups/', default='groups/default_logo.png')
    bio = models.CharField(max_length=750, default='We are the greatest company')
    title = models.CharField(max_length=100, null=True)
    created_by = models.CharField(max_length=255, null=True)


class Tasks(models.Model):
    group_id = models.CharField(max_length=255, null=True)
    tasks = models.CharField(null=True, max_length=1000000)
    begins = models.DateTimeField()
    ends = models.DateTimeField()
    to = models.CharField(max_length=10000, unique=False, null=True)