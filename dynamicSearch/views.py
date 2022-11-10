from django.shortcuts import render

from django.http import JsonResponse

from product.models import *

# Create your views here.
def search(request):
    query = request.GET.get('query')
    payload = []
    if query:
        products = Product.objects.filter(product_name__icontains = query) #icontains lookup is used to get records that contains a specified value. its case insensitive
        for product in products:
            payload.append({
                'product_id' : product.product_id,
                'product_name' : product.product_name,
            })

    return JsonResponse({
        'status' : True,
        'payload' : payload
    })