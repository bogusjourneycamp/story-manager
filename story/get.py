import boto3
import json
from story.location_validator import LocationValidator

def get(event, context):
    if "pathParameters" not in event:
        return {
            "statusCode": 400,
            "body": json.dumps("No pathParameters found in event")
        }
        
    if "location" not in event["pathParameters"]:
        return {
            "statusCode": 400,
            "body": json.dumps("No location found in pathParameters")
        }

    location = event['pathParameters']["location"]

    (is_valid_location, reason) = LocationValidator().check_location_validity(location)

    if not is_valid_location:
        return {
            "statusCode": 400,
            "body": json.dumps(f"Found improperly formatted location. Expecting url like /story?location=A_1:15. Reason: {reason}")
        }

    story_table = boto3.resource('dynamodb').Table('Stories')
    story = story_table.get_item(Key={"location": location}).get("Item", {})
    
    return {
        "statusCode": 200,
        "body": json.dumps(story)
    }
