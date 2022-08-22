from datetime import date
from django.utils import timezone

from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from core.models import TimeStampedModel



class Category(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=30)
    description = models.CharField(_('Description'), max_length=100)
    
    
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

class Brand(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=30)
    description = models.CharField(_('Description'), max_length=100)

    def __str__(self):
        return self.name
    

class Vendor(TimeStampedModel):
    first_name = models.CharField(_('First name'), max_length=30)
    last_name = models.CharField(_('Last name'), max_length=30)
    phone_number = models.CharField(_('Phone number'), max_length=15)
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.get_full_name()
    
    

class Product(TimeStampedModel):
    
    
    sku = models.CharField(_('Stock keeping unit'), max_length=8, unique=True, db_index=True)
    name = models.CharField(_('Name'), max_length=30)
    
    description = models.CharField(_('Description'), max_length=100)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    original_price = models.DecimalField(_('Original Price'), max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(_('Available quantity'), default=1)
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, related_name='products')
    
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    
    def available(self):
        if self.quantity > 0:
            return True
        
        return False
    
    def get_image_url(self):
        return self.image.url
    
    def __str__(self):
        return self.name
    



class Discount(TimeStampedModel):
    
    discount_percent = models.DecimalField(_('Discount percent'), max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discount')
    
    start_date = models.DateField(_('Start date'), default=timezone.now)
    end_date = models.DateField(_('Expiry date'), default=timezone.now)
    
    def expired(self):
        if end_date > date.today():
            return False
        return True
            
                



