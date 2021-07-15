from django.contrib.gis.db import models


class Event(models.Model):
    # ID Column
    id = models.AutoField(primary_key=True)
    # Response Data
    lat = models.FloatField()
    lon = models.FloatField()
    bright_ti4 = models.FloatField()
    scan = models.FloatField()
    track = models.FloatField()
    acq_date = models.CharField(max_length=255)
    acq_time = models.CharField(max_length=255)
    satellite = models.CharField(max_length=100)
    confidence = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    bright_ti5 = models.FloatField()
    frp = models.FloatField()
    daynight = models.CharField(max_length=1)
    resolution = models.CharField(max_length=5)

    # Float representation of event by Longitude and Latitude
    def __float__(self):
        return self.lat + self.lon

