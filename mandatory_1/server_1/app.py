from bottle import run, get, post, request
import requests


# Get user form submission (email, name, password)
def get_user_form():
	print("*** Please fill out the sign up form ***")
	try:
		email = input("Enter your email: ")
		name = input("Enter your full name: ")
		password = input("Enter your password: ")
		
		return {"email": email, "name": name, "password": password}
	except:
		raise Exception("Only string values are allowed!!!")

# Creates an XML form out of the user input
def create_xml_form(user_form):
	try:
		xml_form = f"""<?xml version="1.0" encoding="UTF-8"?>
								<data>
									<email>{user_form["email"]}</email>
									<name>{user_form["name"]}</name>
									<password>{user_form["password"]}</password>
								</data>
							"""
		return xml_form
	except:
		raise Exception("Creation of xml form produced an error!!!")


# Sends XML form to a specified url
def send_xml_form():
	### Url to send request to with specified headers
	URL = "http://127.0.0.1:2222/signup"
	HEADERS = {"Content-Type": "application/xml"}

	### Create user form and create xml form template out of it
	user_form = get_user_form()
	xml_form = create_xml_form(user_form)
	print(xml_form)

	try:
		res = requests.post(url=URL, headers=HEADERS, data=xml_form)
		return res
	except:
		return 'Server 1 - An error occurred while attempting to POST a request!!!'

# Creates a user signup form and sends it to Server 2
@get("/signup")
def do():
	print("Server 1 - Send XML")
	xml_form = send_xml_form()
	print(xml_form)

# Receives the signup form as CSV
@post("/signup")
def do():
	print("Server 1 - Receive CSV")
	res = request.body
	print(res.read())
	return res

@get("/")
def do():
  return "Welcome to System Integration mandatory 1 server 1!"

############################ Server 1
run(host="127.0.0.1", port=1111, debug=False, reloader=True)


