import urllib2 
import string
import sys
import requests, json, urllib, urllib2, base64
from requests_oauth2 import OAuth2
from yelpapi import YelpAPI
#OAuth2(client_id, client_secret, site, redirect_uri, [authorization_url='oauth/authorize'], [token_url='oauth/token'])
#oauth2_handler = OAuth2(client_id, client_secret, "https://www.facebook.com/", "http://yoursite.com/webhook", "dialog/oauth", "oauth/access_token")
#authorization_url = oauth2_handler.authorize_url('email')


# class Oauth1Authenticator(object):

#     def __init__(
#         self,
#         consumer_key,
#         consumer_secret,
#         token,
#         token_secret
#     ):
#         self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
#         self.token = oauth2.Token(token, token_secret)

#     def sign_request(self, url, url_params={}):
#         oauth_request = oauth2.Request(
#             method="GET",
#             url=url,
#             parameters=url_params
#         )
#         oauth_request.update(
#             {
#                 'oauth_nonce': oauth2.generate_nonce(),
#                 'oauth_timestamp': oauth2.generate_timestamp(),
#                 'oauth_token': self.token.key,
#                 'oauth_consumer_key': self.consumer.key
#             }
#         )
#         oauth_request.sign_request(
#             oauth2.SignatureMethod_HMAC_SHA1(),
#             self.consumer,
#             self.token
#         )
#         return oauth_request.to_url()


# This prepates the credentials for Twitter
def get_credentials():
    #initialize to empty
    creds = {}
    creds['consumer_key'] = str()
    creds['consumer_secret'] = str()
    #get credentials
    creds['consumer_key'] = "Ov-ytNFKKBZfdHYTkdQAoQ" #might have to change as API key expires
    creds['consumer_secret'] = "b1z2H2DCRH4hf4aQo1zqaTyYYJA"
    return creds


def get_search_parameters(lat,long):
  #See the Yelp API for more details
  params = {}
  params["term"] = "restaurant"
  params["ll"] = "{},{}".format(str(lat),str(long))
  params["radius_filter"] = "2000"
  params["limit"] = "10"
  return params




def get_results(params):
 
  #Obtain these from Yelp's manage access page
  consumer_key = "YOUR_KEY"
  consumer_secret = "YOUR_SECRET"
  token = "YOUR_TOKEN"
  token_secret = "YOUR_TOKEN_SECRET"
   
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



#def oauth(credentials):

def oauth():
	yelp_api = YelpAPI("Ov-ytNFKKBZfdHYTkdQAoQ", "b1z2H2DCRH4hf4aQo1zqaTyYYJA", "ZCsTHSJC7DAlSVmSQS0e7pxQDDCH_Thk","CNMwy2PUHaXTyXTQe4Qv2lk4BuE")
	search_results = yelp_api.search_query(term='Neptune Oyster', location='Boston, MA')
	print search_results


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
def getSearchResults(lat, long, price, rating, distance):
	print get_credentials()
	#results = urllib2.urlopen("https://api.yelp.com/v2/search?")



oauth()
