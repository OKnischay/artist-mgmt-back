from django.urls import path

from .views import AlbumListAPIView , AlbumDetailAPIView

urlpatterns = [
    path("", AlbumListAPIView.as_view(), name="album-list"),
    path('<str:pk>/', AlbumDetailAPIView.as_view(), name='artist-detail'),
]