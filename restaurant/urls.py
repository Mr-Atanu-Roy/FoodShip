from django.urls import path, include

from .views import *

urlpatterns = [
    path('', restaurants, name='restaurants'),
    path('view/<restaurantID>', restaurantView),
    path('<restaurantType>', viewByRestaurantType),
]
