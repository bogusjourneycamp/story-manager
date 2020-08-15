import json

import boto3
from boto3.dynamodb.conditions import Key

from utils.diceware import generate_passphrase
from utils.response import response
from utils.tree_validator import TreeValidator


def update(event, context):
    if "body" not in event:
        return response("No body passed in event", 400)

    story_tree = json.loads(event["body"])

    (is_valid, reason) = TreeValidator().check_tree_validity(story_tree)

    if not is_valid:
        return response(f"Invalid body passed. Reason: {reason}", 400)

    story_table = boto3.resource("dynamodb").Table("story-manager-dev")

    response = story_table.query(
        ProjectionExpression="#loc, passphrase",
        ExpressionAttributeNames={"#loc": "location"},
        KeyConditionExpression=Key("location").eq(story_tree["location"])
        & Key("passphrase").eq(story_tree["passphrase"]),
    )

    if len(response["Items"]) == 0:
        return response(f"Unable to find story or validate passphrase to edit at location: {story_tree['location']}", 400)

    story_table.put_item(Item=story_tree)

    return response("Successfully updated story at location: {story_tree['location']}", 200)
