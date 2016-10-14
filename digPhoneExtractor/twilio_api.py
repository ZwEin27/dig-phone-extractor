# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-10-13 14:51:29
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-14 11:01:46

# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest.lookups import TwilioLookupsClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACb44ce674a411efd365e5fe344e20daea"
auth_token = "088e5197c15f18770d5dd185f532fdb2"
client = TwilioLookupsClient(account_sid, auth_token)
print repr(client)

def load_phone_number(phone_number):

    """ client.phone_numbers.get

    (check detail at https://github.com/twilio/twilio-python/blob/master/twilio/rest/resources/lookups/phone_numbers.py)

    return twilio.rest.resources.lookups.phone_numbers.PhoneNumber
    
    PhoneNumber Attributes:
    - phone_number: The phone number in normalized E.164 format, e.g. "+14158675309"
    - national_format: The phone number in localized format, e.g. "(415) 867-5309"
    - country_code: The ISO 3166-1 two-letter code for this phone number's country, e.g. "US" for United States
    - carrier: A dictionary of information about the carrier responsible for this
        number, if requested.Contains the following:

        - mobile_country_code: the country code of the mobile carrier.
        Only populated if the number is a mobile number.
        - mobile_network_code: the network code of the mobile carrier.
        Only populated if the number is a mobile number.
        - name: the name of the carrier.
        - type: the type of the number ("mobile", "landline", or "voip")
        - error_code: the error code of the carrier info request, if one
        occurred

    """
    number = client.phone_numbers.get(phone_number, include_carrier_info=True)

    ans = {}
    ans.setdefault('phone_number', number.phone_number)
    ans.setdefault('national_format', number.national_format)
    ans.setdefault('country_code', number.country_code)
    ans.setdefault('carrier', number.carrier)

    return ans

if __name__ == '__main__':
    phone_number = "+12133790692"
    print load_phone_number(phone_number)
