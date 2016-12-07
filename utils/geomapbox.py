#Mapbox access token
#pk.eyJ1IjoibGF1cmVudGl1czkxMiIsImEiOiJjaXdkd2k2cnIwZDJ0MnpwZmViaWZ4OW9lIn0.eXZa4xOeNmH_Zuw-MukY9g

import cgi
import urllib2

import json, requests

#API functions

# This prepares the credentials for Mapbox
def geocode(address):
    #url for accessing mapbox api
    url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + address + ".json?access_token=pk.eyJ1IjoibGF1cmVudGl1czkxMiIsImEiOiJjaXdkd2k2cnIwZDJ0MnpwZmViaWZ4OW9lIn0.eXZa4xOeNmH_Zuw-MukY9g"
    #gets page info
    data = requests.get(url).text
    #encodes into utf
    response = data.encode('utf8')
    #turns into dictionary
    dic = json.loads(response)
    return dic['features'][0]['geometry']['coordinates']