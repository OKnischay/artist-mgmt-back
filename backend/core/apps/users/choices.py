from django.db import models

class GenderChoices(models.TextChoices):
    Male = "M"
    Female = "F"
    Others = "O"

class RoleChoices(models.TextChoices):
    super_admin = "Super Admin"
    artist_manager = "Artist Manager"
    artist = "Artist"