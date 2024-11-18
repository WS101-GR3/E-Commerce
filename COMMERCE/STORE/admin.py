from django.contrib import admin
from .models import Store


# Register your models here.


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_id','store_name')
    list_filter = ('store_name',)