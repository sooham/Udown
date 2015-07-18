import requests, json

url = 'http://localhost:8000/api/v1/user/'

def signup(name, password):
	headers = {'content-type': 'application/json'}
	payload = {
			'type': 'register',
			'username': name,
			'password1': password,
			'password2': password,
			#'email': 'jq.yang@berkeley.edu',
			#'more_fields': 'your value'
		}
	return requests.post(
		url,
		data=json.dumps(payload),
		headers=headers
	)