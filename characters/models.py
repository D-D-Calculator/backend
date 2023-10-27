from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50)
    alignment = models.CharField(max_length=20, null=True, default="Not Informed")

    ability_score_character = models.ForeignKey(
        "ability_scores_characters.AbilityScoreCharacter",
        on_delete=models.CASCADE,
        related_name="characters",
        default=[],
    )
    equipments = models.OneToOneField(
        "equipments.Equipment", on_delete=models.CASCADE, related_name="characters"
    )
    languages = models.ManyToManyField("languages.Language", related_name="characters")
    proficiencies = models.ManyToManyField(
        "proficiencies.Proficiency", related_name="characters"
    )
    skills = models.ManyToManyField("skills.Skill", related_name="characters")
    spells = models.ManyToManyField(
        "spells.Spell", default="Not a magic user", related_name="characters"
    )

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
