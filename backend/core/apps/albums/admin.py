from django.contrib import admin

# Register your models here.
from apps.albums.models import Album

admin.site.register(Album)