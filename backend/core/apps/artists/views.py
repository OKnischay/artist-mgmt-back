from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .selectors import ArtistSelectors
from .services import ArtistServices 
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

artist_services = ArtistServices()
artist_selectors = ArtistSelectors()
class ArtistListAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
       response = artist_selectors.get_artists()
       return response
    
    def post(self, request):        
        response = artist_services.create_artist(request.data)
        return response

class ArtistDetailAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request, pk):
        response = artist_selectors.get_artist_detail(id=pk)
        return response
    
    def put(self, request, pk):
        response = artist_services.update_artist(request.data, id=pk)
        return response
    
    def delete(self, request, pk):
        response = artist_services.delete_artist(id=pk)
        return response