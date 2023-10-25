from django.db import models


class SpellDamage(models.Model):
    damage_type = models.CharField()
    damage_at_character_level = models.CharField(null=True)
    damage_at_short_level = models.CharField(null=True)
