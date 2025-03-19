from rest_framework import serializers

class SongSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    artist_id = serializers.UUIDField()
    title = serializers.CharField(max_length=255)
    genre = serializers.CharField(max_length=255)
    album_name = serializers.CharField(max_length=255,required=False)
    release_date = serializers.DateField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

