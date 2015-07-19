import requests, json

url = 'http://localhost:8000/api/v1/user/'

client_id = '7DCvXFjeXT7px5ojxVtWWYp5IJMwFBQqya53tMR8'
client_secret = 'V3XPbQ8EzQt98ORsLxEAhETQql2yorkYSC9dkrNUSzNNYumq7VQLLCLSw383Zy5v3k8AmMZKhS7g1XSKcirPLMHXPIDkaEKNeLFbvDIwHJ6ClCvmQQ3y49XRcqg6dKTu'

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
		url="http://localhost:8000/api/v1/study_group/",
		headers=headers,
		params=data,
		data=json.dumps({
				'type': "get_user_groups",
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

t = get_token('a', '1234')
token = eval(t.content)['access_token']