from django.db import models


# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=30)
    damage = models.CharField(max_length=10)
    damage_type = models.CharField(max_length=12)
    range = models.IntegerField()
