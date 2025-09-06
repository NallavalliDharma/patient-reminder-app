import json
import boto3

sf = boto3.client('stepfunctions')

def lambda_handler(event, context):
    print("Event received:", event)
    # If invoked by API Gateway with proxy integration
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        # Direct invoke (e.g., from Lambda console test)
        body = event

    #body = json.loads(event['body'])

    input_data = {
        "name": body['name'],
        "email": body['email'],
        "sms": body['sms'],
        "message": body['message'],
        "sendType": body['sendType']
    }

    response = sf.start_execution(
        stateMachineArn="arn:aws:states:us-east-1:751081874724:stateMachine:patient-reminder-step-function",
        input=json.dumps(input_data)
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"status": "Step Function Started", "executionArn": response['executionArn']})
    }