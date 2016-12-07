import urllib2 
import string
import sys
import requests, json, urllib, urllib2, base64
from requests_oauth2 import OAuth2
import rauth


def get_search_parameters(lat,longi):
  #See the Yelp API for more details
  params = {}
  params["term"] = "restaurant"
  params["ll"] = "{},{}".format(str(lat),str(longi))
  params["radius_filter"] = "2000"
  params["limit"] = "10"
  return params



def get_results(params):
 
  #Obtain these from Yelp's manage access page
  consumer_key = "Ov-ytNFKKBZfdHYTkdQAoQ"
  consumer_secret = "b1z2H2DCRH4hf4aQo1zqaTyYYJA"
  token = "ZCsTHSJC7DAlSVmSQS0e7pxQDDCH_Thk"
  token_secret = "CNMwy2PUHaXTyXTQe4Qv2lk4BuE"
   
  session = rauth.OAuth1Session(
    consumer_key = consumer_key
    ,consumer_secret = consumer_secret
    ,access_token = token
    ,access_token_secret = token_secret)
     
  request = session.get("http://api.yelp.com/v2/search",params=params)
   
  #Transforms the JSON API response into a Python dictionary
  data = request.json()
  session.close()
   
  return data
     
  ##Do other processing

	#print get_results(get_search_parameters(40.7179,-74.014))


# 	json:
# 		library to work with json data.
# 		.loads
# 			d = json.loads(<STRING>)
# 		.dumps(<DICTIONARY>)
# 			turns a python dict into a json object string
# 		oauth
# 			more in depth authentication

#uses search results helper function, creates a big list of businesses and the attributes we need to know
def makeBusinessesList():
	nasty = get_results(get_search_parameters(40.7179,-74.014))
	for icky in nasty['businesses']:
		print str(icky) + "\n\n"


makeBusinessesList()	


#takes the business list and reformats it so steph can use it in JS
# {"type": "Feature",
# "geometry": { "type": "Point", "coordinates": [-77.03238901390978, 38.913188059745586]},
# "properties": {"title": "Mapbox DC","icon": "monument"}
# }
#def makeJsList(bizList):



#reads directly from the API
#def getSearchResults(lat, long, price, rating, distance):
	

