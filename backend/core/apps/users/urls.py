from django.urls import path

from .views import LoginAPIView, RegisterAPIView, UserListAPIView, UserListDetailAPIView

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user-list"),
    path("<str:pk>", UserListDetailAPIView.as_view(), name="user-login"),
    path("login/", LoginAPIView.as_view(), name="user-login"),
    path("register/", RegisterAPIView.as_view(), name="user-register"),
]
