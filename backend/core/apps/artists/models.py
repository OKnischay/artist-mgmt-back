from django.db import models
from core.base.models import Profile

# Create your models here.
class Artist(Profile):
    stage_name = models.CharField(unique=True,verbose_name="Stage Name", null=True)
    first_release_year = models.PositiveIntegerField()
    no_of_albums_released = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.stage_name