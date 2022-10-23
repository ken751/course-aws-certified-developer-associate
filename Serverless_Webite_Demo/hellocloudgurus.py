def lambda_handler(event, context):
    print("In lambda handler")

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Keep being awesome Cloud Gurus!",
    }
