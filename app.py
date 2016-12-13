#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for
#from flask_bootstrap import Bootstrap

#import os
import utils.googlemaps
#from utils import yelp
import utils.geomapbox
import utils.yelp
app = Flask(__name__)
#Bootstrap(app)

#app.secret_key = os.urandom(10)


@app.route("/")
@app.route("/homepage/")
def main():
    return render_template('homepage.html')


@app.route("/results/", methods=['POST'])
def results():
    print request.form
    distance = getDis(request.form)
    #price = getPrice(request.form)
    rating = getRating(request.form)
    address = getAddress(request.form)
    print rating
    print distance
    loc=[]
    loc.append(address[1])
    loc.append(address[0])
    businessList = utils.yelp.makeBusinessesList(rating,distance,address[0],address[1],["food","restaurant"])
    jsList = utils.yelp.makeJsList(businessList)
    print address
    mapbox_accessToken = utils.geomapbox.getToken()
    return render_template('results.html',jsList=jsList,businessList=businessList,loc=loc, mapbox_accessToken=mapbox_accessToken)


def getDis(data):
    distance=50
    if data["dist"] == 'birdseye':
        distance=50
    elif data["dist"] == 'fourblocks':
        distance=400
    elif data["dist"] == 'walking':
        distance=800
    elif data["dist"] == 'driving':
        distance=2000
    return distance

'''def getPrice(data):
    if 'steal' in data:
        price='steal'
    elif 'cheap' in data:
        price='cheap'
    elif 'pricey' in data:
        price='pricey'
    elif 'bougie' in data:
        price='bougie'
    return price
'''
def getRating(data):
    qual=1
    if data["qual"] == 'onestar':
        qual=1
    elif data["qual"] == 'twostar':
        qual = 2
    elif data["qual"] == 'threestar':
        qual = 3
    elif data["qual"] == 'fourstar':
        qual = 4
    elif data["qual"] == 'fivestar':
        qual = 5
    return qual

def getAddress(data):
    address=[]
    if data["cur_or_addr"] == 'yes':
        address=utils.googlemaps.locate()
    else:
        address=utils.geomapbox.geocode(data['address'])
        newadd=[]
        newadd.append(address[1])
        newadd.append(address[0])
        return newadd
    return address
    
			



if(__name__ == "__main__"):
    app.debug = True
    app.run();
