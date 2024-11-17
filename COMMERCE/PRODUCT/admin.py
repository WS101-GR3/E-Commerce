from django.contrib import admin
from .models import Product, ProductBundle, Review

# Register your models here.

# Customized View of Product in Admin Panel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id','product_category','product_name','product_price','product_rate')
    order_by = ('-product_rate',)
    search_fields = ('product_category','product_id','product_name')
    list_filter = ('product_category','product_rate','isSoldOut')


@admin.register(ProductBundle)
class ProductBundleAdmin(admin.ModelAdmin):
    list_display = ('bundle_name','motherboard_unit','processor_unit')
    order_by = ('-unit_id')
    search_fields = ('bundle_name',)
    list_filter = ('motherboard_unit','processor_unit','storage_unit','memory_unit')

#Customized View of Product in Admin Panel
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id','product_topic', 'review_context')
    order_by = ('-review_id',)