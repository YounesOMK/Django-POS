from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def decrease_quantity(sender, instance, **kwargs):
    product = instance.product
    ordered_quantity = instance.quantity
    product.quantity -= ordered_quantity
    product.save()