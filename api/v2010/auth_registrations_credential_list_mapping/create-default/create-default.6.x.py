# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

auth_registrations_credential_list_mapping = client.sip \
    .domains('SDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
    .auth \
    .registrations \
    .credential_list_mappings \
    .create(credential_list_sid='CLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print(auth_registrations_credential_list_mapping.sid)
