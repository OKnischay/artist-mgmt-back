from rest_framework.response import Response
from rest_framework import status
from .models import Artist
from .serializers import ArtistSerializer

class ArtistSelectors:
    def get_artists(self):
        artists = Artist.objects.all()
        serializers = ArtistSerializer(artists, many= True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    

    def get_artist_detail(self,id):
        try:
            artist = Artist.objects.get(id=id) 
            serializer = ArtistSerializer(artist) 
            return Response(serializer.data)
        except Artist.DoesNotExist:
            return Response({ "Artist not found."}, status=status.HTTP_404_NOT_FOUND)
        


        
