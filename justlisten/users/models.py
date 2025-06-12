from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="users/pfp", blank=True, null=True, verbose_name="avatar")