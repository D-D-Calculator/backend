from django.db import models

# Create your models here.


class Campaigns(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    master = models.OneToOneField("users.User", on_delete=models.CASCADE)
    characters = models.ForeignKey(
        "characters.Character", on_delete=models.PROTECT, related_name="campaigns"
    )
