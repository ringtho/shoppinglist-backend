from django.conf import settings
import jwt
from rest_framework import authentication, exceptions
from . import models


class CustomUserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            return None

        try:
            payload = jwt.decode(
                token, settings.JWT_SECRET, algorithms=['HS256'])

        except:
            raise exceptions.AuthenticationFailed("Unauthorized")

        user = models.User.objects.filter(id=payload["id"]).first()

        return (user, None)

        # return super().authenticate(request)
