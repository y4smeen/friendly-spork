import httplib, urllib, base64  

# Image to analyse (body of the request)

body = {'url': 'http://grandmahenke.com/grandma/wp-content/uploads/2007/08/happy-anna.jpg'}

# API request for Emotion Detection

headers = {
   'Content-type': 'application/json',
}

params = urllib.urlencode({
    # Request headers
    'Content-Type': 'application/json',
    'subscription-key': '465712c1599e451296c9cd3bf720295e',
})

try:
   conn = httplib.HTTPSConnection('api.projectoxford.ai')
   conn.request("POST", "/emotion/v1.0/recognize?%s" % params, str(body) , headers)
   response = conn.getresponse()
   print("Send request")

   data = response.read()
   print(data)
   conn.close()
except:
     print "Unexpected error:", sys.exc_info()[0]
     raise

####################################
