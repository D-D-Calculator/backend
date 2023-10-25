from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)
    alignments = models.CharField(null=True, default="Not Informed")

    ability_scores = models.ForeignKey(
        "characters.Character", related_name="characters"
    )
    equipments = models.OneToOneField("equipments.Equipment", related_name="characters")
    languages = models.ManyToManyField("languages.Language", related_name="characters")
    proficiencies = models.ManyToManyField(
        "proficiencies.Proficiency", related_name="characters"
    )
    skills = models.ForeignKey("skills.Skill", related_name="characters")
    spells = models.ForeignKey(
        "spells.Spell", null=True, default="Not a magic user", related_name="characters"
    )
    user = models.OneToOneField("users.User", related_name="characters")

    # Rows a serem adicionadas
    #
    # subclass = models.ForeignKey("sub_classes.class", related_name="characters")
    # subrace = models.ForeignKey("users.User", related_name="characters")
    # traits = models.ForeignKey("users.User", related_name="characters")
    # weapon_properties = models.ForeignKey("users.User", related_name="characters")
    # magic_items = models.ForeignKey("users.User", related_name="characters")
    #
    # outro lado da relação
    #
    # class
    # race
    # campaign
    #
    # pendente
    # doubles_proficiency
