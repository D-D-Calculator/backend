from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=20, unique=True)
    speed = models.IntegerField()
    alignment = models.CharField(null=True)
    starting_proficiencies = models.ForeignKey("proficiencies.Proficiency")
    languages = models.ForeignKey("languages.Language", related_name="races")
    character = models.ForeignKey("characters.Character", related_name="races")

    # Rows a serem adicionadas
    #
    # traits = models.ForeignKey("")
