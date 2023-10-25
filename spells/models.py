from django.db import models


class Spells(models.Model):
    name = models.CharField(max_length=50)
    higher_level = models.CharField(null=True)
    desc = models.TextField(max_length=200)
    range = models.CharField()
    components = models.CharField()

    classes = models.ManyToManyField("classes.Class", related_name="spells")
    dc = models.OneToOneField("spells_dc.SpellDamage", related_name="spells")
    damage = models.OneToOneField(
        "spells_damage.SpellDamage",
        null=True,
        related_name="spells",
    )
    proficiencies_choices = models.ForeignKey(
        "proficiencies_choices.ProficiencyChoice", on_delete=models.CASCADE
    )
