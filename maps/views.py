from django.shortcuts import render
from django.http import HttpResponse
from .models import Location
from django.template import loader, RequestContext
from django.core.serializers import serialize
from .models import Location
import json
from django.contrib.gis.geos import Point
# Create your views here.

def index(request):
    latest_locations = Location.objects.order_by('city')
    geo_json_string = (serialize('geojson', Location.objects.all(), geometry_field = 'geom', fields = ('city', 'state', 'reference')))
    print(geo_json_string)
    template = loader.get_template('maps/index.html')
    context = {
        'geo_json_string' : geo_json_string
    }
    # output = ", ".join(l.city for l in latest_locations)
    return render(request, "maps/index.html", {'geo_json_string' : geo_json_string})

def detail(request, location_id):
    return HttpResponse("Location ID is {}".format(location_id))

