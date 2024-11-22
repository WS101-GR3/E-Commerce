from django.urls import path,include
from . import views

# app_name is used as a placeholder
app_name = 'PRODUCT'

urlpatterns = [

    path('list', views.product_list_page, name="LIST"),
    path('', views.home, name='home'),
    path('system-builder/', views.system_builder, name='system_builder'),
    path('pre_build-pc/', views.pre_build_pc, name='pre_build_pc'),
    path('laptop/', views.laptop, name='laptop'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('system-builder/check_out/', views.check_out, name='check_out'),
    path('addtocart/', views.add_cart, name='addtocart'),
]
