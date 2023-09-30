from django.contrib import admin
from .models import *
from leaflet.admin import LeafletGeoAdmin

class IncidentsAdmin(LeafletGeoAdmin):
    pass
    #list_display = ['description', 'location']


admin.site.register(Incidents, IncidentsAdmin)

# Register your models here.
