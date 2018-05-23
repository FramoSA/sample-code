<?php

// Update the path below to your autoload.php,
// see https://getcomposer.org/doc/01-basic-usage.md
require_once '/path/to/vendor/autoload.php';

use Twilio\Rest\Client;

// Your Account Sid and Auth Token from twilio.com/console
$sid    = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
$token  = "your_auth_token";
$twilio = new Client($sid, $token);

$sync_stream = $twilio->sync->v1->services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                                ->syncStreams("TOXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                                ->update(array("ttl" => 1));

print($sync_stream->uniqueName);