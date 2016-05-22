import urllib2, time, json
from flask import Flask, render_template, request, jsonify
from ast import literal_eval
import httplib, urllib, base64
import numpy as np


def primaryEmotion( data ):
    r = json.loads(data)
    l = r[0]["scores"]
    # print "list: " + str(l)
    keys = l.keys()
    # print 'unicode keys: ' + str(keys)
    # [x.encode('UTF8') for x in keys]
    keys = map(str, keys)
    # print 'string keys: ' + str(keys)
    # count = 0
    # for i in keys:
    #     keys[count] = str(i)
    #     count += 1
    # print "emotions: " + keys
    values = l.values()
    print "values: " + str(values)
    print "max value: " + str(max(values))
    print "index: " + str(values.index(max(values)))
    print "emotion: " + keys[values.index(max(values))]
    emotion = keys[values.index(max(values))]
    # print type(new_list[0])
    # return keys.index(max(values))
    return emotion
    #return max(l, key=lambda i: l[i])

def getLink():
    # Load an image
    #img = cv2.imread('picture.jpg')
    #print img

    with open('uploads/picture.jpg', 'rb') as f:
        data = f.read()
    #print data
    img=data
    #with open('picture_out.jpg', 'wb') as f:
    #    f.write(data)



    ret = []




    #URL = 'http://grandmahenke.com/grandma/wp-content/uploads/2007/08/happy-anna.jpg'

    # Image to analyse (body of the request)

    #body = {'url': URL}
    body = img

    # API request for Emotion Detection

    headers = {
        #'Content-type': 'application/json',
        'Content-type': 'application/octet-stream',
    }

    params = urllib.urlencode({
        # Request headers
        'Content-Type': 'application/json',
        'subscription-key': '6f89e0a43e694c6cb72750d82a24e0f5',
    })

    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, str(body) , headers)
        response = conn.getresponse()
        #print("Send request")

        data = response.read()
        ret = data
        conn.close()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise



    emotion = primaryEmotion(data) #CHANGE THE EMOTION HERE

    print "EMOTION: "+emotion
    endpoint = "https://api.spotify.com/v1/search?q="+emotion+"&type=playlist"

    request = urllib2.urlopen(endpoint)
    result = request.read()
    r = json.loads(result)
    #print r
    print r["playlists"]["items"][0]["external_urls"]["spotify"]
    return r["playlists"]["items"][0]["external_urls"]["spotify"]


def getEmotion():
    # Load an image
    #img = cv2.imread('picture.jpg')
    #print img

    with open('uploads/picture.jpg', 'rb') as f:
        data = f.read()
    #print data
    img=data
    #with open('picture_out.jpg', 'wb') as f:
    #    f.write(data)



    ret = []




    #URL = 'http://grandmahenke.com/grandma/wp-content/uploads/2007/08/happy-anna.jpg'

    # Image to analyse (body of the request)

    #body = {'url': URL}
    body = img

    # API request for Emotion Detection

    headers = {
        #'Content-type': 'application/json',
        'Content-type': 'application/octet-stream',
    }

    params = urllib.urlencode({
        # Request headers
        'Content-Type': 'application/json',
        'subscription-key': '6f89e0a43e694c6cb72750d82a24e0f5',
    })

    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/emotion/v1.0/recognize?%s" % params, str(body) , headers)
        response = conn.getresponse()
        #print("Send request")

        data = response.read()
        ret = data
        conn.close()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise



    emotion = primaryEmotion(data) #CHANGE THE EMOTION HERE
    return emotion
