# from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .selectors import ArtistSelectors
from .services import ArtistServices 
from .selector2 import SelectorArtists
from .services2 import ServicesArtists
# Create your views here.
selectors_artist = SelectorArtists()
artist_services = ArtistServices()
artist_selectors = ArtistSelectors()
services = ServicesArtists()
class ArtistListAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        # response = artist_selectors.get_artists()
        response = selectors_artist.fetch_artists()
        return response
    
    def post(self, request):        
        # response = artist_services.create_artist(request.data)
        response = services.artist_create(request)
        return response

class ArtistDetailAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request, pk):
        # response = artist_selectors.get_artist_detail(id=pk)
        response = selectors_artist.fetch_artist(id=pk)
        return response
    
    def put(self, request, pk):
        response = artist_services.update_artist(request.data, id=pk)
        return response
    
    def delete(self, request, pk):
        # response = artist_services.delete_artist(id=pk)
        response = services.artist_delete(id=pk)
        return response