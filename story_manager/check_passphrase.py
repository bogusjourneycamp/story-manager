import json

import boto3
from boto3.dynamodb.conditions import Key

from utils.location_validator import LocationValidator
from utils.response import response


def check_passphrase(event, context):
    print("Event", event)

    if "pathParameters" not in event:
        return response("No pathParameters found in event", 400)

    if "location" not in event["pathParameters"]:
        return response("No location found in pathParameters", 400)

    location = event["pathParameters"]["location"]

    (is_valid_location, reason) = LocationValidator(
    ).check_location_validity(location)

    if not is_valid_location:
        return response(
            f"Found improperly formatted location. Expecting url like /story/check_passphrase/A_1:15. Reason: {reason}",
            400,
        )

    if "body" not in event:
        return response("No body passed in event", 400)

    if "passphrase" not in event["body"]:
        return response("No passphrase passed", 400)

    passed_passphrase = json.loads(event["body"])["passphrase"]

    story_table = boto3.resource("dynamodb").Table("story-manager-dev")

    print(location)

    found_story = story_table.get_item(Key={"location": location}).get("Item", {})

    print(found_story)

    if found_story == {}:
        print("No item found - no password required!")
        return response(True, 200) # If no story here, no password necessary

    if "passphrase" in found_story:
        print("Found passphrase, returning if same")
        return response(found_story["passphrase"] == passed_passphrase, 200)
    else:
        print("Found no passphrase in item - break open")
        return response(True, 200) # If no passphrase value, assume it's the correct password
