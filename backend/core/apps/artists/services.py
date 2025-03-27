from .serializers import ArtistSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Artist
from apps.users.models import CustomUser
class ArtistServices:
    # def create_artist(self, data):
    #     serializer = ArtistSerializer(data=data)
    #     if serializer.is_valid():
    #         artist = self.save_artist(serializer.validated_data)
    #         return Response(ArtistSerializer(artist).data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def save_artist(self, validated_data):
    #     return Artist.objects.create(**validated_data)


    def create_artist(self, data):
        serializer = ArtistSerializer(data=data)
        
        if serializer.is_valid():
           
            artist = self.save_artist(serializer.validated_data)            
            return Response(ArtistSerializer(artist).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def save_artist(self, validated_data):
     
        user_data = validated_data.pop('user', None)
        user = None

        if user_data:
            user, created = CustomUser.objects.get_or_create(**user_data)
        artist = Artist.objects.create(user=user, **validated_data)
        return artist

    

    def update_artist(self, data ,id):
        try:
            artist = Artist.objects.get(id=id) 
            serializer = ArtistSerializer(artist, data= data)
            if serializer.is_valid():
                updated_artist = self.artist_update(artist, serializer.validated_data)
                return Response(ArtistSerializer(updated_artist).data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Artist.DoesNotExist:
            return Response({ "Artist not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def artist_update(self, instance, validated_data):

        instance.stage_name = validated_data.get('stage_name', instance.stage_name)
        instance.address = validated_data.get('address', instance.address)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.first_release_year = validated_data.get('first_release_year', instance.first_release_year)
        instance.no_of_albums_released = validated_data.get('no_of_albums_released', instance.no_of_albums_released)
        # instance.song = validated_data.get('song', instance.song)

        instance.save()

        return instance
    

    def delete_artist(self, id):
        try:
            artist = Artist.objects.get(id=id)
            artist.delete()
            return Response({"detail": "Artist deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        
        except Artist.DoesNotExist:
            return Response({"detail": "Artist not found."}, status=status.HTTP_404_NOT_FOUND)
    
