from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from product.models import *

# Create your views here.

def restaurants(request):
    user_city = request.session.get('user_city', 'you')

    restaurants = Restaurant.objects.filter(city = user_city)

    if(len(restaurants) == 0):
        user_regionName = request.session.get('user_regionName', 'none')

        if(user_city.lower() != 'none'):
            restaurants = Restaurant.objects.filter(state = user_regionName)


    context = {
        'restaurants' : restaurants,
        'user_city' : user_city
    }
    return render(request, './restaurant/restaurant.html', context)


def viewByRestaurantType(request, restaurantType):
    user_city = request.session.get('user_city', 'you')

    restaurants = Restaurant.objects.filter(restaurant_type = restaurantType)
    restaurants = restaurants.filter(city = user_city)

    if(len(restaurants) == 0):
        user_regionName = request.session.get('user_regionName', 'none')

        if(user_city.lower() != 'none'):
            restaurants = Restaurant.objects.filter(state = user_regionName)
            restaurants = restaurants.filter(restaurant_type = restaurantType)

    context = {
        'user_city' : user_city,
        'restaurant_type' : restaurantType,
        'restaurants' : restaurants
    }
    return render(request, './restaurant/viewByRestaurantType.html', context)

def restaurantView(request, restaurantID):
    restaurant = Restaurant.objects.get(restaurant_id = restaurantID)
    products = Product.objects.filter(restaurant = restaurant)

    context = {
        'restaurant': restaurant,
        'products' : products,
    }
    return render(request, './restaurant/viewRestaurant.html', context)

    
