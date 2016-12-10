def getkeydict():
    f = open("../keys.txt", r)
    listkeys = f.readlines()
    #-----List ordering-----
    #0. Yelp consumer_key
    #1. Yelp consumer_secret
    #2. Yelp token
    #3. Yelp token_secret
    #4. Mapbox access_token
    #5. Googlemaps key
    #-----------------------
    d = {'yelp_consumer_key': listkeys[0], 'yelp_consumer_secret': listkeys[1], 'yelp_token': listkeys[2], 'yelp_token_secret': listkeys[3], 'mapbox_access_token': listkeys[4], 'googlemaps_key': listkeys[5]}
    return d
