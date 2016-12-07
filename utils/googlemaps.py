#Google Maps Geolocation API key
#AIzaSyDo7RrtqBzWPeQrNz-ksCGPYuooJU30nMc

import cgi
import urllib2

import json, requests #requests > urllib2 any day of the week

def locate():
	#url for accessing google maps geolcation api
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCcGLxvBq_qRytZgRUQJsLfgHapv9anAqw"
    #gets page info
    data = requests.post(url).text
    #encodes into utf
    response = data.encode('utf8')
    #turns into dictionary
    dic = json.loads(response)
    loc = []
    loc.append(dic['location']['lat'])
    loc.append(dic['location']['lng'])
    return loc