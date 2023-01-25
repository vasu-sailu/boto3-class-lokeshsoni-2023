import boto3
ec2 = boto3.client("ec2")
sns = boto3.client('sns')

INSTANCE_ID = "i-07d311627f148bb11"
TOPIC_ARN = "arn:aws:sns:us-east-1:529310672444:instance-stop-notification"


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
            TopicArn='arn:aws:sns:us-east-1:529310672444:instance-stop-notification',
            Message=f'important instance stopped with the instance id {INSTANCE_ID}',
            Subject='PROD DOWN!!'
        )
        
        print("email sent")
        
    elif instance_status == "running":
        print("instance is running")
        print("do nothing")
        
    else:
        print(f"some other state: {instance_status}")