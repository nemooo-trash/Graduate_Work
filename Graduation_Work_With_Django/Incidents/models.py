from django.db import models

# Create your models here.
class Incidents(models.Model):
    description = models.CharField(max_length=250)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.description