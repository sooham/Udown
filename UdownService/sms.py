from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACc6ddee70e1d4f0e323614b1093968848"
auth_token = "ee55744af15af596f7be3b1e66fb5cb2"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+16478645896", from_="+1289 2120994", body="Hello there!")
