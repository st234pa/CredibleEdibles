from flask import Flask, render_template, request, url_for, session, redirect
import os
import utils.googlemaps
import utils.yelp
import utils.mapbox
import hashlib


app = Flask(__name__)
app.secret_key = os.urandom(10)



@app.route("/")
def main():
    return render_template('homepage.html')


@app.route("/results/", methods=['POST'])
def results():
    print request.form
    distance = getDis(request.form)
    price = getPrice(request.form)
    rating = getRating(request.form)
    return render_template('results.html')


def getDis(data):
    if 'birdseye' in data:
        distance='birdseye'
    elif 'fourblocks' in data:
        distance='fourblocks'
    elif 'walking' in data:
        distance='walking'
    elif 'driving' in data:
        distance='driving' 
    return distance

def getPrice(data):
    if 'steal' in data:
        price='steal'
    elif 'cheap' in data:
        price='cheap'
    elif 'pricey' in data:
        price='pricey'
    elif 'bougie' in data:
        price='bougie'
    return price

def getRating(data):
    if 'onestar' in data:
        qual='onestar'
    elif 'twostar' in data:
        qual = 'twostar'
    elif 'threestar' in data:
        qual = 'threestar'
    elif 'fourstar' in data:
        qual = 'fourstar'
    elif 'fivestar' in data:
        qual = 'fivestar'





if(__name__ == "__main__"):
    app.debug = True
    app.run();
