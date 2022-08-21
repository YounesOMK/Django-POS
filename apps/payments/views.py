from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin, View


class OrdersSaveView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'templates/payments/payment.html'
    
    def post(self, request, *args, **kwargs):
        data = { k[-1]: v for (k, v) in request.POST.items() if k.startswith('qt_item') }
        
        print(data)
        return redirect('/')



