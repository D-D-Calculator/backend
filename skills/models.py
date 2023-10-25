from django.db import models


class Skill(models.Models):
    name = models.CharField(max_length=22)
    desc = models.TextField(max_length=200, null=True)
    ability_scores = models.ForeignKey("abilities_scores", related_name="skills")
