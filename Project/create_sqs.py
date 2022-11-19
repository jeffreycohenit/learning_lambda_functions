#Adding SDK library
import boto3

# Creating the connection to AWS
sqs = boto3.resource('sqs')

# Creating an SQS
queue = sqs.create_queue(
    QueueName='My-Project-Queue'
  )

# Printing results
print("Your new queue has been created!!")
print(queue.url)