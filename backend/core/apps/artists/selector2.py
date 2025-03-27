from django.db import connection
from rest_framework import status

from rest_framework.response import Response
from apps.artists.serializers import ArtistSerializer
from apps.users.serializers import UserArtistSerializer


class SelectorArtists:
    @staticmethod
    def fetch_artists():
        try:
            with connection.cursor() as c:
                c.execute("""SELECT * FROM artists_artist""")
                results = c.fetchall()

                columns = []
                for col in c.description:   
                    columns.append(col[0]) 

                artist_dicts = [dict(zip(columns, row)) for row in results]

                for artist in artist_dicts:
                    user_id = artist['user_id']
                    c.execute("""SELECT * FROM users_customuser WHERE id=%s""",[user_id])
                    result = c.fetchone()
                    columns = []
                    for col in c.description:   
                        columns.append(col[0]) 

                    user_dict = dict(zip(columns, result))
                    serializer = UserArtistSerializer(user_dict)
                    user = serializer.data
                    artist['user'] = user

                serializer = ArtistSerializer(artist_dicts, many=True)
                artists = serializer.data
            
                return Response(artists, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"errors":str(e),"message":"Error again!!!!!"},status=status.HTTP_400_BAD_REQUEST)
    

    # @staticmethod
    # def fetch_artist(id):
    #     try:
    #         with connection.cursor() as c:
    #             c.execute("SELECT * FROM artists_artist WHERE id = %s ", [id])
    #             result = c.fetchone()
    #             columns = []
    #             for col in c.description:
    #                 columns.append(col[0])
                
    #             artist_dict= dict(zip(columns, result))
                
    #             user_id = artist['user_id']
    #             c.execute("SELECT * FROM users_customuser WHERE id = %s", [user_id])
    #             result = c.fetchone()
    #             columns = []

    #             for col in 
    #             serializer =ArtistSerializer(artist_dict)
    #             artist =serializer.data

    #             return Response(artist, status=status.HTTP_200_OK)

    #     except Exception as e:
    #         return Response({"errors":"Something went wrong terribly"}, status=status.HTTP_400_BAD_REQUEST)
        
    @staticmethod
    def fetch_artist(id):
        try:
            with connection.cursor() as c:
                # Fetch artist details
                c.execute("SELECT * FROM artists_artist WHERE id = %s", [id])
                result = c.fetchone()
                if not result:
                    return Response({"error": "Artist not found"}, status=status.HTTP_404_NOT_FOUND)
                
                
                columns = [col[0] for col in c.description]
                artist_dict = dict(zip(columns, result))
                
              
                user_id = artist_dict['user_id']
                c.execute("SELECT * FROM users_customuser WHERE id = %s", [user_id])
                user_result = c.fetchone()
                
                if user_result:
                    user_columns = [col[0] for col in c.description]
                    user_dict = dict(zip(user_columns, user_result))
                    artist_dict['user'] = user_dict  
                
                
                serializer = ArtistSerializer(artist_dict)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"errors": "Something went terribly wrong", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)
