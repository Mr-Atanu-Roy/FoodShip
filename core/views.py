from django.shortcuts import render, redirect

from product.models import *
from restaurant.models import *

import json
import requests

# Create your views here.

def home(request):
    #geting user ip
    ip = requests.get('https://api.ipify.org?format=json') 
    ip = json.loads(ip.text)
    ip =ip['ip']
    print(ip)
    # ip = '24.48.0.1'

    #getting user location info 
    r = requests.get(f'http://ip-api.com/json/{ip}')
    user_data = json.loads(r.text)

    user_country = user_data['country']
    user_city = user_data['city']
    user_regionName = user_data['regionName']
    user_zip = user_data['zip']

    request.session['user_country'] = user_country.lower()
    request.session['user_city'] = user_city.lower()
    request.session['user_regionName'] = user_regionName.lower()

    user_city = user_city.lower()
    restaurants = Restaurant.objects.filter(city = user_city)[:4]
    products = Product.objects.all().order_by('-added_on')[:16]

    context = {
        'restaurants' : restaurants,
        'products' : products,
        'user_country' : user_country,
        'user_city' : user_city,
        'user_regionName' : user_regionName,
        'user_pin' : user_zip,
    }

    return render(request, './core/index.html', context)
