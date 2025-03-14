from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(unique=True, read_only=True)
    email = serializers.EmailField(unique= True, read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)