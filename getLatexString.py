#!/usr/bin/env python
import sys
import base64
import requests
import json

<<<<<<< HEAD
def getLatexString(dir):
# put desired file path here
	image_uri = dir
=======

def getLatexString(dir):
# put desired file path here
	file_path = dir
	image_uri = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read())
>>>>>>> refs/remotes/origin/master
	response = requests.post("https://api.mathpix.com/v3/latex",
    	data=json.dumps({'src': image_uri}),
    	headers={"app_id": "devminhhai_gmail_com", "app_key": "ceb7df5d2d13f08405f4",
            "Content-type": "application/json"})
	data = json.loads(response.text)
	print data['latex']
	return [data['latex']]
<<<<<<< HEAD
=======



>>>>>>> refs/remotes/origin/master
