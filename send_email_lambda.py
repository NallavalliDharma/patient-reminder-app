import json
import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    print("Event:", event)

    email = event['email']
    message = event['message']
    name = event['name']

    response = ses.send_email(
        Source='dharmanallavalli@gmail.com',  # Must be verified in SES
        Destination={'ToAddresses': [email]},
        Message={
            'Subject': {'Data': f'Reminder for {name}'},
            'Body': {
                'Text': {'Data': message}
            }
        }
    )

    return {"status": "Email sent", "ses_response": str(response)}