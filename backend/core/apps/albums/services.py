from rest_framework import status
from rest_framework.response import Response

from .models import  Album
# from .serializers import AlbumSerializer, ArtistAlbumSerializer


class AlbumServices:

    def create_album():
        pass


    def delete_album(self, id):
        try:
            album = Album.objects.get(id = id)
            album.delete()
            return Response(
                    {"detail": "Album deleted successfully."},
                    status=status.HTTP_204_NO_CONTENT,
                )

        except Album.DoesNotExist:
            return Response(
                {"detail": "Album not found."}, status=status.HTTP_404_NOT_FOUND
            )
