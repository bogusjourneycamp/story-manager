import json
import random

import boto3
from boto3.dynamodb.conditions import Key

from utils.response import response


def wander(event, context):
    story_table = boto3.resource("dynamodb").Table("story-manager-dev")

    items = story_table.scan(
        ProjectionExpression="#loc",
        ExpressionAttributeNames={"#loc": "location"}
    )["Items"]

    choice = random.choice(itemKeys)

    return response(choice["location"], 200)
