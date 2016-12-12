#!/usr/bin/python
import sys
script_path = "/rauth"
if script_path in sys.path:
    print "oops, it's already in there."
else:
    sys.path.insert(0, script_path)

from flask import request
import key
import json, urllib, urllib2
#from requests_oauth2 import OAuth2
import rauth
#from rauth import oauth, service, session, utils, compat


#oauth help: creds to http://letstalkdata.com/2014/02/how-to-use-the-yelp-api-in-python/

#distance is in meters, this is **from the form**
def get_search_parameters(lat,longi,distance):
  #See the Yelp API for more details
  params = {}
  params["term"] = "restaurant"
  params["ll"] = "{},{}".format(str(lat),str(longi))
  params["radius_filter"] = distance
  params["limit"] = "10"
  return params

# 	*****Softdev Notes*****
#	json:
# 		library to work with json data.
# 		.loads
# 			d = json.loads(<STRING>)
# 		.dumps(<DICTIONARY>)
# 			turns a python dict into a json object string
# 		oauth
# 			more in depth authentication

def get_results(params):
	
  dic = key.getkeydict()
  consumer_key = dic['yelp_consumer_key']
  consumer_secret = dic['yelp_consumer_secret']
  token = dic['yelp_token']
  token_secret = dic['yelp_token_secret']
   
  session = rauth.OAuth1Session(
    consumer_key = consumer_key
    ,consumer_secret = consumer_secret
    ,access_token = token
    ,access_token_secret = token_secret)
  #returns a json object, sends a get request, returns a Response Object   
  request = session.get("http://api.yelp.com/v2/search",params=params)  
  #returns a python dictionary, converted from json
  data = request.json()
  session.close()  
  #print data
  #print "\n\n\n\n"
  return data
     
  

#uses search results helper function, creates a big list of businesses and the attributes we need to know
#shiz i need to return: name, coordinates, rating, address, image
def makeBusinessesList(rating, distance, lat, longi):
	biz = []
	nasty = get_results(get_search_parameters(lat,longi,distance))
	for icky in nasty['businesses']:
		if icky['rating'] >= rating:
			placeInfo = {}
			placeInfo['rating'] = icky['rating']
			placeInfo['address'] = icky['location']['display_address']
			placeInfo['coord'] = icky['location']['coordinate']		
			bigdict = {}
			bigdict[icky['name']] = placeInfo
			biz.append(bigdict)
	return biz
	
		
#takes the business list and reformats it so steph can use it in JS
# {"type": "Feature",
# "geometry": { "type": "Point", "coordinates": [-77.03238901390978, 38.913188059745586]},
# "properties": {"title": "Mapbox DC","icon": "monument"}
# }

def makeJsList(bizList):
	returnList = []
	i = 0
	for item in bizList:
		for key in item:
			placeDict = {}
			coor = []
			lat = bizList[i][key]['coord']['latitude']
			lon = bizList[i][key]['coord']['longitude']
			placeDict["type"] = "Feature"
			placeDict["geometry"] = {"type": "Point", "coordinates": [lon, lat]}
			placeDict["properties"] = {"title": unicode(key).encode('utf-8'), "icon":"monument"}
			returnList.append(placeDict)
			i+=1
	return returnList	
	


#print makeJsList(makeBusinessesList(4, 800))
#reads directly from the API
#def getSearchResults(lat, long, price, rating, distance):
	

