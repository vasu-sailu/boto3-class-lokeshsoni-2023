# Send email when a new report is uploaded to s3

## Architecture Diagram

<img title="Architecture Diagram" alt="Architecture Diagram" src="./assets/Architecture%20Diagram.png">

## Steps

### 1. Create a SNS Topic
- Under SNS console, create a topic
- Choose standard type
- Give a topic name
- Copy the topic arn

### 2. Add a subscriber
- Under the topic created, under subscriptions tab; click create subscription
- Choose protocol as Email
- Add your email in the Endpoint
- Once added, verify the subcription in your email

###  3. Create a lambda function
- Give a function name
- Select the runtime to be latest python

### 4. Add permissions to the function's role
- click on the role under Configuration -> Permissions
- Under IAM role, add an inline policy with the following permissions
  
```json
# S3 Permisions
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::{replace with your bucket name}/{replace with your folder name}"
    }
  ]
}

# SNS Permissions
{
  "Sid": "VisualEditor1",
  "Effect": "Allow",
  "Action": "sns:Publish",
  "Resource": "{replace with your topic arn}"
}
```

> This is added as minimum permissions required for the function. Can be also added through the visual builder in the policy console.

> Values under {} are to be replaced as per your environment

### 5. Add a trigger
- Under function, click on add trigger
- select S3 and create a new trigger following the below screenshot

<img title="Trigger Configuration" alt="Trigger Configuration" src="./assets/Trigger%20Configuration.png">

> We have added a trigger for any ".txt" file uploaded to the "reports/" folder in the s3 bucket. You can set the prefix and suffix as per your use case.
