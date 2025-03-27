from rest_framework.response import Response
from rest_framework import status
from .models import Album
from .serializers import AlbumSerializer

class AlbumSelectors:
    def get_album_list(self):
        album = Album.objects.all()
        serializers = AlbumSerializer(album, many = True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def get_album_detail(self,id):
        try:
            album = Album.objects.get(id=id) 
            serializer = AlbumSerializer(album) 
            return Response(serializer.data)
        except Album.DoesNotExist:
            return Response({ "Album not found."}, status=status.HTTP_404_NOT_FOUND)