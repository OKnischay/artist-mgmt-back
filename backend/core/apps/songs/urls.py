from django.urls import path
from .views import SongListAPIView, SongDetailAPIView

urlpatterns = [
    path('',SongListAPIView.as_view(), name='song-list'),
    path('<str:pk>',SongDetailAPIView.as_view(), name='song-detail')
]
