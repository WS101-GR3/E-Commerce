from django.urls import path
from . import views


urlpatterns = [
    path('list', views.prod_list, name="LIST")
]
