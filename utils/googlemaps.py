#Google Maps Geolocation API key
#AIzaSyDo7RrtqBzWPeQrNz-ksCGPYuooJU30nMc

import cgi
import urllib2

import json, requests

def locate():
	#url for accessing google maps geolcation api
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDo7RrtqBzWPeQrNz-ksCGPYuooJU30nMc"
    #gets page info
    data = requests.get(url).text
    #encodes into utf
    response = data.encode('utf8')
    #turns into dictionary
    print response

locate()