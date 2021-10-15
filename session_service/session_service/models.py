from django.db import models


class User(models.Model):
    user_uid = models.UUIDField(unique=True)
    login = models.CharField(max_length=31, unique=True)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField()
    current_token = models.CharField(max_length=255)
