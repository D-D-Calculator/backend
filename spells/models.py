from django.db import models


class Spell(models.Model):
    name = models.CharField(max_length=50, unique=True)
    higher_level = models.CharField(max_length=40, null=True)
    description = models.TextField(max_length=200)
    range = models.CharField(max_length=20)
    components = models.CharField(max_length=60)

    classes = models.ManyToManyField("classes.Class", related_name="spells")
    dc = models.OneToOneField(
        "spells_dc.SpellDc", on_delete=models.PROTECT, related_name="spells"
    )
    damage = models.OneToOneField(
        "spells_damage.SpellDamage",
        on_delete=models.PROTECT,
        null=True,
        related_name="spells",
    )
