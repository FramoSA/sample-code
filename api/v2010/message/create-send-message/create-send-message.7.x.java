// Install the Java helper library from twilio.com/docs/java/install

import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;

import java.net.URI;
import java.util.Arrays;

public class Example {
    // Find your Account Sid and Token at twilio.com/console
    // DANGER! This is insecure. See http://twil.io/secure
    public static final String ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    public static final String AUTH_TOKEN = "your_auth_token";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
        Message message = Message.creator(
                new com.twilio.type.PhoneNumber("+15558675310"),
                new com.twilio.type.PhoneNumber("+15017122661"),
                "This is the ship that made the Kessel Run in fourteen parsecs?")
            .setMediaUrl(
                Arrays.asList(URI.create("https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg")))
            .create();

        System.out.println(message.getSid());
    }
}