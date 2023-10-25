from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=144, unique=True)
    is_superuser = models.BooleanField(null=True, default=False)
    password = models.CharField(max_length=50)

    characters = models.ForeignKey(
        "characters.Character", on_delete=models.CASCADE, related_name="users"
    )
