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
    confidence = models.CharField(max_length=50)
    version = models.CharField(max_length=100)
    bright_ti5 = models.FloatField()
    frp = models.FloatField()
    daynight = models.CharField(max_length=1)
    resolution = models.CharField(max_length=5)
    is_user_made = models.CharField(max_length=1)

    # Constructs a GeoJSON dictionary for use with
    # LeafletJS which needs to be serialized
    def serialize(self):
        json_dict = {'type': 'Feature',
                     'geometry': dict(type='Point', coordinates=list([self.lon, self.lat])),
                     'properties': dict(id=self.id, Bright_ti4=self.bright_ti4,
                                        Scan=self.scan, Track=self.track, Acq_date=self.acq_date,
                                        Acq_time=self.acq_time, Satellite=self.satellite,
                                        Confidence=self.confidence, Version=self.version,
                                        Bright_ti5=self.bright_ti5, Frp=self.frp,
                                        Daynight=self.daynight, Resolution=self.resolution)
                     }

        return json_dict

    # Float representation of event by Longitude and Latitude
    def __float__(self):
        return self.lat + self.lon
