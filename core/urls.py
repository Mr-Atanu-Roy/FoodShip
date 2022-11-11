from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('user/', include('account.urls')),
    path('restaurants/', include('restaurant.urls')),
    path('products/', include('product.urls')),
    path('order/', include('order.urls')),
    path('search/', include('API.urls')),
]