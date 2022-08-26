from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'responsible_cashier', 'created', 'total_profit'
    )
    
    list_filter = (
        'created', 'created', 'updated'
    )
    inlines = [OrderItemInline]