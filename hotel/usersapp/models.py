from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class HotelUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_guest = models.BooleanField(default=True)