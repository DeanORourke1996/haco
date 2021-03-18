from django.db import models


class MODISEventRecord(models.Model):
    # Response Data
    name = models.CharField(max_length=50)
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

    # String representation of event
    def __str__(self):
        return self.name
