from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'paid', 'responsible_cashier',
    )
    
    list_filter = (
        'paid', 'created', 'created', 'updated'
    )
    inlines = [OrderItemInline]