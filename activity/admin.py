from django.contrib import admin
from .models import *

# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Activity._meta.fields]

admin.site.register(Activity, ActivityAdmin)