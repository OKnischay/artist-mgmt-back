from rest_framework import serializers

class ArtistAlbumSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only = True)
    stage_name = serializers.CharField()
    gender = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    

class AlbumSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only = True)
    album_name = serializers.CharField()
    total_tracks = serializers.IntegerField()
    release_date = serializers.DateField()
    # stage_name = serializers.CharField()
    artist = ArtistAlbumSerializer()