#Mapbox access token
#pk.eyJ1IjoibGF1cmVudGl1czkxMiIsImEiOiJjaXdkd2k2cnIwZDJ0MnpwZmViaWZ4OW9lIn0.eXZa4xOeNmH_Zuw-MukY9g

import cgi
import urllib2

#import json, requests
import json


#urllib2 
#	.urlopen
#	u = urllib2.urlopen(<URL>)
#	open a url to be read by your program
#	.geturl()
#		reutnrs the actual url (in case of redirects)
#	.info()
#		returns the http/s header information
#	.read()
#		returns the contents of the target webpage.
#	use urlopen on ur rest api links
#	now its going to grab what I would get from this website
#	should return some json object as a string
#	json:
#		library to work with json data.
#		.loads
#			d = json.loads(<STRING>)
#		.dumps(<DICTIONARY>)
#			turns a python dict into a json object string


		
#API functions

# This prepares the credentials for Mapbox
#takes an address and returns the coordinates

def geocode(address):
	query = ""
	query = address.replace(" ", "%20")
	url = "https://api.mapbox.com/geocoding/v5/mapbox.places/\"" + query + "\".json?access_token=pk.eyJ1IjoibGF1cmVudGl1czkxMiIsImEiOiJjaXdkd2k2cnIwZDJ0MnpwZmViaWZ4OW9lIn0.eXZa4xOeNmH_Zuw-MukY9g"
	response = urllib2.urlopen(url)
	data = response.read()
	dic = json.loads(data)
	return dic['features'][0]['geometry']['coordinates']

	##~~~~~~~~OLD stuff WITH REQUESTS~~~~~~~~~~~~~##
	#url for accessing mapbox api
	#url = "https://api.mapbox.com/geocoding/v5/mapbox.places/" + address + ".json?access_token=pk.eyJ1IjoibGF1cmVudGl1czkxMiIsImEiOiJjaXdkd2k2cnIwZDJ0MnpwZmViaWZ4OW9lIn0.eXZa4xOeNmH_Zuw-MukY9g"
	#gets page info
	#data = requests.get(url).text
	#encodes into utf
	#response = data.encode('utf8')
	#turns into dictionary
	#dic = json.loads(response)
	#return dic['features'][0]['geometry']['coordinates']