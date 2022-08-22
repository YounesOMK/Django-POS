from django.db import models
from django.utils.translation import gettext as _

from apps.products.models import Product
from apps.accounts.models import CustomUser
from core.models import TimeStampedModel



class Order(TimeStampedModel):
    class Meta:
        ordering = ('-created',)
        
    #paid = models.BooleanField(_('Paid'), default=False)
    responsible_cashier = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders', limit_choices_to={'is_cashier': True}, verbose_name=_('Responsible Cashier'))
    
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all() )
    
    def __str__(self):
        return str(self.id) + ': ' + str(self.get_total_cost()) + ' MAD'
    
    

class OrderItem(TimeStampedModel):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(_('Quantity'), default=1)
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
