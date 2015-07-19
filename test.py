import requests, json

url = 'http://localhost:8000/api/v1/user/'

client_id = 'r1oBSwzAR2XB2oJD9dkVufpMJhAyjG8yo52qWDKq'
client_secret = '73RvpJUjqVFBcMKG7LZRcuVj6T0hDSbzpEUGUAn9E3MHyEfdYz37jvslZfNIrOhPsXkepTlmf1bj9IncYwzIy6qPV8sYQKCnXVubXLHtV5p75552SZGT4umqiPGlmSfu'

def signup(name, email, password):
	headers = {'content-type': 'application/json'}
	payload = {
			'type': 'register',
			'username': name,
			'email': email,
			'password1': password,
			'password2': password,
		}
	return requests.post(
		url,
		data=json.dumps(payload),
		headers=headers
	)

def login(name, password):
	headers = {'content-type': 'application/json'}
	payload = {
		'type': 'login',
		'username': name,
		'password': password,
	}
	return requests.post(
		url,
		data=json.dumps(payload),
		headers=headers
	)

def get_token(username, password):
	headers = {'content-type': 'application/json'}
	payload = {
        'grant_type': 'password',
        'username': username,
        'password': password,
        'client_id': client_id,
        'client_secret': client_secret,
    }
	return requests.post(
		url="http://localhost:8000/o/token/",
		data=payload,
		#headers=headers
	)

def create_group(token):
	headers = {'content-type': 'application/json'}
	if token != None:
		data = {
			'oauth_consumer_key': token,
		}
	else:
		data = None
	return requests.post(
		url="http://localhost:8000/api/v1/study_group/",
		headers=headers,
		params=data,
		data=json.dumps({
				'type': "create",
				'description': "LOL",
			})
	)