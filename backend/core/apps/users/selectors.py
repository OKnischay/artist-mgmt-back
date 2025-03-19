from apps.users.models import CustomUser
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

class UserSelectors:
    def get_users(self):
        user = CustomUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    

    def get_user_detail(self,id):
        try:
            user = CustomUser.objects.get(id=id) 
            serializer = UserSerializer(user) 
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({ "User not found."}, status=status.HTTP_404_NOT_FOUND)
        

