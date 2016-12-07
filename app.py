from flask import Flask, render_template, request, url_for, session, redirect
#from flask_bootstrap import Bootstrap

#import os
#import utils.googlemaps
import utils.yelp
#import utils.mapbox


app = Flask(__name__)
#Bootstrap(app)

#app.secret_key = os.urandom(10)



@app.route("/")
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
    businessList = utils.yelp.makeBusinessesList(rating,distance,40.7179460,-74.0139050)
    jsList = utils.yelp.makeJsList(businessList)
    #print price
    #return render_template('results.html', jsList=jsList,businessList=businessList)
    return render_template('results.html',jsList=jsList,businessList=businessList)


def getDis(data):
    if 'birdseye' in data:
        distance=50
    elif 'fourblocks' in data:
        distance=400
    elif 'walking' in data:
        distance=800
    elif 'driving' in data:
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
    if 'onestar' in data:
        qual=1
    elif 'twostar' in data:
        qual = 2
    elif 'threestar' in data:
        qual = 3
    elif 'fourstar' in data:
        qual = 4
    elif 'fivestar' in data:
        qual = 5
    return qual

def getAddress(data):
    address=''
    if 'usecurrentloc' in data:
        #address=utils.googlemaps.locate()
        print 'placeholder'
    else:
        address=data['address']
    return address
    
			



if(__name__ == "__main__"):
    app.debug = True
    app.run();
