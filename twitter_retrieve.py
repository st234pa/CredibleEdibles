#!/usr/bin/python
print 'Content-Type: text/html'
print ''
#-------------essentials!--------------------------

#------------- Opening Bookends -------------------
import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved
import operator
import numpy #for Pearsons


#import for Twitter access and encoding
import string
import sys
import requests, json, urllib, urllib2, base64


print '<html>'
print '<head><title> Tweet Analysis </title></head>'
style = """<style>
		head, body {
			background: url("cloudy-sky-cartoon.jpg") no-repeat 50% 50% fixed; 
            background-size: cover;
            -moz-background-size: cover;
            -o-background-size: cover;
            -webkit-background-size: cover;
			font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;
			   }
	    .center {
            margin-left: auto;
            margin-right: auto;
            width: 70%;
	    }
		a:link, a:visited, a:hover, a:active {
			color: black;
			}
		div {
		    text-align: center;
		}
		table, th, td {
		    font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;
            border: 1px solid black;
            border-collapse: collapse;
        }
        h1 {
            text-align: center;
        }

        h2 {
            text-align: center;
        }

        h3 {
            text-align: center;
        } 
		
	</style>
	<div>"""
print style
print '<body>'

#=============== Prepared HTML for conditionals==============
corrShplain = """*The number shown for correlations is Pearson's correlation
coefficient, or <i>r</i>. It being closer to -1 indicates a strong negative correlation,
and it being closer to 1 indicates a strong positive correlation. The closer it is to 0,
the more the data lacks correlation.
"""
rets = "<h3>Average times retweeted (per tweet): </h3>"
fols = "<h3>Follower amount: </h3>"
cCount = "<h3>Average Character Count (per tweet): </h3>"
reject = "does not exist as a Twitter handle. <a href = \"twitter.com\">Would you like to make it one?</a></h2>"
#=============== API functions ===================

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

# ~~~~~~~~~~~~~~~~~~~~~~~USEFUL GLOBAL VARS~~~~~~~~~~~~~~~~~~~~~~~~~~
#================ JSON Analysis ===================
stopwords_list = []

hashtag_count = {}

word_count = {}

def pearson(L1,L2): #correlation coefficient
    filter(lambda v: v==v, L1) #gets rid of NaN's
    filter(lambda v: v==v, L2)
    corr = numpy.corrcoef(L1, L2)[0, 1]
    return corr

def word_table():
    reversed_dict = {}
    #creates a reversed dictionary where freq is key and words are values (stored in list)
    for word in word_count:
        if word_count[word] not in reversed_dict:
            new_word_list = []
            new_word_list.append(word)
            reversed_dict[word_count[word]] = new_word_list
        else:
            new_word_list = reversed_dict[word_count[word]]
            new_word_list.append(word)
            reversed_dict[word_count[word]] = new_word_list
    reversed_word_keys = sorted(reversed_dict.keys(), reverse=True)
    retStr='<table align="center"><th>Word</th><th>Frequency</th>'
    counter = 0 #used to limit to top 20 words
    done = False #flag to see whether 20 reached
    for i in reversed_word_keys:
        word_list = reversed_dict[i]
        for word in word_list:
            if counter >= 20: #once counter, met set flag and break
                done = True
                break
            retStr+='<tr>'
            retStr+= '<td>'+str(word)+'</td>'+'<td>'+str(i)+'</td>'
            retStr+='</tr>'
            counter += 1
        if done == True:
            break
    retStr+= '</table>'
    return retStr

def hashtag_table():
    reversed_dict = {}
    #creates a reversed dictionary where freq is key and words are values (stored in list)
    for tag in hashtag_count:
        if hashtag_count[tag] not in reversed_dict:
            new_tag_list = []
            new_tag_list.append(tag)
            reversed_dict[hashtag_count[tag]] = new_tag_list
        else:
            new_tag_list = reversed_dict[hashtag_count[tag]]
            new_tag_list.append(tag)
            reversed_dict[hashtag_count[tag]] = new_tag_list
    reversed_tag_keys = sorted(reversed_dict.keys(), reverse=True)
    retStr='<table align="center"><th>Hashtag</th><th>Frequency</th>'
    counter = 0 #used to limit to top 20 words
    done = False #flag to see whether 20 reached
    for i in reversed_tag_keys:
        tag_list = reversed_dict[i]
        for tag in tag_list:
            if counter >= 10: #once counter, met set flag and break
                done = True
                break
            retStr+='<tr>'
            retStr+= '<td>'+str(tag)+'</td>'+'<td>'+str(i)+'</td>'
            retStr+='</tr>'
            counter += 1
        if done == True:
            break
    retStr+= '</table>'
    return retStr


