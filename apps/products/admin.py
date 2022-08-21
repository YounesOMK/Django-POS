from django.contrib import admin

from .models import (
    Product, Category, Brand,
    Vendor, Discount
)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'quantity', 'category',)
    list_filter = ('created', 'category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ('created',)
    search_fields = ('name', 'description',)

@admin.register(Brand)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_filter = ('created',)
    search_fields = ('name', 'description',)
    
@admin.register(Vendor)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    list_filter = ('created',)
    search_fields = ('name', 'phone_number',)

@admin.register(Discount)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('discount_percent', 'product', 'created', 'start_date', 'end_date')
    list_filter = ('created', 'start_date', 'end_date')
    search_fields = ('product',)



