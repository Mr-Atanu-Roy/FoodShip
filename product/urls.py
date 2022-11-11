from django.urls import path, include
from .views import *


urlpatterns = [
    path('', products, name='products'),
    path('view/<productID>', ProductView),
    path('<productType>', viewByProductType),

    path('add-review/', addProductReview, name="addProductReview"),
]