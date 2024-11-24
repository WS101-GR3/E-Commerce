from django.urls import path 
from . import views

app_name = 'PRODUCT'

urlpatterns = [
    path('System_Builder/', views.system_builder, name="BUILD"),
    path('laptop/', views.laptop, name="LAPTOP"),
    path('pre_build/', views.pre_build_pc, name="PRE-BUILD")
]
