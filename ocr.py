#!/usr/bin/env python
import sys
import base64
import requests
import json


def getLatexString(dir):
# put desired file path here
    file_path = dir
    #print(base64.b64encode(open(file_path, "rb").read()))
    image_uri = "data:image/jpeg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()
    response = requests.post("https://api.mathpix.com/v3/latex",
    	data=json.dumps({'url': image_uri}),
    	headers={"app_id": "devminhhai_gmail_com", "app_key": "ceb7df5d2d13f08405f4",
            "Content-type": "application/json"})
    data = json.loads(response.text)
    print(data)
    print(data['latex'])
    return [data['latex']]
'''

file_path = "test.jpg"
image_uri = "data:image/jpeg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()
response = requests.post("https://api.mathpix.com/v3/latex",
	data=json.dumps({'url': image_uri}),
	headers={"app_id": "devminhhai_gmail_com", "app_key": "ceb7df5d2d13f08405f4",
        "Content-type": "application/json"})
data = json.loads(response.text)
print(data)
'''
