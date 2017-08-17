# parsing-JSON

import json

input = '''
[
#this kind of bracket is a list,{ this is a dict[]
  {"id" : "001",
    "x" : "2",
    "name" : " chuck"
   },
   {"id" : "009",
    "x" : "7",
    "name" : " chuck"
   }
  ]'''
  
  info = json.load(input)
  #in this case, info is a list
  print('user count:',len(info))
  # we got two dict() and one list
  
  for item in info:
      print('name', item['name'])
      print('id',item['id'])
      print('attribute',item['x'])
    
