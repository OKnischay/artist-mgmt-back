from rest_framework.views import APIView
from .selectors import AlbumSelectors
from rest_framework.permissions import AllowAny
from .services import AlbumServices

albums_selectors = AlbumSelectors()
albums_services = AlbumServices()

class AlbumListAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        response = albums_selectors.get_album_list()
        return response
    

class AlbumDetailAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request, pk):
        response = albums_selectors.get_album_detail(id=pk)
        return response  
    
    def put(self, request, pk):
        response = albums_services.update_album(request.data, id=pk)
        return response

    def delete(self, request, pk):
        response = albums_services.delete_album(id = pk)
        return response
