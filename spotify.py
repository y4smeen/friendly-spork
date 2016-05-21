emotion = "happy" #CHANGE THE EMOTION HERE

endpoint = "https://api.spotify.com/v1/search?q="+emotion+"&type=playlist"

import urllib2, time, json
from flask import Flask, render_template, request, jsonify
from ast import literal_eval

request = urllib2.urlopen(endpoint)
result = request.read()
r = json.loads(result)
print r

