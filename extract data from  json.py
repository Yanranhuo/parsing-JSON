#Extracting Data from JSON

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract 
#the comment counts from the JSON data


import urllib.request, urllib.parse, urllib.error
import json


sum = 0
url = input('Enter location: ')
if len(url)<1:
	url = 'http://py4e-data.dr-chuck.net/comments_42.json'
#url = urllib.parse.urlencode({'address': address})
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
print('Retrieved', len(data), 'characters')
for comment in info['comments']:
	sum = sum + int(comment['count'])
print(sum)
       

    
