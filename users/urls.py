from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterAPI.as_view(), name='register'),
    path("login/", views.LoginAPI.as_view(), name='login'),
    path("me/", views.UserAPI.as_view(), name='me'),
    path("logout/", views.LogoutAPI.as_view(), name='logout')
]

'''

    {
        "first_name": "Jordin",
        "last_name": "Sparks",
        "email": "j_sparks@yahoo.com",
        "password": "hello_me123"
    }

    {
        "item": "Spaghetti",
        "quantity": 2,
        "notes": "to prepare lunch this Sunday",
        "is_completed": false
    }

'''
