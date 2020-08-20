from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.EmailField(unique=True)
    # first_name = models.CharField(max_length=30)
    REQUIRED_FIELDS = ['email', 'first_name']

    def __str__(self):
        return self.username
