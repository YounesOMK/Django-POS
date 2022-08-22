from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic import TemplateView
from django.core.exceptions import FieldError
from django.urls import reverse

from .models import Order, OrderItem

from ..products.models import Product


class OrdersSaveView(LoginRequiredMixin, TemplateResponseMixin, View):
    
    def post(self, request, *args, **kwargs):
        data = { k[-1]: int(v) for (k, v) in request.POST.items() if k.startswith('qt_item') }
        
        for product_id, quantity in data.items():
            product = get_object_or_404(Product, id=product_id)
            if product.quantity < quantity or product.quantity == 0 :
                raise FieldError('Quantity field is incorrect.')

        
        order = Order.objects.create(responsible_cashier=request.user)
        for product_id, quantity in data.items():
            product = get_object_or_404(Product, id=product_id)
            
            order_item = OrderItem(
                order=order,
                price= product.price,
                quantity= quantity
            )
            
            order_item.product = product
            order_item.save()
                
        # html = render_to_string('payments/novice.html', {'order': order})
        # response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
        # weasyprint.HTML(string=html).write_pdf(response)
            
        return redirect(reverse('payments:inovice_generate', kwargs={'order_id': order.id}))


class InoviceGenerateView(TemplateResponseMixin, View):
    
    template_name = 'payments/inovice.html'
    
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        print(order.responsible_cashier)

        return self.render_to_response({
            'order': order,
        })



