from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'payments'

urlpatterns = [
    path('save_orders/', views.OrdersSaveView.as_view(), name='orders_save'),
    path('inovice_generate/<int:order_id>/', views.InoviceGenerateView.as_view(), name='inovice_generate')
]