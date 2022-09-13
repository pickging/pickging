from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'guild', 'region', 'point', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at', 'password']

admin.site.register(User, UserAdmin)
