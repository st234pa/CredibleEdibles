# CredibleEdibles
by LipgLOSSisPoppin


## What does it do?

Credible Edibles will take in an address or the user’s location, as well as their preferences for prices/distance/ratings, and create a map of restaurants near them that match their input as closely as possible with the addresses and ratings of the restaurants listed below. The project would use the Yelp, Mapbox, and Google Maps APIs.

## How do you use it?

Clone the repo, locally add the text file with the API keys to the root. Make sure flask, rauth, key, urllib, urllib2, json, sys, cgi, and request is installed, and then run app.py!

### The homepage

Fill out the form to indicate your preferences for restaurants.
For the first question, either select "Use my current location" or "Enter an address." If you select the latter, make sure to enter a complete address. Here is an example of a valid address:

345 Chambers St, New York, NY 10282

For the second question (regarding distance), selecting a radius (for example, "walking distance") will filter the results to include restaurants that are within the radius.
For the third question (regarding ratings), selecting a rating (for example, "edible") will filter the results to include restaurants with that rating or higher.

### The results

After your submit your response to the form, Credible Edibles will render a map displaying up to 10 features, which will also be listed below with the corresponding ratings and addresses. (If there are no results that match your form response, no features will show up on the map, and no entries will show up on the list.)
