from django.urls import path

from .views import ArtistListAPIView, ArtistDetailAPIView

urlpatterns = [
    path("", ArtistListAPIView.as_view(), name="artist-list"),
    path('<str:pk>/', ArtistDetailAPIView.as_view(), name='artist-detail'),
]