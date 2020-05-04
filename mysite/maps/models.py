from django.db import models, connection
from django.contrib.gis.geos import GEOSGeometry, Point, fromstr
from django.contrib.gis.db import models


cursor = connection.cursor()

# Create your models here.
# class Helpers:
    # def update(self):
        # cursor.execute("UPDATE maps_location SET geom = ST_SetSRID(ST_MakePoint(lon,lat),4326)")

        # # geo_jsons = json.dumps(cursor.execute("SELECT FROM public.maps_location ST_AsGeoJSON(geom)"))
        # cursor.execute("SELECT json_build_object( \
        #     'type', 'FeatureCollection',\
        #     'crs',  json_build_object( \
        #         'type',      'name', \
        #         'properties', json_build_object( \
        #             'name', 'EPSG:4326' \
        #         ) \
        #     ), \
        #     'features', json_agg( \
        #         json_build_object(\
        #             'type',       'Feature',\
        #             'id',         id, \
        #             'geometry',   ST_AsGeoJSON(geom)::json,\
        #             'properties', json_build_object(\
        #                 'city', city,\
        #                 'state', state\
        #             )\
        #         )\
        #     )\
        # )\
        # FROM maps_location")
        # records = cursor.fetchall()
        # for row in records:
        #     print(row)

class Location(models.Model):

    city = models.CharField(max_length= 200)
    state = models.CharField(max_length=2)
    lat = models.FloatField(max_length=50, default=0)
    lon = models.FloatField(max_length=50, default=0)
    geom = models.PointField()

    def __str__(self):
        return "{}, {} - {}, {}".format(self.city, self.state, self.lat, self.lon)


#DONT FORGET TO CLOSE CONNECTION- I BOOKMARKED THAT ARTICLE

#
# class Question(models.Model):
#     question_text = models.CharField(max_length = 100)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
# class Choice(models.Model):
#     choice_text = models.CharField(max_length= 200)
#     votes = models.IntegerField(default= 0)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.choice_text
