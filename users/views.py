# from django.shortcuts import render
from rest_framework import views, response, exceptions, permissions, status
from . import serializer as user_serializer, services as service, authentication
# Create your views here.


class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        serializer.instance = service.create_user(user=data)

        return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class LoginAPI(views.APIView):
    """
    This class handles the login functionality of a User and returns an 
    access token if successful or raises 401 error otherwise
    """

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = service.user_selector(email)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid credentials")

        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid credentials")

        token = service.generate_token(user_id=user.id)

        resp = response.Response()

        resp.set_cookie(key="jwt", value=token, httponly=True)
        resp.status_code = 200
        resp.status_text = "Ok"

        return resp


class UserAPI(views.APIView):
    """
    This endpoint is only used for 
    authenticated users
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPI(views.APIView):
    """
    This endpoint logs out the current
    authenticated user and deletes their cookie
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {
            "message": "Logout successful"
        }

        return resp
