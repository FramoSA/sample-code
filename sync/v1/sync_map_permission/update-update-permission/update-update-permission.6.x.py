# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

sync_map_permission = client.sync \
<<<<<<< Updated upstream
                            .services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                            .sync_maps("MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                            .sync_map_permissions("bob") \
                            .update(manage=True, read=False, write=False)
=======
                            .services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                            .sync_maps('MPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
                            .sync_map_permissions('bob') \
                            .update(read=False, write=False, manage=False)
>>>>>>> Stashed changes

print(sync_map_permission.service_sid)
