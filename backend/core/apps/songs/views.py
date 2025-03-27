from django.shortcuts import render
from rest_framework.views import APIView
from .selectors import SongSelector
from .services import SongServices
# Create your views here.

song_services = SongServices()
song_selectors = SongSelector()
class SongListAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self, request):
        response = song_selectors.get_song()
        return response
    
    def post(self, request):
        response = song_services.create_song(request.data)
        return response
    
class SongDetailAPIView(APIView):
    permission_classes = []
    authentication_classes = []    

    def get(self, request, pk):
        response = song_selectors.get_song_detail(id=pk)
        return response  

