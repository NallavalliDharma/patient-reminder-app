import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    print("Event:", event)

    phone = event['sms']
    message = event['message']

    response = sns.publish(
        PhoneNumber=f"+91{phone}",  # Change country code if needed
        Message=message
    )

    return {"status": "SMS sent", "sns_response": str(response)}