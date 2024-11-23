from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import Product

# Create your views here.


# accepts category and filter the overall list to get the selected category
def product_list_page(request, category):
    product_target = Product.objects.filter(category=category)
    return render(request, 'PRODUCT/product_page.html',{
        'products':product_target,
        'category':category
    })

 #HOME SECTION
def home(request):
    return render(request, 'PRODUCT/home.html')


# SYSTEM BUILDER SECTION
def system_builder(request):
    return render(request, 'PRODUCT/system_builder.html')


# PRE-BUILD PC SECTION
def pre_build_pc(request):
    return render(request, 'PRODUCT/pre_build_pc.html')


#LAPTOP SECTION
def laptop(request):
    return render(request, 'PRODUCT/laptop.html')

def check_out(request):
    return render(request, 'PRODUCT/check_out.html')

def add_cart(request):
    return render(request, 'PRODUCT/addtocart.html')

#LOGIN/REGISTER/LOGOUT

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User Does Not Exist")

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('product:home')
        else:
            messages.error(request,"Username or Password Does Not Exist")


    context = {'page':page}
    return render(request,'PRODUCT/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('product:home')

def registerUser(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('product:home')
        else:
            messages.error(request,'An Error Occured during registration')

    return render (request, 'PRODUCT/login_register.html',{'form':form})

