from django.db import models
from django.contrib.gis.geos import GEOSGeometry, Point, fromstr
from django.contrib.gis.db import models


# Create your models here.

# cursor.execute("UPDATE maps_location SET geom = ST_SetSRID(ST_MakePoint(lon,lat),4326)")


class Location(models.Model):

    city = models.CharField(max_length= 200)
    state = models.CharField(max_length=2)
    lat = models.FloatField(max_length=50, default=0)
    lon = models.FloatField(max_length=50, default=0)
    geom = models.PointField()
    reference = models.CharField(max_length=200)

    def __str__(self):
        return "{}, {} - {}, {}".format(self.city, self.state, self.lat, self.lon)

class Population(models.Model):
    region = models.CharField(max_length=50)
    subRegion = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    refugeePop = models.IntegerField()

    def __str__(self):
        return "region: {}, sub-region: {}, origin: {}, refugee population: {}".format(self.region, self.subRegion, self.origin, self.refugeePop)
