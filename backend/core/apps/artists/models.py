from django.db import models
from core.base.models import Profile
from apps.users.models import CustomUser
# Create your models here.
class Artist(Profile):
    stage_name = models.CharField(unique=True,verbose_name="Stage Name", null=True)
    first_release_year = models.PositiveIntegerField()
    no_of_albums_released = models.PositiveIntegerField(default=0)

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="artist", default=0
    )

    def __str__(self):
        return self.stage_name