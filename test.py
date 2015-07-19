import requests, json

url = 'http://localhost:8000/api/v1/user/'

client_id = 'KnFuX8NUWSupmktwLogNPKxCXScCXAMVhTOw9Nh9'
client_secret = 'SMLGxyR6GzLsaccIiS8DMeA3fWFkB4f6am6Oce0LKcPnIoUW54zSzFwS7U5UWn3Q7MOYHsNnVzVe0PyzpR8Fb4vJNUdWwj3t1LveCARcJEPl8mN9BpyRKPT8qgBlLSMU'

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

def get_user_groups(token):
	headers = {'content-type': 'application/json'}
	if token != None:
		data = {
			'oauth_consumer_key': token,
		}
	else:
		data = None
	return requests.post(
		url="http://localhost:8000/api/v1/user/",
		headers=headers,
		params=data,
		data=json.dumps({
				'type': "get_groups",
			})
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

def quit_group(token, id):
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
				'type': "quit_group",
				'id': id,
			})
	)

def set_gis(token, longitude, latitude):
	headers = {'content-type': 'application/json'}
	if token != None:
		data = {
			'oauth_consumer_key': token,
		}
	else:
		data = None
	return requests.post(
		url="http://localhost:8000/api/v1/user/",
		headers=headers,
		params=data,
		data=json.dumps({
				'type': "set_gis",
				'longitude': longitude,
				'latitude': latitude,
			})
	)

def delete_group(token, id):
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
				'type': "delete",
				'id': id,
			})
	)

def add_to_group(token, id):
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
				'type': "add_to_group",
				'id': id,
			})
	)

def invite_to_group(token, id):
	pass

t = get_token('a', '1234')
token = eval(t.content)['access_token']