from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin



class CustomUserAdminConfig(UserAdmin):
    ordering = ('-start_date',)
    search_fields = ('email', 'username', 'phone_number',)
    list_filter = ('is_active', 'is_staff', 'is_cashier',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_cashier')
    
    fieldsets = (
        (None, {
            'fields': (
                'email', 'username', 'first_name', 'last_name', 'phone_number'
            ),
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_cashier',
                'groups', 'user_permissions',
            )
        })
    )
    
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_cashier')

        }),
        
    )
    

admin.site.register(CustomUser, CustomUserAdminConfig)