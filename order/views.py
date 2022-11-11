from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import random
import os

from instamojo_wrapper import Instamojo

from account.models import *
from account.models import UserAddress
from order.models import *
from product.models import *

api = Instamojo(
    api_key = os.environ.get('API_KEY'), 
    auth_token = os.environ.get('AUTH_TOKEN'), 
    endpoint = os.environ.get('ENDPOINT'))

# Create your views here.

delivery_charge = 55.00

@login_required(login_url='/user/login/')
def placeOrder(request, productID):
    quantity = request.GET.get('q', None)

    if quantity is not None:

        try:
            product = Product.objects.get(product_id = productID)
            price = (product.price)*int(quantity)

            total_price = price + (price*5)/100

            total_price = float(total_price) + delivery_charge

            userProfile = UserProfile.objects.get(email = request.user.email)
            
            try:
                
                address = UserAddress.objects.get(email = request.user.email, address_preference = "primary")
                #making request to instamojo
                response = api.payment_request_create(
                    amount = total_price,
                    purpose = product.product_name,
                    buyer_name = f"{userProfile.first_name} {userProfile.last_name}",
                    email = address.address_email,
                    send_email = True,
                    phone = address.phone,
                    send_sms = True,
                    allow_repeated_payments = False,
                    redirect_url = 'http://127.0.0.1:8000/order/order-success',
                )

                online_payment_url = response['payment_request']['longurl']

                payment_id = ""
                payment_id = payment_id.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(16))
                payment_id = "MOJO" + payment_id
                offline_payment_url = f"http://127.0.0.1:8000/order/order-success?payment_id={payment_id}&payment_status=PayOnDelivery&payment_request_id={response['payment_request']['id']}"

                newOrder, _ = Order.objects.get_or_create(order_id = response['payment_request']['id'], user = request.user.email, address_email = address.address_email, amount = f"{total_price} INR", product = product, phone = address.phone, address = address, quantity = quantity)
                newOrder.save()

                context = {
                    'quantity' : quantity,
                    'product' : product,
                    'address' : address,
                    'product_price' : price,
                    'delivery_charge' : delivery_charge,
                    'total_price' : round(total_price, 2),
                    'online_payment_url' : online_payment_url,
                    'offline_payment_url' : offline_payment_url,
                }
            except:
                return HttpResponse("you dont have any active address. Due to this delivery is not possible")

        except:
            return HttpResponse("invalid product id")


    else:
        context = {}
        return redirect('products')

    return render(request, './order/placeOrder.html', context)


@login_required(login_url='/user/login/')
def orderSuccess(request):
    payment_id = request.GET.get('payment_id', None)

    if payment_id is not None:
        payment_request_id = request.GET.get('payment_request_id', None)
        payment_status = request.GET.get('payment_status', None)

        getOrder = Order.objects.get(order_id = payment_request_id, user = request.user.email)
        if getOrder is not None:
            getOrder.order_status = "ordered"
            if payment_status.lower() != "payondelivery":
                response = api.payment_request_payment_status(payment_request_id, payment_id)
                phone = response['payment_request']['payment']['buyer_phone']
                buyer_name = response['payment_request']['buyer_name']
                amount = response['payment_request']['amount']
                currency = response['payment_request']['payment']['currency']
                purpose = response['payment_request']['purpose']
                payment_status = response['payment_request']['status']
                payment_mode = response['payment_request']['payment']['billing_instrument']

                getOrder.payment_id = payment_id
                getOrder.phone = phone
                getOrder.buyer_name = buyer_name
                getOrder.amount = f"{amount} {currency}"
                getOrder.payment_status = payment_status
                getOrder.payment_mode = payment_mode
                getOrder.save()
                
            else:
                try:
                    userProfile = UserProfile.objects.get(email = request.user.email)

                    buyer_name = f"{userProfile.first_name} {userProfile.last_name}"
                    payment_status = "success"
                    payment_mode = "cash"

                    getOrder.payment_id = payment_id
                    getOrder.buyer_name = buyer_name
                    getOrder.payment_status = payment_status
                    getOrder.payment_mode = payment_mode
                    getOrder.save()
                except:
                    return HttpResponse("invalid request")

        else:
            print("Invalid request")
            return HttpResponse("invalid request")

        context = {
            'buyer_name' : getOrder.buyer_name,
            'product' : getOrder.product,
            'amount' : getOrder.amount,
            'payment_mode' : getOrder.payment_mode,
            'payment_status' : getOrder.payment_status,
            'payment_id' : getOrder.payment_id,
            'order_id' : getOrder.order_id,
            'address' : getOrder.address,
            'payment_date' : getOrder.payment_date
        }

    else:
        context = {}
        return redirect('products')

    return render(request, './order/orderSuccess.html', context)

