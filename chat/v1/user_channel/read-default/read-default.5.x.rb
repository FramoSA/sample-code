# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

user_channels = @client.chat
                       .v1
                       .services('ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                       .users('USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                       .user_channels
                       .list(limit: 20)

user_channels.each do |record|
  puts record.service_sid
end
