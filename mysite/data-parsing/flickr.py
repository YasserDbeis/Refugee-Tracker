import flickr_api
from flickr_api import Walker, Photo

user = flickr_api.Person.findByEmail('asamoaht@unhcr.org')
photos = user.getPhotos()

for photo in photos:
    print(photo.title)
    print(photo.getPageUrl())



# w = Walker(Photo.search, tags="syria crisis")
# for photo in w:
#     print(photo.title)
#     print(photo.getPageUrl())