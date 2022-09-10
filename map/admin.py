from django.contrib import admin
from .models import *

# Register your models here.
class PathAdmin(admin.ModelAdmin):
    # list_display = [f.name for f in Path._meta.fields]
    list_display = ['path_length', 'path_coordinate', 'mission']

class SpotAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Spot._meta.fields]

admin.site.register(Path, PathAdmin)
admin.site.register(Spot, SpotAdmin)