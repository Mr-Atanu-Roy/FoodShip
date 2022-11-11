from django.shortcuts import render

from django.http import JsonResponse

from product.models import *
from restaurant.models import *

# Create your views here.
def search(request):
    query = request.GET.get('query')
    payload = []
    if query:
        #icontains lookup is used to get records that contains a specified value. its case insensitive
        products = Product.objects.filter(product_name__icontains = query) 
        restaurants = Restaurant.objects.filter(restaurant_name__icontains = query) 
        for p in products:
            payload.append({
                'name' : p.product_name,
                'url' : f'/products/view/{p.product_id}'
            })
        for r in restaurants:
            payload.append({
                'name' : r.restaurant_name,
                'url' : f'/restaurants/view/{r.restaurant_id}'
            })

    return JsonResponse({
        'status' : True,
        'payload' : payload
    })