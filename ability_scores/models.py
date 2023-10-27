from django.db import models


class AbilityScore(models.Model):
    name = models.CharField(max_length=22)
    ability_characters = models.ForeignKey(
        "ability_scores_characters.AbilityScoreCharacter",
        on_delete=models.PROTECT,
        related_name="ability_score",
    )
