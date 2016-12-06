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
def geocode(address):
    
