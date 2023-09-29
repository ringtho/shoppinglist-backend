from django.conf import settings
import jwt
from rest_framework import authentication, exceptions
from . import models


class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # token = request.COOKIES.get("jwt")
        # token = request.META.get('HTTP_AUTHORIZATION')

        # Extract the JWT from the Authorization header
        token = request.COOKIES.get(
            "jwt") or request.META.get('HTTP_AUTHORIZATION')

        print('get my token', token)

        if not token:
            return None

        try:
            payload = jwt.decode(
                token, settings.JWT_SECRET, algorithms=['HS256'])
            print('get my payload', payload)

        except:
            raise exceptions.AuthenticationFailed("Unauthorized")

        user = models.User.objects.filter(id=payload["id"]).first()
        print('get my user', user)

        return (user, None)

        # return super().authenticate(request)
