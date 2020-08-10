import boto3
from utils.location_validator import LocationValidator
from utils.response import response


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
    story = story_table.get_item(Key={"location": location}).get("Item", {})

    return response(story, 200)
