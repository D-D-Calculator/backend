from django.db import models


class SpellDamage(models.Model):
    damage_type = models.CharField(max_length=40)
    damage_at_character_level = models.CharField(max_length=40, null=True)
    damage_at_short_level = models.CharField(max_length=40, null=True)
