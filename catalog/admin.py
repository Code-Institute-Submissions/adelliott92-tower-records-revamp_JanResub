from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import storeCategory, storeProduct

@admin.register(storeCategory)
class storeAdmin(admin.ModelAdmin):
    display_list = ['name', 'slug']
    fields_prepopulated = {'slug': ('categoryName', )}

@admin.register(storeProduct)
class productAdmin(admin.ModelAdmin):
    display_list = ['product_title', 'creator_id', 'slug', 'product_price', 'product_in_stock', 'created_on', 'updated_on']
    filter_list = ['product_in_stock', 'product_is_active']
    editable_list = ['product_price', 'product_in_stock']
    fields_prepopulated = {'slug': ('product_title', )}