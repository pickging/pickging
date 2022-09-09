from django.contrib import admin

from .models import *


# Register your models here.
class GuildAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Guild._meta.fields]
    search_fields = ['guild_name']
    
    
admin.site.register(Guild, GuildAdmin)