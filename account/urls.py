from django.urls import path, include
from .views import *


urlpatterns = [
    path('signin/', signIn, name='signIn'),
    path('login/', logIn, name='logIn'),
    path('logout/', logOut, name='logOut'),
    path('profile/', userProfile, name='userProfile'),
    path('add-address/', addAddress, name='addAddress'),
]