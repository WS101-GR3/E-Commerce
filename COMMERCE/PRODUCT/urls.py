from django.urls import path
from . import views

# app_name is used as a placeholder
app_name = 'PRODUCT'

urlpatterns = [
    path('list', views.product_list_page, name="LIST")
]
