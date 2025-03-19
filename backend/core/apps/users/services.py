from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser

class UserServices:
    def create_user(self, data):
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = self.save_user(serializer.validated_data)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def save_user(self, validated_data):
        return CustomUser.objects.create(**validated_data)
    
    def update_user(self, data ,id):
        try:
            artist = CustomUser.objects.get(id=id) 
            serializer = UserSerializer(artist, data= data)
            if serializer.is_valid():
                updated_user = self.user_update(artist, serializer.validated_data)
                return Response(UserSerializer(updated_user).data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({ "User not found."}, status=status.HTTP_404_NOT_FOUND)
    
    def user_update(self, instance, validated_data):

        instance.email = validated_data.get('email', instance.email)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.role = validated_data.get('role', instance.role)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        # instance.password = validated_data.get('password', instance.password)
        instance.save()

        return instance


    
    def delete_user(self, id):
        try:
            user = CustomUser.objects.get(id=id)
            user.delete()
            return Response({"detail": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    