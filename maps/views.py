from django.shortcuts import render
from django.http import HttpResponse
from .models import Location
from django.template import loader, RequestContext
from django.core.serializers import serialize
from .models import Location
from djgeojson.serializers import Serializer as GeoJSONSerializer
from pynytimes import NYTAPI

import json
from django.contrib.gis.geos import Point
# Create your views here.

def index(request):
    articles = nyt.article_search(
        query="Refugee Camps",
        results=50,
        dates={
            "begin": datetime.datetime(2020, 1, 1),
            "end": datetime.datetime.now(),
        }
    )

    links = []

    for article in articles:
        pair = {}
        pair['url'] = (article['web_url'])
        pair['headline'] = (str(article['headline']['main']).replace(u"\u2018", "'").replace(u"\u2019", "'"))
        links.append(pair)

    linksJson = json.dumps(links)
    print(linksJson)
    latest_locations = Location.objects.order_by('city')
    geo_json_string = GeoJSONSerializer().serialize(Location.objects.all(), use_natural_keys=True, with_modelname=False)

    # geo_dict = json.load(geo_json_string)
    # print(type(geo_dict))
    # for r in geo_dict:
    #     print(r['city'])

    # geo_json_string = (GeoJSONSerializer().('geojson', Location.objects.all(), geometry_field = 'geom', fields = ('city', 'state', 'reference')))
    # print(geo_json_string)
    template = loader.get_template('maps/index.html')
    context = {
        'geo_json_string': geo_json_string,
        'links': linksJson,
    }
    # output = ", ".join(l.city for l in latest_locations)
    return render(request, "maps/index.html", {'geo_json_string': geo_json_string, 'links': linksJson})





    # latest_locations = Location.objects.order_by('city')
    # geo_json_string = GeoJSONSerializer().serialize(Location.objects.all(),  use_natural_keys=True, with_modelname=False)
    #
    # # geo_json_string = (GeoJSONSerializer().('geojson', Location.objects.all(), geometry_field = 'geom', fields = ('city', 'state', 'reference')))
    # print(geo_json_string)
    # template = loader.get_template('maps/index.html')
    # context = {
    #     'geo_json_string' : geo_json_string
    # }
    # # output = ", ".join(l.city for l in latest_locations)
    # return render(request, "maps/index.html", {'geo_json_string' : geo_json_string})

def detail(request, location_id):
    return HttpResponse("Location ID is {}".format(location_id))

