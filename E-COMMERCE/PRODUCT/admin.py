from django.contrib import admin
from .models import Parts, PackageBundle, Laptop, Review

# Register your models here.

# Customized View of Product in Admin Panel
@admin.register(Parts)
class PartsAdmin(admin.ModelAdmin):
    list_display = ('parts_id','parts_category','parts_name','parts_price','parts_rate')
    order_by = ('-parts_rate',)
    search_fields = ('parts_category','parts_id','parts_name')
    list_filter = ('parts_category','parts_rate','isSoldOut')





@admin.register(PackageBundle)
class PackageBundle(admin.ModelAdmin):
    list_display = ('bundle_name','motherboard_unit','processor_unit')
    order_by = ('-unit_id')
    search_fields = ('bundle_name',)
    list_filter = ('motherboard_unit','processor_unit','storage_unit','memory_unit')


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('lap_id','name','processor')


#Customized View of Product in Admin Panel
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id','product_topic', 'review_context')
    order_by = ('-review_id',)
