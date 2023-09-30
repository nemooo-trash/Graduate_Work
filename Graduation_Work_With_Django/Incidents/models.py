from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
# Create your models here.
class Incidents(models.Model):
    description = models.CharField(max_length=250)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __str__(self):
        return self.description