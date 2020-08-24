import json
import random

import boto3
from boto3.dynamodb.conditions import Key

from utils.response import response


def wander(event, context):
    story_table = boto3.resource("dynamodb").Table("story-manager-dev")

    itemKeys = story_table.scan(
        ProjectionExpression="#loc",
        ExpressionAttributeNames={"#loc": "location"}
    )["Items"]

    choiceKey = random.choice(itemKeys)

    print(choiceKey)    

    selected_story = story_table.get_item(Key=choiceKey)["Item"]

    print(selected_story)

    return response(selected_story, 200)
