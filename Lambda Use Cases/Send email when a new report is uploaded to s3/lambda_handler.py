import boto3
s3 = boto3.client('s3')
sns = boto3.client('sns')

BUCKET_NAME = "replace with your bucket name"
TOPIC_ARN = "replace with your topic arn"


def lambda_handler(event, context):
    s3_key = event['Records'][0]['s3']['object']['key']
    file_name = s3_key.split("/")[-1]
    
    with open('/tmp/file_download.txt', 'wb') as fh:
        s3.download_fileobj(
            BUCKET_NAME, 
            s3_key, 
            fh
        )
        
    with open('/tmp/file_download.txt', "r") as fh:
        content = fh.read()
        message = f"Contents from the uploaded file is \n\n{content}"
        
        sns.publish(
            TopicArn=TOPIC_ARN,
            Message=message,
            Subject=f'New report uploaded at {file_name}',
        )
