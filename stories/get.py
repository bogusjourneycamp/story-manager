import boto3
import json
from location_validator import LocationValidator

def get(event, context):
    if "queryStringParameters" not in event:
        return {
            "statusCode": 400,
            "body": json.dumps("No queryStringParameters found in event")
        }
        
    if "location" not in event["queryStringParameters"]:
        return {
            "statusCode": 400,
            "body": json.dumps("No location found in queryStringParameters")
        }

    location = event['pathParameters']["location"]

    (is_valid_location, reason) = LocationValidator().check_location_validity(location)

    if not is_valid_location:
        return {
            "statusCode": 400,
            "body": json.dumps(f"Found improperly formatted location. Expecting url like /story?location=A_1:15. Reason: {reason}")
        }

    stories = boto3.resource('dynamodb').Table('Stories')
    story = stories.get_item(Key={"location": location}).get("Item", {})
    
    return {
        "statusCode": 200,
        "body": json.dumps(story)
    }
