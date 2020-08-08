import boto3
import json
from story.tree_validator import TreeValidator
from story.response import response


def create(event, context):
    if "body" not in event:
        return response("No body passed in event", 400)

    tree = json.loads(event["body"])

    (is_valid, reason) = TreeValidator().check_tree_validity(tree)

    if not is_valid:
        return response(f"Invalid body passed. Reason: {reason}", 400)

    story_table = boto3.resource("dynamodb").Table("story-manager-dev")
    story_table.put_item(Item=tree)

    return response("", 200)
