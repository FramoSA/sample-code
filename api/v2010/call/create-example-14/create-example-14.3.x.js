// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// DANGER! This is insecure. See http://twil.io/secure
const accountSid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.calls
      .create({
         method: 'GET',
         statusCallback: 'https://www.myapp.com/events',
         statusCallbackMethod: 'POST',
         url: 'http://demo.twilio.com/docs/voice.xml',
         to: '+14155551212',
         from: '+18668675310'
       })
      .then(call => console.log(call.sid));
