from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import *
from restaurant.models import *

# Create your views here.
def products(request):
    user_city = request.session.get('user_city', 'you')

    # restaurants = Restaurant.objects.filter(city = user_city)
    # print(restaurants)
    # products = Product.objects.filter(restaurant = restaurants) 
    products = Product.objects.all()
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

    product_reviews = ProductReview.objects.filter(product = product.product_name).order_by('-added_on')

    context = {
        # 'review_error' : "",

        "product_id" : productID,

        'product' : product,
        'similar_products_mealType' : similarProductMealType,
        'similar_products_foodType' : similarProductFoodType[:16],

        'len_similar_products_mealType' : len(similarProductMealType),
        'len_similar_products_foodType' : len(similarProductFoodType),

        'product_reviews' : product_reviews,
        'len_product_reviews' : len(product_reviews),
    }

    return render(request, './product/viewProduct.html', context)


@login_required(login_url='/user/login/')
def addProductReview(request):
    context = {
        'review_error' : "",
    }
    product_id = request.GET.get('product_id')
    if product_id is not None:
        try:
            product = Product.objects.get(product_id = product_id)
            print(product)
            if request.method == "POST":
                review = request.POST['review']
                print(review)
                if review == "":
                    context['review_error'] = "please write something"
                    return redirect(f'/products/view/{product_id}', context)
                else:
                    newReview = ProductReview(product = product.product_name, user = request.user.email)
                    print(product.product_name)
                    print(request.user.email)
                    print("1")
                    newReview.review = review
                    print("2")
                    newReview.username = f"{request.user.first_name} {request.user.last_name}"
                    print("3")
                    newReview.save()
                    print("review saved successfully")

                    context['review_error'] = ""
                    # return redirect(f'/products/view/{product_id}', context)

        except:
            pass

    return redirect(f'/products/view/{product_id}', context)
    
