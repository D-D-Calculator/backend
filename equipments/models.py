from django.db import models


# Create your models here.
class Equipments(models.Model):
    name = models.CharField(max_length=30)
    damage = models.CharField(max_length=10)
    damage_type = models.CharField(max_length=20)
    range = models.IntegerField()
