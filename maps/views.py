from asgiref.sync import sync_to_async
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
import logging
from datetime import datetime, timedelta
from newsapi import NewsApiClient
import flickr_api
from flickr_api import Walker, Photo
import os, sys
from gnews import GNews

# sys.path.insert(1, '/path/to/application/app/folder')

sys.path.append(os.path.realpath('.'))

# Create your views here.

def getArticles():

    regionAndCountries = [
        ('Middle East', ['SY', 'TR', 'JO', 'IQ']),
        ('East Africa', ['KY', 'ET', 'SD', 'WN', 'MW']),
        ('West Africa', ['MR', 'BF', 'NE',]),
        ('South Asia', ['BD'])
    ]

    links = []
    for region, countries in regionAndCountries:
  
        gn = GNews(max_results=20, language='en')
    
        all_articles = gn.get_news(region + " Refugee Camp")
        print(all_articles)

        countryToList = {}
    
        if (len(all_articles) == 0):
                all_articles = gn.get_news('Refugee Camps')
                    
        subList = []
        i = 0
        for article in all_articles:
            info = {'url': (article['url']),
                    'headline': (str(article['title']).replace(u"\u2018", "'").replace(u"\u2019", "'"))}
            subList.append(info)
            i = i + 1
            if(i == 20):
                break
    
        for country in countries:
            countryToList[country] = subList

        links.append(countryToList)

    linksJson = json.dumps(links)

    return linksJson
    

def index(request):

    geo_json_string = GeoJSONSerializer().serialize(Location.objects.all(), use_natural_keys=True, with_modelname=False)

    links = getArticles()
    
    #end of articles - start of regional stats queries

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
    countriesJSONs = []

    for country in countriesList:
        countriesPop = {}
        countriesPop['country'] = country
        countriesPop['population'] = (Population.objects.filter(origin=country).aggregate(Sum('refugeePop')))['refugeePop__sum']
        countriesJSONs.append(countriesPop)

    countriesPop = json.dumps(countriesJSONs)

    # hardcoded image urls because API was too slow
    # user = flickr_api.Person.findByUserName('MedGlobal')
    # photos = user.getPhotos()

    images = ['https://live.staticflickr.com/65535/49757472791_95d370c625_b.jpg', 'https://live.staticflickr.com/65535/49757808382_4b4e4a86d4_b.jpg', "https://live.staticflickr.com/65535/49757474531_155b81172d_6k.jpg"]     
    images = json.dumps(images)

    print("IMAGES DONE")
    return render(request, "maps/index.html", {'geo_json_string' : geo_json_string, 'links' : links, 'regions' : regionsPop, 'subregions' : subregionsPop, 'countries' : countriesPop, 'images' : images})
