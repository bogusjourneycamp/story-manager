import json


def response(message, status_code):
    return {
        "statusCode": str(status_code),
        "body": json.dumps(message),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "https://nervous-blackwell-595d82.netlify.app",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Methods": "GET,OPTIONS,POST",
        },
    }
