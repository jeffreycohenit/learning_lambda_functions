import json
import boto3

from datetime import datetime

def lambda_handler(event, context):
 
     now = datetime.now()
     data = now.strftime("%H:%M:%S %p")

     sqs = boto3.client('sqs')
 
     sqs.send_message(QueueUrl="https://sqs.us-east-1.amazonaws.com/442498226259/My-Project-Queue",MessageBody=data)
 
 
     return {
        'statusCode': 200,
        'body': json.dumps(data)
     }