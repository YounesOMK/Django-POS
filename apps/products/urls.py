from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
]