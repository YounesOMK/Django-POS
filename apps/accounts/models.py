from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext as _


from core.models import TimeStampedModel



class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email, password, **other_fields):
        if not email:
            raise ValueError(_('You should specify an email address.'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.password = make_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_cashier', False)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff set to True.'))
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser set to True.'))
        
        if other_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active set to True.'))
        
        if other_fields.get('is_cashier') is not False:
            raise ValueError(_('Superuser must have is_cashier set to False.'))
        
        return self.create_user(username, email, password, **other_fields)
        

class CustomUser(PermissionsMixin, TimeStampedModel, AbstractBaseUser):
    username = models.CharField(_('username'), max_length=150, unique=True)
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    phone_number = models.CharField(_('phone number'), max_length=15)
    
    start_date = models.CharField(_('start date'), max_length=150, default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']
    
    objects = CustomUserManager()
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name_shortcut(self):
        return f'{self.first_name[0]}{self.last_name[0]}'

    
    def __str__(self):
        return self.username