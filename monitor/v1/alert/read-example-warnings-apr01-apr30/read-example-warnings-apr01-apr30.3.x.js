// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// DANGER! This is insecure. See http://twil.io/secure
const accountSid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.monitor.alerts
              .list({
                 endDate: new Date(Date.UTC(2015, 3, 30)),
                 logLevel: 'warning',
                 startDate: new Date(Date.UTC(2015, 3, 1))
               })
              .then(alerts => console.log(alerts.sid));
