from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    """Админка модели пользователя"""
    list_display = ['id', 'email', 'first_name', 'last_name', 'date_joined','is_active', 'is_staff', 'is_superuser']
    list_display_links = ['id', 'email']
    list_editable = ['is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'first_name', 'last_name']

admin.site.register(User, UserAdmin)
