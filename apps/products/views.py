from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from .models import Product, Category

class ProductListView(TemplateResponseMixin, View):
    
    template_name = 'products/list.html'
    
    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()
        return self.render_to_response({
            'products': products,
            'categories': categories,
        })