def load_stopwords():
    in_stream = open('stopwords_list.txt','r')
    output = in_stream.read()
    in_stream.close()
    global stopwords_list 
    stopwords_list = output.split('\n')
    
    
def analyze_response_text(response):
    for t_tweet in response:
        t_text = t_tweet["text"]
        t_text = t_text.encode('ascii', 'ignore').decode('ascii') #converts all utf chars to ASCII, flattens, fix this later
        t_text = t_text.lower()
        word_list = t_text.split(' ')
        for word in word_list:
            word = str(word)
            word = word.strip('''.!?,;:-()[]{}'"''')
            word = word.replace('\'','')
            if is_valid_word(word): #if not stopword
                if word in word_count:
                    word_count[word] += 1 #add to bucket
                else:
                    word_count[word] = 1 #create a bucket
    return word_table()
    #Time to sort word_count
    #sorted_word_count = sorted(word_count.items(), key=operator.itemgetter(1))
    #return sorted_word_count # make this prettier later on

def get_all_tweets(response):
    all_tweets = ''
    for t_tweet in response:
        t_text = t_tweet["text"]
        t_text = t_text.encode('ascii', 'ignore').decode('ascii') #converts all utf chars to ASCII, flattens, fix this later
        t_text = t_text.lower()
        all_tweets += t_text + ' '
    return all_tweets

def analyze_response_hashtag(response):
    for t_tweet in response:
        t_text = t_tweet["text"]
        t_text = t_text.encode('ascii', 'ignore').decode('ascii') #converts all utf chars to ASCII, flattens, fix this later
        t_text = t_text.lower()
        word_list = t_text.split(' ')
        for word in word_list:
            word = str(word)
            word = word.strip(".!?,;:-()[]{}'")
            word = word.replace('\'','')
            word = word.replace(',',"")
            word = word.replace('\\n',"")
            if is_hashtag(word): #if hashtag
                if word in hashtag_count:
                    hashtag_count[word] += 1 #add to bucket
                else:
                    hashtag_count[word] = 1 #create a bucket
    return hashtag_table()
    #Time to sort word_count
    #sorted_word_count = sorted(hashtag_count.items(), key=operator.itemgetter(1))
    #return sorted_word_count # make this prettier later on
    
def access(screen_name):
    creds = get_credentials()
    auth = oauth(creds)
    num_tweets = 200
    response = get_tweets_timeline(screen_name, num_tweets, auth)
    return response
    
def avgCount(screen_name): #average tweet character count of user
    response = access(screen_name)
    charSum = 0 #character Sum
    for t_tweet in response:
        t_text = t_tweet["text"]
        t_text = t_text.encode('ascii', 'ignore').decode('ascii') #converts all utf chars to ASCII, flattens, fix this later
        t_text = t_text.lower()
        t_text = t_text.split("http")[0]
        if "rt" not in t_text:
            count = len(t_text)
        else: 
            count = len(t_text) - 2 #get rid of offset that is 'rt', indicating retweet
        charSum += count 
    retStr= str(charSum/ len(response)) #mean Character Sum
    return retStr

def followers(screen_name): #follower amount
    response = access(screen_name)
    placehold = "rt"
    pos = 0
    while placehold == "rt": #b/c not for rt post
        t_tweet = response[pos]
        t_text = t_tweet["text"]
        t_text = t_text.encode('ascii', 'ignore').decode('ascii') #converts all utf chars to ASCII, flattens, fix this later
        t_text = t_text.lower()
        placehold = t_text[:3]
        pos += 1 
    retStr = int(response[pos]['user'][u'followers_count']) #follower count
    return retStr

def is_numeric(word): #helper
    try:
        i = float(word)
    except (ValueError, TypeError):
        return False
    return True

def is_hashtag(word):
    if word != "":
	if word[0]=="#":
            return True
	else:
            return False

#to be added to as we find cases to fix
def is_valid_word(word): #boolean, T if not valid, F otherwise
    if word in stopwords_list:
        return False
    elif "#" in word:
        return False
    elif "http" in word:
        return False
    elif "$" in word:
        return False
    elif is_numeric(word):
        return False
    elif "@" in word:
        return False
    elif word == '':
        return False
    elif "~" in word:
        return False
    elif "%" in word:
        return False
    elif "&" in word:
        return False
    else:
        return True

