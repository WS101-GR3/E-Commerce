from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from USER.models import Basket
from PRODUCT.models import Laptop, PackageBundle
from django.http import HttpResponse

# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())

            # Creates a basket/cart upon a new user registration
            newBasket = Basket(user_id=request.user)
            newBasket.save()



            return redirect('PRODUCT:LAPTOP')
    else:
        form = UserCreationForm()

    return render(request, 'USER/registration.html',{
        'form': form
    })

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('PRODUCT:LAPTOP')
    else:
        form = AuthenticationForm()
    return render(request, 'USER/login.html',{
        'form':form
    })

def logout_user(request):
    logout(request)
    return redirect('HOME')

def getUserCart(request, userID):
    Items = Basket.objects.filter(user_id=userID)

    itemNames = []

    for item in Items:
        a.append(item.basket_item_name)

    return HttpResponse(f'{itemNames}')



def addToCart(request, product_type, userID, product_id):
    if product_type == 'DESKTOP':
        product = PackageBundle.objects.get(unit_id=product_id)
    elif product_id == 'LAPTOP':
        product = Laptop.objects.get(lap_id=product_id)
    
    insertBasket = Basket(
        user_id=userID,
        basket_item_id=product_id,
        basket_item_name=product.name,
        basket_item_price=product.price
    )

    return HttpResponse(f'{product} is ADDED')

