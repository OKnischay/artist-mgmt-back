from django.contrib import admin

# Register your models here.
from apps.songs.models import Song

admin.site.register(Song)