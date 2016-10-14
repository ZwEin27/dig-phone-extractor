# """
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest.lookups import TwilioLookupsClient

try:
    # Python 3
    from urllib.parse import quote
except ImportError:
    # Python 2
    from urllib import quote

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACb44ce674a411efd365e5fe344e20daea"
auth_token = "088e5197c15f18770d5dd185f532fdb2"
client = TwilioLookupsClient(account_sid, auth_token)

# number = client.phone_numbers.get("+16502530000")

number = client.phone_numbers.get("+12133790691", include_carrier_info=True, add_on='whitepages_pro_caller_id')
print number.carrier
# print(number.carrier['type'])
# print(number.carrier['name'])

# """

"""
import twilio
client = twilio.rest.Client(username="ACb44ce674a411efd365e5fe344e20daea", password="088e5197c15f18770d5dd185f532fdb2")
ph = client.lookups.phone_numbers("+16502530000").fetch(add_ons="payfone_tcpa_compliance",add_ons_data={"payfone_tcpa_compliance.RightPartyContactedDate":"20160101"})
print(ph.add_ons)
"""

# https://www.twilio.com/blog/2016/02/how-to-verify-phone-numbers-in-python-with-the-twilio-lookup-api.html
