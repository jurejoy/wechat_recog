# -*- coding: utf-8 -*-

########### Python 2.7 #############
import httplib, urllib, base64, json
import os,sys


# Replace the subscription_key string value with your valid subscription key.
subscription_key = '1aeaf4a5de9c4d828c0ff823b5899074'

params = urllib.urlencode({
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
})

    #specify image from file

    #For a local image, Content-Type should be application/octet-stream or multipart/form-data AND JSON SHOULD BE EMPTY

headers = {

    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

body = "" 

    #load image

filename = 'C:/avatar.JPG'

with open(filename, "rb") as f:
    body = f.read()


try: 
    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')

    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)

    response = conn.getresponse()

    data = response.read()
    
    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    emotion = ""
    for item in parsed:
        for key in item:
            for key1 in item[key]:
                if key1 == "emotion":
                    for key2 in item[key][key1]:
                        if key2 == "happiness":
                            emotion = item[key][key1][key2]
                            print(emotion)
        if emotion > 0.5:
            mood = 'happy'
        else:
            mood = 'flat'

        print(mood)

    conn.close()

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))