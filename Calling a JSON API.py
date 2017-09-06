# parsing-JSON
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. 
#The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
#and retrieve the first place_id from the JSON.A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json


# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'


while True:
    address =input('Enter location: ')
    if len(address) < 1 :
        address = 'South Federal University'

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})
    print('Retrieving',url)
	
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')

    try: js = json.loads(str(data))
    except: js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print json.dumps(js, isndent=4)

    print(js['results'][0]['place_id'])
