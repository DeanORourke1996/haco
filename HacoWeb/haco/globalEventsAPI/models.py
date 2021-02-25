from django.db import models


class AmbeeAPIHookup(models.Model):
    # Response Data
    name = models.CharField(max_length=155)
    lon = models.FloatField()
    lat = models.FloatField()
    confidence = models.CharField(max_length=7)
    frp = models.FloatField()
    day_night = models.CharField(max_length=1)
    detection_time = models.DateTimeField()
