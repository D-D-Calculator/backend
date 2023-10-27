from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=22, unique=True)
    description = models.TextField(max_length=200, null=True)
    ability_scores = models.ForeignKey(
        "ability_scores.AbilityScore", on_delete=models.PROTECT, related_name="skills"
    )
