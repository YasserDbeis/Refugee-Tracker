import logging
from pyunsplash import PyUnsplash
# instantiate PyUnsplash object
pu = PyUnsplash(api_key=api_key)

# pyunsplash logger defaults to level logging.ERROR
# If you need to change that, use getLogger/setLevel
# on the module logger, like this:
logging.getLogger("pyunsplash").setLevel(logging.DEBUG)

# Start with the generic collection, maximize number of items
# note: this will run until all photos of all collections have
#       been visited, unless a connection error occurs.
#       Typically the API hourly limit gets hit during this


images = []

search = pu.search(type_='photos', query='refugee camps')
for entry in search.entries:
    linkAndAuthor = {}
    linkAndAuthor['link'] = entry.link_download
    linkAndAuthor['author'] = entry.get_attribution()
    images.append(linkAndAuthor)

print(images)


    # no need to specify per_page: will take from original object
# no need to specify per_page: will take from original object
