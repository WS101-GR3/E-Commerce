from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def prod_list(request):
    return HttpResponse('PRODUCT PAGE')