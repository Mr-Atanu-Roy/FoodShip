from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from restaurant.models import *

# Create your views here.
def products(request):
    user_city = request.session.get('user_city', 'you')

    # restaurants = Restaurant.objects.filter(city = user_city)
    # print(restaurants)
    # products = Product.objects.filter(restaurant = restaurants) 
    products = Product.objects.all()
    # print(products)
    context = {
        'products' : products,
    }
    return render(request, './product/product.html', context)

def viewByProductType(request, productType):
    user_city = request.session.get('user_city', 'you')

    # restaurants = Restaurant.objects.filter(city = user_city)
    # print(restaurants)
    # products = Product.objects.filter(restaurant = restaurants) 
    # products = products.filter(meal_type = productType)
    products = Product.objects.filter(meal_type = productType)

    context = {
        'product_type' : productType,
        'products' : products
    }

    return render(request, './product/viewByProductType.html', context)

def ProductView(request, productID):
    user_city = request.session.get('user_city', 'you')

    product = Product.objects.get(product_id = productID)

    similarProductMealType = Product.objects.filter(meal_type = product.meal_type)
    similarProductMealType = similarProductMealType.exclude(product_id = productID)

    similarProductFoodType = Product.objects.filter(food_type = product.food_type)
    similarProductFoodType = similarProductFoodType.exclude(product_id = productID)

    context = {
        'product' : product,
        'similar_products_mealType' : similarProductMealType,
        'similar_products_foodType' : similarProductFoodType[:16],

        'len_similar_products_mealType' : len(similarProductMealType),
        'len_similar_products_foodType' : len(similarProductFoodType),
    }

    return render(request, './product/viewProduct.html', context)


    
