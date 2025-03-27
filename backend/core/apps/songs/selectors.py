from rest_framework import status
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer

class SongSelector:
    def get_song(self):
        songs = Song.objects.all()
        serializers =  SongSerializer(songs, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    

    def get_song_detail(self,id):
        try:
            artist = Song.objects.get(id=id) 
            serializer = SongSerializer(artist) 
            return Response(serializer.data)
        except Song.DoesNotExist:
            return Response({ "Song not found."}, status=status.HTTP_404_NOT_FOUND)




