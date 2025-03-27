import uuid
from django.db import connection
from django.utils import timezone
from .serializers import ArtistSerializer
from rest_framework.response import Response
from rest_framework import status
# from .models import Artist
# from django.contrib.auth.hashers import make_password

class ServicesArtists:
    @staticmethod
    def artist_create(request, user_id):
        data = request.data
        try:
            id=str(uuid.uuid4())
            stage_name = data.get('stage_name')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            address = data.get('address')
            gender = data.get('gender')
            first_release_year = data.get('first_release_year')
            no_of_albums_released = data.get('no_of_albums_released')
            created_at = timezone.now()
            updated_at = timezone.now()

            with connection.cursor() as c:
                c.execute("""INSERT INTO artists_artist 
                          (id, stage_name, first_name, last_name, address, gender,
                          first_release_year, no_of_albums_released, created_at, updated_at, user_id) VALUES
                          (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING *;
                          """,
                          [
                            id, stage_name, first_name, last_name, address, gender, first_release_year,
                            no_of_albums_released, created_at, updated_at, user_id
                          ],
                          )
                result = c.fetchone()
                columns = [col[0] for col in c.description]

                user_dicts = dict(zip(columns, result))
                serializer = ArtistSerializer(user_dicts)

                return Response(serializer.data,status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({"error":str(e),"message": "Error while creating user"}, status=status.HTTP_400_BAD_REQUEST)
        

    @staticmethod
    def artist_delete(id):
        try:
            with connection.cursor() as c:
                c.execute("DELETE FROM artists_artist WHERE id = %s RETURNING TRUE;",[id])
                result = c.fetchone()

            if not result:
                return Response({"mesage": "Arist not found"}, status=status.HTTP_404_NOT_FOUND)
            
            return Response({"message": "Successfully delete artist"}, status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            return Response({"error":str(e),"message": "Failed to delete artist"}, status=status.HTTP_400_BAD_REQUEST) 
        

    @staticmethod
    def artist_update(request, user_id):
        data = request.data
        try:
            with connection.cursor() as c:
                c.execute("SELECT * FROM artists_artist WHERE user_id = %s;",[user_id])
                result = c.fetchone()

                if not result:
                    return Response({"message: Artist not found"}, status= status.HTTP_404_NOT_FOUND)
                
                columns = [col[0] for col in c.description]

                before_edit = dict(zip(columns, result))

                stage_name = data.get('stage_name', before_edit.get('stage_name'))
                address = data.get('address', before_edit.get('address'))
                no_of_albums_released = data.get('no_of_albums_released', before_edit.get('no_of_albums_released'))
                updated_at = timezone.now()

                c.execute("""UPDATE artists_artist SET
                          stage_name = %s,
                          address = %s,
                          no_of_albums_released = %s,
                          updated_at = %s
                          WHERE user_id = %s 
                          RETURNING *;
                           """,  
                           [stage_name,address,no_of_albums_released,updated_at,user_id])
                           
                
                after_edit = c.fetchone()
                columns = [col[0] for col in c.description]

                user_dict = dict(zip(columns, after_edit))
                serializer = ArtistSerializer(user_dict)

                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"error": str(e),"message": "Error while editing "},status=status.HTTP_400_BAD_REQUEST)





























        