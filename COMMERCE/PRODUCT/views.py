from django.shortcuts import render
from .models import Product

# Create your views here.


# accepts category and filter the overall list to get the selected category
def product_list_page(request, category):
    product_target = Product.objects.filter(category=category)
    return render(request, 'PRODUCT/product_page.html',{
        'products':product_target,
        'category':category
    })