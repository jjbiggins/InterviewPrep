from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json

flickrAPIKey = "YOUR-FLICKR-API-KEY-GOES-HERE"

def searchFlickr(topic, geo=None, maxNum = 20, radius=2):
    global url, resultFromFlickr, jsonresult, flickrPhotos
    base="https://api.flickr.com/services/rest/?"
    args = "method=flickr.photos.search&format=json&per_page={}&nojsoncallback=1".format(maxNum)
    topicPart = "&text=" + quote_plus(topic)

    url = base + args + topicPart + "&api_key=" + flickrAPIKey
    if geo != None:
        geoPart = "&lat={}&lon={}&radius={}".format(geo[0], geo[1], radius)
        url = url + geoPart
    resultFromFlickr= urlopen(url).read().decode('utf8')
    jsonresult = json.loads(resultFromFlickr)
    if jsonresult['stat'] == 'ok':
        flickrPhotos = jsonresult['photos']['photo']
        print("{} photos found".format(len(flickrPhotos)))
        return flickrPhotos
    else:
        print("status returned from Flickr not ok")

def photoURL(photoListItem):
    farmId = photoListItem['farm']
    serverId = photoListItem['server']
    photoId = photoListItem['id']
    secret = photoListItem['secret']
    url = "https://farm{}.staticflickr.com/{}/{}_{}.jpg".format(farmId,serverId,photoId, secret)
    return url

def photoLoc(photoListItem):
    global photoI
    base="https://api.flickr.com/services/rest/?"
    args = "method=flickr.photos.getInfo&format=json&nojsoncallback=1"
    idPart = "&photo_id=" + photoListItem['id']
    url = base + args + idPart + "&api_key=" + flickrAPIKey
    resultFromFlickr= urlopen(url).read().decode('utf8')
    photoI = json.loads(resultFromFlickr)
    photoI = photoI['photo']
    loc = photoI['location']
    lat = float(loc['latitude'])
    lon = float(loc['longitude'])
    return (lat, lon)

def photoInfo(photoListItem):
    global photoI
    base="https://api.flickr.com/services/rest/?"
    args = "method=flickr.photos.getInfo&format=json&nojsoncallback=1"
    idPart = "&photo_id=" + photoListItem['id']
    url = base + args + idPart + "&api_key=" + flickrAPIKey
    resultFromFlickr= urlopen(url).read().decode('utf8')
    photoI = json.loads(resultFromFlickr)
    return photoI

import webbrowser
def showFlickrPhoto(photoListItem):
    webbrowser.open(photoURL(photoListItem))

def showFlickrPhotoPage(photoListItem):
    pI = photoInfo(photoListItem)
    pageURL = pI['photo']['urls']['url'][0]['_content']
    webbrowser.open(pageURL)   
	

    
        

    
