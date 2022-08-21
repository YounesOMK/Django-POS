from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'payments'

urlpatterns = [
    path('save_orders/', views.OrdersSaveView.as_view(), name='orders_save'),
]