from pynytimes import NYTAPI
import json

from GoogleNews import GoogleNews
googlenews = GoogleNews()



import datetime
from newsapi import NewsApiClient

querySet = [("M'bera Refugee Camp", 'MR'), ("Burkina Faso Refugee Camp", 'BF'), ("Niger Refugee Camp", 'NE'), ("Niger Refugee Camp", 'NE'), ("Malawi Refugee Camp", 'MW'), 
("Kenya Refugee Camp", 'KY'), ("Ethiopia Refugee Camp", 'ET'), ("Syria Refugee Camp", 'SY'), ("Jordan Refugee Camp", 'JO'), ("Iraq Refugee Camp", 'IQ'), 
("Bangladesh Refugee Camp", 'BD'), ("Sudan Refugee Camp", 'SD'), ("Turkey Refugee Camp", 'TR'), ("West Nile Refugee Camp", 'WN')]


# Init
# /v2/top-headlines

links = []
for query, iso2 in querySet:

    all_articles = newsapi.get_everything(q=query,
                                        from_param='2020-04-16',
                                        to= datetime.datetime.now().date(),
                                        language='en',
                                        sort_by='relevancy',
                                        page=1)
    countryToList = {}

    if(all_articles['totalResults'] is 0):
        all_articles = newsapi.get_everything(q='Refugee Camps',
                                            from_param='2020-04-16',
                                            to='2020-05-16',
                                            language='en',
                                            sort_by='relevancy',
                                            page=1)
    subList = []
    for article in all_articles['articles']:
        info = {}
        info['url'] = (article['url'])
        info['headline'] = (str(article['title']).replace(u"\u2018", "'").replace(u"\u2019", "'"))
        subList.append(info)

    countryToList[iso2] = subList
    links.append(countryToList)
linksJson = json.dumps(links)

print(linksJson)
