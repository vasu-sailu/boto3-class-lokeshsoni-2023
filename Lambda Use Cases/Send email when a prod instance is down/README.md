# Send email when a prod instance is down

## Architecture Diagram

<img title="Architecture Diagram" alt="Architecture Diagram" src="./assets/Architecture%20Diagram.png">

## Steps

###  1. Create a lambda function
  - Give a function name
  - Select the runtime to be latest python

### 2. Add permissions to the function's role
  - click on the role under Configuration -> Permissions
  - Under IAM role, add an inline policy with the following permissions
  
  ```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "ec2:DescribeInstances",
            "Resource": "*"
        }
    ]
}
```

> This is added as minimum permissions required for the function. Can be also added through the visual builder in the policy console.

> Values under {} are to be replaced as per your environent

### 3. Add a trigger
- Under function, click on add trigger
- select Eventbridge and create a new rule following the below screenshot

<img title="Trigger Configuration" alt="Trigger Configuration" src="./assets/Trigger%20Configuration.png">

> We have added a trigger to check the instance status every 1 minute. You can set the schedule as per your use case.
