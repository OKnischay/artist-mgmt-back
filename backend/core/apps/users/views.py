from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import CustomUser
from .serializers import UserSerializer
from .selectors import UserSelectors
from .services import UserServices

user_services = UserServices()
user_selectors = UserSelectors()

class UserListAPIView(APIView):
    permission_classes = []
    authentication_classes = []
   
    def get(self, request):
        response = user_selectors.get_users()
        return response

    def post(self, request):
        response = user_services.create_user(request.data)
        return response


class UserListDetailAPIView(APIView):
    def get(self, request, pk):
        response = user_selectors.get_user_detail(id=pk)
        return response    

    def put(self, request, pk):
            response = user_services.update_user(request.data, id=pk)
            return response

    def delete(self, request, pk):
        response = user_services.delete_user(id=pk)
        return response


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not found")

        if user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")

        return Response({"message": "Login success"})