def avgcount(screen_name): #avgCharacterCount
    response = access(screen_name)
    charSum = 0
    for t_tweet in response:
        t_text = t_tweet["text"]
        t_text = t_text.encode('ascii', 'ignore').decode('ascii') #converts all utf chars to ASCII, flattens, fix this later
        t_text = t_text.lower()
        t_text = t_text.split("http")[0]
        if "rt" not in t_text:
            count = len(t_text)
        else: 
            count = len(t_text) - 2
        charSum += count 
    return str(int(charSum/ len(response)))

def buzzwords(screen_name):
    response = access(screen_name)
    load_stopwords()
    retStr = ''
    retStr+= '<h3>Top 20 buzzwords in ' + str(screen_name) + "'s timeline!</h3>"
    retStr+= str(analyze_response_text(response))
    all_tweets = get_all_tweets(response)
    if all_tweets != '':
        sentiment_response = access_sentiment(all_tweets)
        entity_map = analyze_sentiment(sentiment_response)
        retStr+= '<h3>How does ' + str(screen_name) + " feel about ...</h3>"
        retStr+= '*On a sentiment scale of -1(NEGATIVE) to 1(POSITIVE) <br><br>'
        retStr+=convert_sentiment(entity_map)
    retStr+= '<h3>Top 10 Trending tags in ' + str(screen_name) + "'s timeline!</h3>"
    retStr+= str(analyze_response_hashtag(response))
    return retStr

def access_sentiment(all_tweets):
    #Call Alchemy API for sentiment
    # Base AlchemyAPI URL for targeted sentiment call
    alchemy_url = "http://access.alchemyapi.com/calls/text/TextGetRankedNamedEntities"
    # Parameter list, containing the data to be enriched
    len_tweets = len(all_tweets)
    if len_tweets > 5000:
        len_tweets = 5000
    all_tweets = all_tweets[0:len_tweets]
    parameters = {
        "apikey" : "c144cb756e62501c2aa2c25abf4603882293ceba",
        "text"   : all_tweets,
        "outputMode" : "json",
        "sentiment" : 1 
    }
    results = requests.get(url=alchemy_url, params=urllib.urlencode(parameters))
    response = results.json()
    return response
       
       
def analyze_sentiment(response):
    entity_list = response["entities"]
    entity_map = {}
    for entity in entity_list:
        e_text = entity["text"]
        e_text = e_text.encode('ascii', 'ignore').decode('ascii') #converts all utf chars to ASCII, flattens, fix this later
        e_text = e_text.lower()
      
        e_sentiment = entity["sentiment"]
        e_sentiment_type = e_sentiment["type"]
        if e_sentiment_type == 'neutral':
            continue
        e_sentiment_score = float(e_sentiment["score"])
        if e_text in entity_map:
            score = entity_map[e_text]
            if e_sentiment_score > score:
               entity_map[e_text] = e_sentiment_score
        else:
            entity_map[e_text] = e_sentiment_score 
    return entity_map
    
def convert_sentiment(entity_map):
    retStr1='<table align="center"><caption>Positive keywords</caption><th>Word</th><th>Sentiment</th>'
    retStr2='<table align="center"><caption>Negative keywords</caption><th>Word</th><th>Sentiment</th>'
    counter = 0 #used to limit to top 20 words
    done = False #flag to see whether 20 reached
    for e, v in entity_map.items():
        if counter >= 30: #once counter, met set flag and break
            done = True
            break
        if v >= 0:
            retStr1+='<tr>'
            retStr1+= '<td>'+str(e)+'</td>'+'<td>'+str(v)+'</td>'
            retStr1+='</tr>'
            counter += 1
        if v < 0:
            retStr2+='<tr>'
            retStr2+= '<td>'+str(e)+'</td>'+'<td>'+str(v)+'</td>'
            retStr2+='</tr>'
            counter += 1
    retStr1+= '</table>'
    retStr2+= '</table>'
    return retStr1 + '<br>' + retStr2

def allCount(screen_name): #list of all character counts (pearson)
    response = access(screen_name)
    charNums = []
    for t_tweet in response:
        t_text = t_tweet["text"]
        t_text = t_text.encode('ascii', 'ignore').decode('ascii') #converts all$
        t_text = t_text.lower()
        t_text = t_text.split("http")[0]
        if "rt" not in t_text:
            count = len(t_text)
        else:
            count = len(t_text) - 2 #get rid of offset that is 'rt', indicating$
        charNums.append(count)
    return charNums

