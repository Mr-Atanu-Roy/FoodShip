from django.urls import path, include
from .views import *

urlpatterns = [
    path('<productID>/', placeOrder, name='placeOrder'),
    path('order-success', orderSuccess, name='orderSuccess'),
]