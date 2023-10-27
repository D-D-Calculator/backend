from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=30, unique=True)
    speed = models.IntegerField()
    alignment = models.CharField(max_length=20, null=True)
    starting_proficiencies = models.ForeignKey(
        "proficiencies.Proficiency", on_delete=models.CASCADE, related_name="races"
    )
    languages = models.ForeignKey(
        "languages.Language", on_delete=models.PROTECT, related_name="races"
    )
    characters = models.ForeignKey(
        "characters.Character", on_delete=models.PROTECT, related_name="races"
    )

    # Rows a serem adicionadas
    #
    # traits = models.ForeignKey("")
