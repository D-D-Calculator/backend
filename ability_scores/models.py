from django.db import models

# Create your models here.


class AbilityScores(models.Model):
    name = models.CharField(max_length=22)
    value = models.IntegerField()
