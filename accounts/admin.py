from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import your custom user model

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'gender')  # Add 'gender' to list_display

# Register your custom user model
admin.site.register(CustomUser, CustomUserAdmin)
