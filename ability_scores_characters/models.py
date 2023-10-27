from django.db import models


class AbilityScoreCharacter(models.Model):
    name = models.CharField(max_length=22)
    value = models.IntegerField()
