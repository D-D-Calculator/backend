from django.db import models


# Create your models here.
class ProficiencyChoices(models.Model):
    description = models.CharField(max_length=22, unique=True)
    proficiency_choose = models.IntegerField()

    proficiencies = models.ForeignKey(
        "proficiencies.Proficiency",
        on_delete=models.PROTECT,
        related_name="proficiencies_choices",
    )
