import boto3
ec2 = boto3.client("ec2")

INSTANCE_ID = "put your instance id here"


def lambda_handler(event, context):
	print(event)

	response = ec2.start_instances(
		InstanceIds=[
			INSTANCE_ID
		]
	)

	print("instance is started")
