from django.contrib import admin

# Register your models here.
from apps.artists.models import Artist

admin.site.register(Artist)