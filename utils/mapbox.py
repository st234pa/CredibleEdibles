#Mapbox access token
#pk.eyJ1IjoibGF1cmVudGl1czkxMiIsImEiOiJjaXdkd2k2cnIwZDJ0MnpwZmViaWZ4OW9lIn0.eXZa4xOeNmH_Zuw-MukY9g

import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved
import operator

import string
import sys
import requests, json, urllib, urllib2, base64

#API functions

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

def geocode(address):
    
