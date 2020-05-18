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
import logging
from datetime import datetime, timedelta
from newsapi import NewsApiClient
import flickr_api
from flickr_api import Walker, Photo
nyt = NYTAPI("n0zstttYijH85qvE5B25zpdcY6VCoAW0")
flickr_api.set_keys(api_key = '1e68e420d9c8bd0e33301429630cf3b5', api_secret = '67a16ddaf7414f8f')

import datetime



# Create your views here.

def index(request):

    geo_json_string = GeoJSONSerializer().serialize(Location.objects.all(),  use_natural_keys=True, with_modelname=False)



    querySet = [("M'bera Refugee Camp", 'MR'), ("Burkina Faso Refugee Camp", 'BF'), ("Niger Refugee Camp", 'NE'),
                ("Niger Refugee Camp", 'NE'), ("Malawi Refugee Camp", 'MW'),
                ("Kenya Refugee Camp", 'KY'), ("Ethiopia Refugee Camp", 'ET'), ("Syria Refugee Camp", 'SY'),
                ("Jordan Refugee Camp", 'JO'), ("Iraq Refugee Camp", 'IQ'),
                ("Bangladesh Refugee Camp", 'BD'), ("Sudan Refugee Camp", 'SD'), ("Turkey Refugee Camp", 'TR'),
                ("West Nile Refugee Camp", 'WN')]

    newsapi = NewsApiClient(api_key='e7574739bccf4313bf4f01f06774802f')

    links = []
    for query, iso2 in querySet:
    
        all_articles = newsapi.get_everything(q=query,
                                              from_param='2020-04-17',
                                              to=datetime.datetime.now().date(),
                                              language='en',
                                              sort_by='relevancy',
                                              page=1)
        countryToList = {}
    
        if (all_articles['totalResults'] is 0):
            all_articles = newsapi.get_everything(q='Refugee Camps',
                                                  from_param='2020-04-16',
                                                  to='2020-05-16',
                                                  language='en',
                                                  sort_by='relevancy',
                                                  page=1)
        subList = []
        for article in all_articles['articles']:
            info = {'url': (article['url']),
                    'headline': (str(article['title']).replace(u"\u2018", "'").replace(u"\u2019", "'"))}
            subList.append(info)
    
        countryToList[iso2] = subList
        links.append(countryToList)

    linksJson = json.dumps(links)

    print(linksJson)

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
    print(countriesList)
    countriesJSONs = []

    for country in countriesList:
        countriesPop = {}
        countriesPop['country'] = country
        countriesPop['population'] = (Population.objects.filter(origin=country).aggregate(Sum('refugeePop')))['refugeePop__sum']
        countriesJSONs.append(countriesPop)


    countriesPop = json.dumps(countriesJSONs)



    # instantiate PyUnsplash object

    # pyunsplash logger defaults to level logging.ERROR
    # If you need to change that, use getLogger/setLevel
    # on the module logger, like this:

    # Start with the generic collection, maximize number of items
    # note: this will run until all photos of all collections have
    #       been visited, unless a connection error occurs.
    #       Typically the API hourly limit gets hit during this

    user = flickr_api.Person.findByUserName('MedGlobal')
    photos = user.getPhotos()

    images = []
    i = 0
    for photo in photos:
        i+=1
        linkAndAuthor = {'link': photo.getPhotoFile(), 'title': photo.title}
        images.append(linkAndAuthor)
        if i == 20:
            break

    images = json.dumps(images)

    return render(request, "maps/index.html", {'geo_json_string' : geo_json_string, 'links' : linksJson, 'regions' : regionsPop, 'subregions' : subregionsPop, 'countries' : countriesPop, 'images' : images})

# def stories(request):



#     return render(request, "maps/index.html", {'images' : images})

