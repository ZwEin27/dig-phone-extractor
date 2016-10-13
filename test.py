# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest.lookups import TwilioLookupsClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACb44ce674a411efd365e5fe344e20daea"
auth_token = "088e5197c15f18770d5dd185f532fdb2"
client = TwilioLookupsClient(account_sid, auth_token)

number = client.phone_numbers.get("+1213379069181", include_carrier_info=True)
print(number.carrier['type'])
print(number.carrier['name'])