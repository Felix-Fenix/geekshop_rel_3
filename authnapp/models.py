from datetime import timedelta
from re import T
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


def get_activation_key_expiration_date():
    return now() + timedelta(hours=48)

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to="users_avatars", blank=True)
    age = models.PositiveIntegerField(verbose_name="возраст")
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expiration_date)   
