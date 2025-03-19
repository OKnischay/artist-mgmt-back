from django.db import models
from core.base.choices import GenreChoices
from core.base.models import BaseModel
from apps.artists.models import Artist
from django.utils.timezone import now
# Create your models here.
class Song(BaseModel):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE, related_name='songs')
    album_name = models.CharField(max_length=255)
    genre = models.CharField(choices=GenreChoices)
    release_date = models.DateField(default=now)

    def __str__(self):
        return self.title