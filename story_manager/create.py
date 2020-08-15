import json

import boto3

from utils.diceware import generate_passphrase
from utils.response import response
from utils.tree_validator import TreeValidator


def create(event, context):
    print("Event", event)
    if "body" not in event:
        return response("No body passed in event", 400)

    story_tree = json.loads(event["body"])
    print("Found body", story_tree)

    (is_valid, reason) = TreeValidator().check_tree_validity(story_tree)

    if not is_valid:
        print("Invalid body")
        return response(f"Invalid body passed. Reason: {reason}", 400)

    print("Valid body")

    res = story_table.query(
        ProjectionExpression="#loc",
        ExpressionAttributeNames={"#loc": "location"},
        KeyConditionExpression=Key("location").eq(story_tree["location"])
    )

    if len(res["Items"]) != 0:
        print("Found existing item")
        return response("Used create endpoint - should have used update", 400)

    story_tree["passphrase"] = generate_passphrase(4)

    story_table = boto3.resource("dynamodb").Table("story-manager-dev")
    story_table.put_item(Item=story_tree)

    return response(story_tree["passphrase"], 200)
