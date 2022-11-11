from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from .models import *
from order.models import *

# Create your views here.
def signIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = {}
        #input variables
        context['fname'] = context['lname'] = context['email'] = context['password'] = context['cpassword'] = ""
        #error variables
        context['fnameErr'] = context['lnameErr'] = context['emailErr'] = context['passwordErr'] = context['cpasswordErr'] = ""
        try:
            if request.method == 'POST':
                fname = request.POST['fname']
                lname = request.POST['lname']
                email = request.POST['email']
                password = request.POST['password']
                cpassword = request.POST['cpassword']
                context['fname'] = fname
                context['lname'] = lname
                context['email'] = email
                context['password'] = password
                context['cpassword'] = cpassword
                if fname != "" and lname != "" and email != "" and password != "" and cpassword != "":
                    if password == cpassword:
                        if User.objects.filter(email = email).exists():
                            context['emailErr'] = "user already exists"
                            return redirect('signin', context)
                        else:
                            username = email
                            newUser = User.objects.create_user(first_name = fname, last_name = lname, email = email, password = password, username = username)
                            newUser.save()

                            newUserProfile = UserProfile(email = username)
                            newUserProfile.first_name = fname
                            newUserProfile.last_name = lname
                            newUserProfile.save()

                            auth.login(request, newUser)

                            print("registered successfull")

                            return redirect('/user/profile')
                    else:
                        context['passwordErr'] = context['cpasswordErr'] = "passwords do not match"
                        return redirect('signin', context)
                else:
                    context['fnameErr'] = "all fields are required"
                    return redirect('signin', context)
        except:
            pass 
    
    return render(request, 'account/signin.html', context)

def logIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = {}
        #input variables
        context['email'] = context['password'] = ""
        #error variables
        context['emailErr'] = context['passwordErr'] = ""
        try:
            if request.method == "POST":
                email = request.POST['email']
                password = request.POST['password']
                context['email'] = email
                context['password'] = password
                if email != "" and password != "":
                    username = email
                    user = auth.authenticate(username = username, password = password)
                    print(user)
                    if user is not None:
                        auth.login(request, user)
                        print("login successfull")

                        if request.GET.get('next') != None:
                            return redirect(request.GET['next'])
                        
                        return redirect('home')
                    else:
                        context['emailErr'] = context['passwordErr'] = "invalid credentials"
                        return redirect('login', context)
                        
                else:
                    context['emailErr'] = context['passwordErr'] = "email and password are required"
                    return redirect('login', context)
        except:
            pass

    return render(request, 'account/login.html', context)

@login_required(login_url='/user/login/')
def logOut(request):
    auth.logout(request)
    return redirect('home')


@login_required(login_url='/user/login/')
def userProfile(request):
    context = {
        'address_email' : request.user.email
    }

    user_city = request.session.get('user_city', '')
    user_country = request.session.get('user_country', '')
    user_zip = request.session.get('user_zip', '')

    userProfile = UserProfile.objects.get(email = request.user.email)

    context['fname'] = userProfile.first_name
    context['lname'] = userProfile.last_name
    context['phone'] = userProfile.phone
    context['city'] = userProfile.city
    context['country'] = userProfile.country
    context['gender'] = userProfile.gender
    context['pin'] = userProfile.pin

    if userProfile.phone == None :
        context['phone'] = ""
    if userProfile.country == None :
        context['country'] = user_country
    if userProfile.city == None :
        context['city'] = user_city
    if userProfile.pin == None:
        context['pin'] = ""

    try:
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            phone = request.POST['phone']
            country = request.POST['country']
            city = request.POST['city']
            pin = request.POST['pin']
            gender = request.POST['gender']

            context['fname'] = fname
            context['lname'] = lname
            context['phone'] = phone
            context['city'] = city
            context['country'] = country
            context['gender'] = gender
            context['pin'] = pin

            print(gender)

            userProfile.first_name = fname
            userProfile.last_name = lname
            userProfile.phone = phone
            userProfile.city = city
            userProfile.country = country
            userProfile.pin = pin
            userProfile.gender = gender
            userProfile.save()
            print("profile saved")
    except:
        pass
    

    userAddress = UserAddress.objects.filter(email = request.user.email)
    context['user_address'] = userAddress
    context['user_address_no'] = len(userAddress)

    userOrders = Order.objects.filter(user = request.user.email)
    context['user_orders'] = userOrders

    return render(request, 'account/profile.html', context)


@login_required(login_url='/user/login/')
def addAddress(request):
    userProfile = UserProfile.objects.get(email = request.user.email)
    context = {
        'address_email' : request.user.email,
        'address_phone' : userProfile.phone,
    }
    try:
        if request.method == 'POST':
            email = request.POST['email']
            phone = request.POST['phone']
            state = request.POST['state']
            city = request.POST['city']
            street = request.POST['street']
            landmark = request.POST['landmark']
            pin = request.POST['pin']
            address_type = request.POST['address_type']

            context['address_phone'] = phone
            context['address_city'] = city
            context['address_state'] = state
            context['address_landmark'] = landmark
            context['address_street'] = street
            context['address_pin'] = pin

            if phone == "":
                phone = userProfile.phone
            if email == "":
                email = request.user.email

            createdAddress = UserAddress.objects.filter(email = request.user.email, address_preference = "primary")
            if createdAddress is not None:
                address_preference = "secondary"
            else:
                address_preference = "primary"

            newAddress = UserAddress(email = request.user.email)
            newAddress.address_email = email
            newAddress.phone = phone
            newAddress.landmark = landmark
            newAddress.city = city
            newAddress.state = state
            newAddress.pin = pin
            newAddress.street = street
            newAddress.address_type = address_type
            newAddress.address_preference = address_preference

            newAddress.save()

            print("address saved")
            return redirect('/user/profile', context)
    except:
        pass

    return render(request, 'account/addAddress.html', context)



