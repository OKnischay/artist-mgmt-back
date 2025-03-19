from .serializers import SongSerializer
from .models import Song
from rest_framework.response import Response
from rest_framework import status
from .models import Artist


class SongServices:
    def create_song(self, data):
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            song = self.save_song(serializer.validated_data)
            return Response(SongSerializer(song).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

    def save_song(self, validated_data):
        artist_id = validated_data.pop("artist_id", None)
        try:
            artist = Artist.objects.get(id=artist_id)
        except Artist.DoesNotExist:
            return Response({'artist not found'}, status=status.HTTP_400_BAD_REQUEST)
        return Song.objects.create(artist= artist,**validated_data)
     
    def delete_song(self, id):
        try:
            song = Song.objects.get(id=id)
            song.delete()
            return Response({"detail": "Song deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        
        except Song.DoesNotExist:
            return Response({"detail": "Song not found."}, status=status.HTTP_404_NOT_FOUND)

