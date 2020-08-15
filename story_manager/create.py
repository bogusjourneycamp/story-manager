import json

import boto3

from utils.diceware import generate_passphrase
from utils.response import response
from utils.tree_validator import TreeValidator


def create(event, context):
    if "body" not in event:
        return response("No body passed in event", 400)

    story_tree = json.loads(event["body"])

    (is_valid, reason) = TreeValidator().check_tree_validity(story_tree)

    if not is_valid:
        return response(f"Invalid body passed. Reason: {reason}", 400)

    story_tree["passphrase"] = generate_passphrase(4)

    story_table = boto3.resource("dynamodb").Table("story-manager-dev")
    story_table.put_item(
        Item=story_tree,
        ExpressionAttributeNames={"#nam": "name", "#loc": "location"},
        ConditionExpression="attribute_not_exists(location)"
    )

    return response(story_tree["passphrase"], 200)
