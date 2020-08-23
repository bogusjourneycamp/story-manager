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
            f"Found improperly formatted location. Expecting url like /story/A_1:15. Reason: {reason}",
            400,
        )

    if "body" not in event:
        return response("No body passed in event", 400)

    if "passphrase" not in event["body"]:
        return response("No passphrase passed", 400)

    passed_passphrase = json.loads(event["body"])["passphrase"]

    story_table = boto3.resource("dynamodb").Table("story-manager-dev")

    res = story_table.query(
        ProjectionExpression="#loc",
        ExpressionAttributeNames={"#loc": "location"},
        KeyConditionExpression=Key("location").eq(story_tree["location"])
    )

    if len(res["Items"]) == 0:
        return response(True, 200) # If no story here, no password necessary

    found_story = res["Items"][0]

    if "passphrase" in found_story:
        return response(found_story["passphrase"] == passed_pasphrase, 200)
    else:
        return response(True, 200) # If no passphrase value, assume it's the correct password
