import boto3
ec2 = boto3.client("ec2")
sns = boto3.client('sns')

INSTANCE_ID = "replace with your instance id"
TOPIC_ARN = "replace with your topic arn"


def lambda_handler(event, context):
    response = ec2.describe_instances(
        InstanceIds=[
            INSTANCE_ID
        ]
    )
    
    instance_status = response['Reservations'][0]['Instances'][0]['State']['Name']
    
    if instance_status == "stopped":
        print("instance is stopped")
        print("send an email")
        
        response = sns.publish(
            TopicArn=TOPIC_ARN,
            Message=f'important instance stopped with the instance id {INSTANCE_ID}',
            Subject='PROD DOWN!!'
        )
        
        print("email sent")
        
    elif instance_status == "running":
        print("instance is running")
        print("do nothing")
        
    else:
        print(f"some other state: {instance_status}")
