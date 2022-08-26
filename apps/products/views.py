from django.shortcuts import render
from django.views.generic import View
from django.db.models import Count
from django.views.generic.base import TemplateResponseMixin
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
import plotly.express as px
import pandas as pd


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


class StatsView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'products/stats/stats.html'
    
    
    
    def get(self, request):
        config = {'displayModeBar': False}
        
        orders = Order.objects.all()
        
        nb_of_sales_per_qt_qs = Category.objects.prefetch_related('products').annotate(
            number_of_sales=Sum('products__order_items__quantity')
        )
        
        nb_of_sales_per_qt_df = pd.DataFrame(list(nb_of_sales_per_qt_qs.values('name', 'number_of_sales')))
                
        revenues_per_date_df = pd.DataFrame({
            'date': [o.created.date() for o in orders],
            'profit': [o.total_profit for o in orders],
        })
        
        # example to test chart
        # revenues_per_date_df = pd.DataFrame({
        #     'date': [
        #         '2022-08-22',
        #         '2022-08-23',
        #         '2022-08-24',
        #         '2022-08-25',
        #         '2022-08-26',
        #         '2022-08-27',
        #         '2022-08-28',
        #         '2022-08-29'  
        #     ],
        #     'profit': [8541, 7514, 9850, 6352, 9851, 5362, 4041, 4520]
        # })
        
        
        revenues_per_date_df = revenues_per_date_df.groupby('date', as_index=False).agg(
            {'profit': 'sum'}
        )
        
        rev_per_date_fig = px.line(revenues_per_date_df,
            x = 'date',
            y = 'profit',
            title="Revenues per date.",
        )

        nb_of_sales_per_qt_fig = px.pie(nb_of_sales_per_qt_df,
            values = 'number_of_sales',
            names = 'name',
            title = 'Number of sales per category.'                           
        )

        
        revenues_per_date_chart = rev_per_date_fig.to_html(config=config)
        nb_of_sales_per_qt_chart = nb_of_sales_per_qt_fig.to_html(config=config)
        
        return self.render_to_response({
            'revenues_per_date_chart': revenues_per_date_chart,
            'nb_of_sales_per_qt_chart': nb_of_sales_per_qt_chart,
        })