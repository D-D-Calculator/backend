from django.db import models


# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    hit_die = models.IntegerField()
    proficiencies_choices = models.ForeignKey(
        "proficiencies_choices.ProficiencyChoice", on_delete=models.CASCADE
    )
    characters = models.ForeignKey("characters.Character", related_name="Class")
