#!/bin/python3

import requests
import json
import re

#base_url = 'https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=pizza'

topic = 'pizza'
url = 'https://en.wikipedia.org/w/api.php?'
parameters = {
   'action': 'parse',
   'section': '0',
   'prop': 'text',
   'format': 'json',
   'page': topic
}

response = requests.get(url, params=parameters)

if response.ok:

   # Matches the task answer
   print (len(re.findall(topic, json.dumps(response.text))))

   # Case sensitive search
   #print (len(re.findall(topic, json.dumps(response.text), flags=re.IGNORECASE)))
