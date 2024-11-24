from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

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