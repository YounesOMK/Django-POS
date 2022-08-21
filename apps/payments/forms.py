from django import forms
from .models import OrderItem, Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            #
        ]