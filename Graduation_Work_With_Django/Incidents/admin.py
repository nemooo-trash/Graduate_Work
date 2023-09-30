from django.contrib import admin
from .models import *

class IncidentsAdmin(admin.ModelAdmin):
    list_display = ['description', 'location']


admin.site.register(Incidents, IncidentsAdmin)

# Register your models here.
