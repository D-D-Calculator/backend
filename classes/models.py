from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=30, unique=True)
    desc = models.TextField(max_length=200)
    hit_die = models.IntegerField()
    proficiencies_choices = models.ForeignKey(
        "proficiencies_choices.ProficiencyChoices",
        on_delete=models.CASCADE,
        related_name="classes",
    )

    characters = models.ForeignKey(
        "characters.Character", on_delete=models.PROTECT, related_name="classes"
    )
