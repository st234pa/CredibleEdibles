import urllib2 
import string
import sys
import requests, json, urllib, urllib2, base64
import oauth
import oauth2
from requests_oauth2 import OAuth2
from rauth import oauth

# This prepates the credentials for Twitter
# def get_credentials():
#     #initialize to empty
#     creds = {}
#     creds['consumer_key'] = str()
#     creds['consumer_secret'] = str()
#     #get credentials
#     creds['consumer_key'] = "Ov-ytNFKKBZfdHYTkdQAoQ" #might have to change as API key expires
#     creds['consumer_secret'] = "b1z2H2DCRH4hf4aQo1zqaTyYYJA"
#     return creds


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


def main():
  locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
  api_calls = []
  for lat,long in locations:
    params = get_search_parameters(lat,long)
    api_calls.append(get_results(params))
    #Be a good internet citizen and rate-limit yourself
    time.sleep(1.0)
     
  ##Do other processing

print get_results(get_search_parameters(90.22,100.04))

#def oauth(credentials):

# def oauth():
# 	yelp_api = YelpAPI("Ov-ytNFKKBZfdHYTkdQAoQ", "b1z2H2DCRH4hf4aQo1zqaTyYYJA", "ZCsTHSJC7DAlSVmSQS0e7pxQDDCH_Thk","CNMwy2PUHaXTyXTQe4Qv2lk4BuE")
# 	search_results = yelp_api.search_query(term='Neptune Oyster', location='Boston, MA')
# 	print search_results


    #try:
        #Encode creds
    # encoded_credentials = base64.b64encode(credentials['consumer_key'] + ':' + credentials['consumer_secret'])
    # #Prepare URL and HTTP parameters
    # post_url = "https://api.yelp.com/v2/search/?"
    # parameters = {'grant_type' : 'client_credentials'}
    # #Prepare headers
    # auth_headers = {
    #     "Authorization" : "Basic %s" % encoded_credentials,
    #     "Content-Type"  : "application/x-www-form-urlencoded;charset=UTF-8"
    # }
    # print "hi"
    # # Make a POST call
    # results = requests.post(url=post_url, data=urllib.urlencode(parameters), headers=auth_headers)
    # response = results.json()

    # # Store the access_token and token_type for further use
    # auth = {}
    # #auth['access_token'] = response['access_token']
    # auth['access_token'] = "ZCsTHSJC7DAlSVmSQS0e7pxQDDCH_Thk"
    # auth['token_type']   = response['token_type']

    # return auth
    


    # #except Exception as e:
    # #print "Failed to authenticate with Twitter credentials:", e
    # #print "Twitter consumer key:", credentials['consumer_key']
    # #print "Twitter consumer secret:", credentials['consumer_secret']
    # sys.exit()


#making and parsing a REST call in python

# urllib2 
# 	library designed to handle urls
# 	.urlopen
# 	u = urllib2.urlopen(<URL>)
# 	open a url to be read by your program
# 	.geturl()
# 		reutnrs the actual url (in case of redirects)
# 	.info()
# 		returns the http/s header information
# 	.read()
# 		returns the contents of the target webpage.
# 	use urlopen on ur rest api links
# 	now its going to grab what I would get from this website
# 	should return some json object as a string
# 	json:
# 		library to work with json data.
# 		.loads
# 			d = json.loads(<STRING>)
# 		.dumps(<DICTIONARY>)
# 			turns a python dict into a json object string
# 		oauth
# 			more in depth authentication

#uses search results helper function, creates a big list of businesses and the attributes we need to know
#def makeBusinessesList():


#takes the business list and reformats it so steph can use it in JS
# {"type": "Feature",
# "geometry": { "type": "Point", "coordinates": [-77.03238901390978, 38.913188059745586]},
# "properties": {"title": "Mapbox DC","icon": "monument"}
# }
#def makeJsList(bizList):



#reads directly from the API
#def getSearchResults(lat, long, price, rating, distance):
	

