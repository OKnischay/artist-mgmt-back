import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from users.models import CustomUser

class JWTAuthetication(authentication.BaseAuthentication):
     def authenticate(self, request):
         token = request.headers.get('Authorization',None)
         if not token:
             return None
         try:
             payload= jwt.decode(token, settings.SECERT_KEY, algorithms=["HS256"])
             user = CustomUser.objects.get(id=payload['user_id'])
         except (jwt.ExpiredSignatureError, jwt.DecodeError, CustomUser.DoesNotExist):
             raise exceptions.AuthenticationFailed('Invalid token or user')
    
         return (user,None)

