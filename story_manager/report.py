import json

import boto3
from botocore.exceptions import ClientError

from utils.location_validator import LocationValidator
from utils.response import response

# SENDER = "charliesummers@gmail.com"
# RECIPIENT = "charliesummers@gmail.com"
SENDER = "scott.snelgrove1@gmail.com"
RECIPIENT = "scott.snelgrove1@gmail.com"
AWS_REGION = "us-west-2"
SUBJECT = "Amazon SES Test"
BODY_TEXT = ("This is a test")
CHARSET = "UTF-8"
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-python/'>
      AWS SDK for Python (Boto)</a>.</p>
</body>
</html>
            """            

def report(event, context):
    print("Event", event)

    # if "body" not in event:
    #     return response("No body passed in event", 400)

    # report_info = json.loads(event["body"])

    if "pathParameters" not in event:
        return response("No location found in pathParameters", 400)

    location = event["pathParameters"]["location"]

    (is_valid_location, reason) = LocationValidator(
    ).check_location_validity(location)

    if not is_valid_location:
        return response(
            f"Found improperly formatted location. Expecting url like /story/A_1:15. Reason: {reason}",
            400
        )
    
    client = boto3.client('ses')
    try:
        response = client.send_email(
            Destination={
                'ToAddresses':[
                    RECIPIENT
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])