# from django.utils import timezone
from apps.users.managers import CustomUserManager
from core.base.choices import GenderChoices, RoleChoices
from core.base.models import BaseModel, Profile
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    # username = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=10, blank=True, null=True, unique=False)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)

    gender = models.CharField(
        choices=GenderChoices,
        max_length=10)

    role = models.CharField(
        choices=RoleChoices, 
        default=RoleChoices.artist, 
        max_length=20
    )

    date_of_birth = models.DateField(null=True)

    # date_joined= models.DateTimeField(auto_now_add=timezone.now())
    # updated_at = models.DateTimeField(auto_now=timezone.now())

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.email}"

class UserProfile(Profile):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)

    class Meta:
        verbose_name = "User Profile"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"