def diversify(num, length): #so pearson isnt dividing by 0/returning isNan
    retL = [] #mean of list is same, just makes a standard deviation != 0
    if (length % 2 == 1):
        retL.append(num)
	theLen = 1
    else:
	theLen = 0
    while theLen < length:
	    retL.append(num-1)
	    retL.append(num+1)
    	    theLen = len(retL)
    return retL

def avgRT(screen_name):
    response = access(screen_name)
    RTs = []
    for t_tweet in response:
	RTs.append( t_tweet[u'retweet_count'])
    return sum(RTs)/len(response)

def allRT(screen_name):
    response = access(screen_name)
    RTs = []
    for t_tweet in response:
        RTs.append( t_tweet[u'retweet_count'])
    return RTs

def dataCorr(d1, d2, screen_name): #will be main function for correlation
    if d1 == "Retweets":
	d1 = allRT(screen_name)
	if d2 == "Followers":
	    d2 = diversify( followers(screen_name), len(d1))
	    retStr = "<h3>Correlation Coefficient (<i>r</i>) of Retweets and Followers: </h3>"
	    retStr += str( pearson(d1,d2))
	if d2 == "Retweets":
	    retStr = "You can't correlate Retweets with itself. Try again."
	if d2 == "charCnt":
	    d2 = allCount(screen_name)
	    retStr= "<h3>Correlation Coefficient (<i>r</i>) of Retweets and Average Character Count (of tweets): </h3>"
	    retStr+= str( pearson(d1, d2))
    elif d1 == "Followers":
	if d2 == "Retweets":
            d2 = allRT(screen_name)
            retStr= "<h3>Correlation Coefficient (<i>r</i>) of Followers and Retweets: </h3>"
	    d1 = diversify( followers(screen_name), len(d2))
	    retStr += str( pearson(d1, d2))
        if d2 == "Followers":
            retStr = "Can't correlate followers with itself."
        if d2 == "charCnt":
	    d2 = allCount(screen_name)
	    d1 = diversify( followers(screen_name), len(d2))
	    retStr = "<h3>Correlation Coefficient (<i>r</i>) of Followers and Average Character Count (of tweets): </h3>"
            retStr += str( pearson(d1, d2))
    elif d1 == "charCnt":
	d1 = allCount(screen_name)
	if d2 == "Retweets":
	    d2 = allRT(screen_name)
	    retStr = "<h3>Correlation Coefficient (<i>r</i>) of Average Character Count (of tweets) and Retweets: </h3>"
            retStr += str( pearson(d1, d2))
        if d2 == "charCnt":
            retStr = "You can't correlate Avg Character Count with itself. Try again."
        if d2 == "Followers":
	    d2 = diversify (followers(screen_name), len(d1))
	    retStr = "<h3>Correlation Coefficient (<i>r</i>) of Average Character Count (of tweets) and Followers: </h3>"
	    retStr += str( pearson(d1, d2))
    return retStr + '<br><br>' + corrShplain + '<br><br>'


#==================================================
# ~~~~~~~~~~~~~~~ main ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    inputs = FStoD()
    screen_name = inputs['handle']
    retStr = ""
    try:
        if 'commonWords' in inputs:
                retStr+= str(buzzwords(screen_name)) + "<br>"
        if 'followers' in inputs:
                retStr+= fols + str(followers(screen_name)) + "<br>"
        if 'charCount' in inputs:
                retStr+= cCount + str(avgCount(screen_name)) + "<br>"
        if 'retweets' in inputs:
                retStr+= rets + str(avgRT(screen_name)) + "</br>"
        if "first" in inputs and "second" in inputs:
                data1 = inputs['first']
                data2 = inputs['second']
                retStr+= dataCorr(data1, data2, screen_name)
        elif "first" in inputs or "second" in inputs:
                retStr = "You only entered one piece of data to correlate. Try again"
    except:
        retStr += "<h2><i>@" + screen_name + "</i> " + reject
    return retStr
    
print main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  

#------------- Closing Bookends -------------------
print '<h3>Wanna tweet-a-lyze someone else? Or maybe play with different options?<a href="index.html"> Click here to go back to the main page!</a></h3>'
print '</body>'
print '</div>'
print '</html>'
