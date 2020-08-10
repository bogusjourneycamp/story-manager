import boto3
import random
from story_manager.location_validator import LocationValidator
from story_manager.response import response


def get(event, context):
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

    story_table = boto3.resource("dynamodb").Table("story-manager-dev")

    if location.lower() == "random":
        scan_kwargs = {
            "ExpressionAttributeNames": {"#loc": "location"},
            "ProjectionExpression": "#loc"
        }
        story_locations = story_table.scan(**scan_kwargs).get('Items', [])
        location = random.choice(story_locations)['location']

    story = story_table.get_item(Key={"location": location}).get("Item", {})

    return response(story, 200)
