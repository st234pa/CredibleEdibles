import urllib2 




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
