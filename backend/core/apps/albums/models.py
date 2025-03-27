from django.db import models
from core.base.models import BaseModel
from apps.artists.models import Artist
from django.utils.timezone import now
# Create your models here.
class Album(BaseModel):
    album_name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateField(default=now)
    total_tracks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.album_name} - {self.artist.stage_name}"