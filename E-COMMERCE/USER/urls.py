from django.urls import path
from . import views

app_name = 'USER'

urlpatterns = [
    path('login', views.login_user, name="LOGIN"),
    path('register/', views.register_user, name="REGISTER"),
    path('logout/', views.logout_user, name="LOGOUT"),
    path('cart/<str:userID>', views.getUserCart, name="FETCHCART"),
    path('cart/add/<str:product_type>/<str:userID>/<str:product_id>', views.addToCart, name="ADD_TO_CART")
]
