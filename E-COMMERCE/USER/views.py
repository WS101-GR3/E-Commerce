from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from USER.models import Basket, BasketItems
from django.http import HttpResponse

# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
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
    # pass

    # usersBasket = Basket.objects.get(user_id=userID)
    a = Basket.objects.all() #Returns an array of basket instances
    usersBasketItems = BasketItems.objects.filter(basket=a[0]) #Fetch the items of a basket
    items = usersBasketItems[0] #Contains the basket items of a certain user's basket
    # print(items.basket_laptop.name) 


    #Get One User -> return a list of instances and then get the first instances
    userInstance = (User.objects.all())[0]

    # Get User's Basket -> return one instance since user and basket have one to one RS
    userBasket = Basket.objects.get(user_id=userInstance)
    
    #Get Basket's Items -> return a list of basketItems associated with user's basket
    basketList = BasketItems.objects.filter(basket=userBasket)

    items = []

    for i in range(len(basketList)):
        ko = basketList[i]
        items.append(ko.basket_laptop.name)
    print(items)

    return HttpResponse(a)