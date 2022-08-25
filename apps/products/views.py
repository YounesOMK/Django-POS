from django.shortcuts import render
from django.views.generic import View
from django.db.models import Count
from django.views.generic.base import TemplateResponseMixin

import plotly.express as px

from .models import Product, Category, Brand
from ..payments.models import Order, OrderItem

class ProductListView(TemplateResponseMixin, View):
    
    template_name = 'products/list.html'
    
    def get(self, request):
        products = Product.objects.filter(quantity__gte=1)
        categories = Category.objects.annotate(num_products=Count('products')).filter(num_products__gte=1)
        brands = Brand.objects.annotate(num_products=Count('products')).filter(num_products__gte=1)        
        return self.render_to_response({
            'products': products,
            'categories': categories,
            'brands': brands,
        })



#htmx

class ProductListByCategory(TemplateResponseMixin, View):
    
    template_name = 'products/fragments/product_list.html'
    
    def get(self, request, cat_id):
        products = Product.objects.filter(category__id=cat_id)
        return self.render_to_response({
            'products': products,
        })
        
        
class ProductSearchView(TemplateResponseMixin, View):
    template_name = 'products/fragments/product_list.html'

    def post(self, request):
        search_text = request.POST.get('search_text')
        products = Product.objects.filter(quantity__gte=1, name__icontains=search_text)
        
        return self.render_to_response({
            'products': products,
        })


class AdminStatsView(TemplateResponseMixin, View):
    template_name = 'products/stats/admin.html'
    
    
    
    def get(self, request):
        orders = Order.objects.all()
                
        fig = px.line(
            x = [o.created.date() for o in orders],
            y = [o.total_profit for o in orders]
        )
        
        chart = fig.to_html()
         
        return self.render_to_response({
            'chart': chart
        })