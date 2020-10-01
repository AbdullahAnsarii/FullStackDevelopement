from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe88a10aa66484512ccd7a0b2c389534f"
# Your Auth Token from twilio.com/console
auth_token  = "e83461ee0585de1430a2f747814675e8"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+923162153041", 
    from_="+12056229884",
    body="Abdullah loves to code!")

print(message.sid)
