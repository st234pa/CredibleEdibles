import urllib2 
from requests_oauth2 import OAuth2
OAuth2(client_id, client_secret, site, redirect_uri, [authorization_url='oauth/authorize'], [token_url='oauth/token'])

 oauth2_handler = OAuth2(client_id, client_secret, "https://www.facebook.com/", "http://yoursite.com/webhook", "dialog/oauth", "oauth/access_token")
authorization_url = oauth2_handler.authorize_url('email')


# This prepates the credentials for Twitter
def get_credentials():
    #initialize to empty
    creds = {}
    creds['consumer_key'] = str()
    creds['consumer_secret'] = str()
    #get credentials
    creds['consumer_key'] = "JRRQwIBrhimuwIffw9ZlncDSg" #might have to change as API key expires
    creds['consumer_secret'] = "kfsbDKfo8VHVhb1IKhhmX45I1sMnyfSqDJrBdK2MRkURWwAwxD"
    return creds

def oauth(credentials):
    try:
        #Encode creds
        encoded_credentials = base64.b64encode(credentials['consumer_key'] + ':' + credentials['consumer_secret'])
        #Prepare URL and HTTP parameters
        post_url = "https://api.twitter.com/oauth2/token"
        parameters = {'grant_type' : 'client_credentials'}
        #Prepare headers
        auth_headers = {
            "Authorization" : "Basic %s" % encoded_credentials,
            "Content-Type"  : "application/x-www-form-urlencoded;charset=UTF-8"
            }

        # Make a POST call
        results = requests.post(url=post_url, data=urllib.urlencode(parameters), headers=auth_headers)
        response = results.json()

        # Store the access_token and token_type for further use
        auth = {}
        auth['access_token'] = response['access_token']
        auth['token_type']   = response['token_type']

        return auth
    except Exception as e:
        print "Failed to authenticate with Twitter credentials:", e
        print "Twitter consumer key:", credentials['consumer_key']
        print "Twitter consumer secret:", credentials['consumer_secret']
        sys.exit()

def get_tweets_timeline(screen_name, num_tweets, auth):
    # This collection will hold the Tweets as they are returned from Twitter
    collection = []
    
    # Prepare GET call, timeline URL, headers, parameters
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    timeline_headers = {
        "Authorization" : "Bearer %s" % auth['access_token']
    }
    parameters = {
        'screen_name' : screen_name,
        'count' : num_tweets,
        'lang' : 'en'
    }
    
    # Construct actual url to send to Twitter to get the timeline tweets
    get_url = url + '?' + urllib.urlencode(parameters)

    # Make the GET call to Twitter
    results = requests.get(url=get_url, headers=timeline_headers)
    #Twitter RESPONSE in JSON format.. YAY!
    response = results.json()
    #if (response.empty()):
    #    print "Twitter gave an empty response.  Do you have a valid username? Do you have tweets?"
    return response

def FStoD():
    d = {}
    form_data = cgi.FieldStorage()
    for k in form_data.keys():
       d[k] = form_data[k].value
    return d






















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
def makeBusinessesList():




#takes the business list and reformats it so steph can use it in JS
# {"type": "Feature",
# "geometry": { "type": "Point", "coordinates": [-77.03238901390978, 38.913188059745586]},
# "properties": {"title": "Mapbox DC","icon": "monument"}
# }
def makeJsList(bizList):





#reads directly from the API
def getSearchResults(lat, long, price, rating, distance):
	results = urllib2.urlopen("https://api.yelp.com/v2/search?")
