from django.shortcuts import render
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = CustomUser.objects.all()
        serializer = UserSerializer(many=True)
        return Response(serializer.data)