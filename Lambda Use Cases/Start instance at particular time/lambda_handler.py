import boto3
ec2 = boto3.client("ec2")

# INSTANCE_ID = "put your instance id here"
INSTANCE_ID = "i-07d311627f148bb11"


def lambda_handler(event, context):
	print(event)

	response = ec2.stop_instances(
		InstanceIds=[
			INSTANCE_ID
		]
	)

	print("instance is stopped")



import boto3
ec2 = boto3.client("ec2")

INSTANCE_ID = "put your instance id here"


def handler(event, context):
    print(event)
    
    response = ec2.describe_instances()
    reservations = response['Reservations']
    
    for reservation in reservations:
      instance_id = reservation['Instances'][0]['InstanceId']
    
      print(f"instance id is {instance_id}")
      
      # response = ec2.start_instances(
      #   InstanceIds=[
      #       instance_id
      #   ]
      # )
      
      # print("instance is started")
      
      response = ec2.stop_instances(
        InstanceIds=[
            instance_id
        ]
      )
      
      print("instance is stopped")
      print()
    