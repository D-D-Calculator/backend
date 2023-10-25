from django.db import models


class SpellDamage(models.Model):
    dc_type = models.OneToOneField("abilities_scores", related_name="spells")
    dc_sucess = models.CharField(max_length=30)
    desc = models.TextField(max_length=200)
