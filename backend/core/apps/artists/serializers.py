# from users.models import CustomUser
from rest_framework import serializers
from apps.songs.serializers import SongSerializer
from apps.users.serializers import UserArtistSerializer

class ArtistSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    stage_name = serializers.CharField()
    address = serializers.CharField()
    gender = serializers.CharField(max_length=10)
    date_of_birth = serializers.DateField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    first_release_year = serializers.IntegerField()
    no_of_albums_released = serializers.IntegerField()
    # song = SongSerializer(many=True, read_only=True)
    user = UserArtistSerializer()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
