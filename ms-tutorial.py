########### Python 2.7 #############
import httplib, urllib, base64

body = {'url': 'http://grandmahenke.com/grandma/wp-content/uploads/2007/08/happy-anna.jpg'}

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '465712c1599e451296c9cd3bf720295e',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
