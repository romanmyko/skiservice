from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'is_superuser', 'password')
    list_filter = ('role', 'is_active', )
    readonly_fields = ('email','role',)
