from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    #path("test/", views.test_view, name='test'),    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]