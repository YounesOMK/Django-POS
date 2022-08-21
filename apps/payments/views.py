from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin, View


from .models import Order, OrderItem

from ..products.models import Product


class OrdersSaveView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'templates/payments/payment.html'
    
    def post(self, request, *args, **kwargs):
        data = { k[-1]: int(v) for (k, v) in request.POST.items() if k.startswith('qt_item') }
        
        order = Order.objects.create(responsible_cashier=request.user)
        
        for product_id, quantity in data.items():
            product = Product.objects.get(pk=product_id)
            OrderItem.objects.create(
                order=order,
                product= product,
                price= product.price,
                quantity= quantity
            )
        
        order.paid = True
        order.save()
            
        return redirect('/')



