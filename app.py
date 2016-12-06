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


			



if(__name__ == "__main__"):
    app.debug = True
    app.run();
