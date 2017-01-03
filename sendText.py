from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "<your account sid id>" 
AUTH_TOKEN = "<your account tokent>" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to="+12897725600", 
    from_="+12048171105", 
    body="Hi, From Python twilio"
)