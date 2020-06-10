import tkinter
import math
from urllib.request import urlopen, urlretrieve
from urllib.parse import urlencode, quote_plus
import json

# To use, see the last function in this file, startGUI().

# Given a string representing a location, return 2-element 
# [latitude, longitude] list for that location 
#
# See https://developers.google.com/maps/documentation/geocoding/
# for details
#
def geocodeAddress(addressString):
   global url
   urlbase = "http://maps.googleapis.com/maps/api/geocode/json?address="
   url = urlbase + quote_plus(addressString)
   
   stringResultFromGoogle = urlopen(url).read().decode('utf8')
   jsonResult = json.loads(stringResultFromGoogle)
   if (jsonResult['status'] != "OK"):
      print("Status returned from Google geocoder *not* OK: {}".format(jsonResult['status']))
      return
   loc = jsonResult['results'][0]['geometry']['location']
   return (float(loc['lat']),float(loc['lng']))


# Contruct a Google Static Maps API URL that specifies a map that is:
# - width-by-height in size (in pixels)
# - is centered at latitude lat and longitude long
# - is "zoomed" to the give Google Maps zoom level
#
# See https://developers.google.com/maps/documentation/static-maps/
#
# YOU WILL NEED TO MODIFY THIS TO BE ABLE TO
# 1) DISPLAY A PIN ON THE MAP
# 2) SPECIFY MAP TYPE - terrain vs road vs ...
#
def getMapUrl(width, height, lat, lng, zoom):
   urlbase = "http://maps.google.com/maps/api/staticmap?"
   args = "center={},{}&zoom={}&size={}x{}&format=gif".format(lat,lng,zoom,width,height)
   return  urlbase+args

# Retrieve a map image via Google Static Maps API:
# - centered at the location specified by global variable mapLocation
# - zoomed according to global variable zoomLevel (Google's zoom levels range from 0 to 21)
# - width and height equal to global variable mapSize
# Store the returned image in file name specified by global variable mapFileName
#
def retrieveMap():
   lat, lng = geocodeAddress(mapLocation)
   url = getMapUrl(mapSize, mapSize, lat, lng, zoomLevel)
   urlretrieve(url, mapFileName)
   return mapFileName

########## 
# very basic GUI code

# Global variables used by GUI and map code
#

rootWindow = None
mapLabel = None

defaultLocation = "Mauna Kea, Hawaii"
mapLocation = defaultLocation
mapFileName = 'googlemap.gif'
mapSize = 400
zoomLevel = 9

def readEntryAndShowMap():
   global mapLocation
   #### you should change this function to read from the location from an Entry widget
   #### instead of using the default location
   mapLocation = defaultLocation
   showMap()
    
def showMap():
   retrieveMap()    
   mapImage = tkinter.PhotoImage(file=mapFileName)
   mapLabel.configure(image=mapImage)
   # next line necessary to "prevent (image) from being garbage collected" - http://effbot.org/tkinterbook/label.htm
   mapLabel.mapImage = mapImage  
  
def initializeGUIetc():
   global rootWindow
   global mapLabel

   rootWindow = tkinter.Tk()
   rootWindow.title("HW9 Q2")

   mainFrame = tkinter.Frame(rootWindow) 
   mainFrame.pack()

   # until you add code, pressing this button won't change the map.
   # you need to add an Entry widget that allows you to type in an address
   # The click function should extract the location string from the Entry widget and create
   # the appropriate map.
   readEntryAndShowMapButton = tkinter.Button(mainFrame, text="Show me the map!", command=readEntryAndShowMap)
   readEntryAndShowMapButton.pack()

   # we use a tkinter Label to display the map image
   mapLabel = tkinter.Label(mainFrame, bd=2, relief=tkinter.FLAT)
   mapLabel.pack()

def startGUI():
    initializeGUIetc()
    showMap()
    rootWindow.mainloop()
