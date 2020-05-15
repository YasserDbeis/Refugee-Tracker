from django.shortcuts import render
from django.http import HttpResponse
from .models import Location
from django.template import loader, RequestContext
from django.core.serializers import serialize
from .models import Location, Population
from djgeojson.serializers import Serializer as GeoJSONSerializer
import ast
import json
from django.contrib.gis.geos import Point
from django.db.models import Sum
from pynytimes import NYTAPI

nyt = NYTAPI("n0zstttYijH85qvE5B25zpdcY6VCoAW0")

import datetime



# Create your views here.

def index(request):
    articles = nyt.article_search(
        query="Refugee Camps",
        results=1,
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
    geo_json_string = GeoJSONSerializer().serialize(Location.objects.all(),  use_natural_keys=True, with_modelname=False)

    regionsQuery = Population.objects.values_list("region", flat=True).order_by("region").distinct()
    regionsList = list(regionsQuery)

    regionJSONs = []

    for region in regionsList:
        regionsPop = {}
        regionsPop['region'] = region
        regionsPop['population'] = (Population.objects.filter(region=region).aggregate(Sum('refugeePop')))['refugeePop__sum']
        regionJSONs.append(regionsPop)

    regionsPop = json.dumps(regionJSONs)

    subregionsQuery = Population.objects.values_list("subRegion", flat=True).order_by("subRegion").distinct()
    subregionsList = list(subregionsQuery)

    subregionsJSONs = []

    for subregion in subregionsList:
        subregionsPop = {}
        subregionsPop['subregion'] = subregion
        subregionsPop['population'] = (Population.objects.filter(subRegion=subregion).aggregate(Sum('refugeePop')))['refugeePop__sum']
        subregionsJSONs.append(subregionsPop)

    subregionsPop = json.dumps(subregionsJSONs)

    countriesQuery = Population.objects.values_list("origin", flat=True).order_by("refugeePop").distinct()
    countriesList = list(countriesQuery)
    countriesList = countriesList[-9:]
    print(countriesList)
    countriesJSONs = []

    for country in countriesList:
        countriesPop = {}
        countriesPop['country'] = country
        countriesPop['population'] = (Population.objects.filter(origin=country).aggregate(Sum('refugeePop')))['refugeePop__sum']
        countriesJSONs.append(countriesPop)


    countriesPop = json.dumps(countriesJSONs)

    return render(request, "maps/index.html", {'geo_json_string' : geo_json_string, 'links' : linksJson, 'regions' : regionsPop, 'subregions' : subregionsPop, 'countries' : countriesPop})

def detail(request, location_id):
    return HttpResponse("Location ID is {}".format(location_id))

