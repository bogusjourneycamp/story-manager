import boto3
import json
from tree.TreeValidator import TreeValidator

def create_story(event, context):
    if "body" not in event:
        return {
            "statusCode": 400,
            "body": json.dumps("No body passed in event")
        }
    
    tree = json.loads(event["body"])
    
    (is_valid, reason) = TreeValidator().check_tree_validity(tree)
    
    if not is_valid:
        return {
            "statusCode": 400,
            "body": json.dumps(f"Invalid body passed. Reason: {reason}")
        }

    stories = boto3.resource('dynamodb').Table('Stories')
    stories.put_item(Item=tree)
    
    return {
        "statusCode": 200
    }
