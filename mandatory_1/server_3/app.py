from bottle import run, get, post, request
import pandas as pd
import requests
import json


# Helper func
def json_to_csv(json_data):
	headers = ""
	data = ""
	data_length = len(json_data["data"])

	i = 1
	for key in json_data["data"]:
		if(i < data_length):
			headers += str(key) + ','
			i += 1
		else:
			headers += str(key)

	headers += '\n'

	i = 1
	for key in json_data["data"]:
		if(i < data_length):
			data += json_data["data"][key] + ','
			i += 1
		else:
			data += json_data["data"][key]

	data += '\n'
	print(headers + data)
	return headers + data


@get("/")
def do():
  return "Welcome to System Integration mandatory 1 server 3!"


@post("/signup")
def do():
	print("Ping Server 3")
	URL = "http://127.0.0.1:1111/signup"
	HEADERS = {"Content-Type": "text/csv"}

	
	req = json.load(request.body)

	print("Server 3 - Json to csv")
	res = json_to_csv(req)

	try:
		res = requests.post(url=URL, headers=HEADERS, data=res)
		return 'Send csv formatted text data'
	except:
		return 'An error occurred'



############################ COMPANY
run(host="127.0.0.1", port=3333, debug=True, reloader=True)


