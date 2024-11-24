from django.shortcuts import render
from PRODUCT.models import PackageBundle, Laptop


# Create your views here.


# SYSTEM BUILDER SECTION
def system_builder(request):
    return render(request, 'PRODUCT/system_builder.html')


# PRE-BUILD PC SECTION
def pre_build_pc(request):
    prebuild = PackageBundle.objects.filter(bundle_category='PreBuild')
    return render(request, 'PRODUCT/pre_build_pc.html',{'prebuilds':prebuild})


#LAPTOP SECTION
def laptop(request):
    laptops = Laptop.objects.all()
    return render(request, 'PRODUCT/laptop.html',{'laptops':laptops})

def check_out(request):
    return render(request, 'PRODUCT/check_out.html')

def add_cart(request):
    return render(request, 'PRODUCT/addtocart.html')