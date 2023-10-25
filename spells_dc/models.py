from django.db import models


class SpellDc(models.Model):
    dc_success = models.CharField(max_length=30)
    description = models.TextField(max_length=200, null=True)

    dc_type = models.OneToOneField(
        "ability_scores.AbilityScores", on_delete=models.PROTECT, related_name="spells"
    )
