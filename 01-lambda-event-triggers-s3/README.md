# AWS Lambda Triggers or S3 Event Notifications

## Data Uploading to AWS S3 using AWS CLI

### Setup

1. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

2. Install boto3:
    ```bash
    pip install boto3
    
    ```

3. Set AWS profile:
    ```bash
    export AWS_PROFILE=<your_profile_name>
    ```

### S3 Operations

- List buckets:
    ```bash
    aws s3 ls
    ```

- Remove existing objects and folders in a bucket:
    ```bash
    aws s3 rm s3://{bucket_name} --recursive
    ```

- Remove a bucket:
    ```bash
    aws s3 rb s3://{bucket_name}
    ```

- Create a bucket:
    ```bash
    aws s3 mb s3://{bucket_name}
    ```

- Copy data to S3:
    ```bash
    aws s3 cp data s3://{bucket_name}/data --recursive
    ```

- List objects recursively:
    ```bash
    aws s3 ls s3://{bucket_name}/data --recursive
    ```

- List objects in a specific folder:
    ```bash
    aws s3 ls s3://{bucket_name}/data/
    ```

## Creating AWS Lambda Function for S3 Event Notifications

### Steps

1. Create Lambda function in AWS Lambda console.
2. Create an IAM role with `AWSS3FullAccessRole` policy attached for Lambda function.
3. Add S3 trigger to Lambda function:
    - Click on "Add trigger" in Lambda function configuration.
    - Select "S3" as trigger type.
    - Specify bucket name and event type (e.g., `put`).
    - Set prefix (e.g., `data/`) to trigger Lambda function for objects with this prefix.
    - Acknowledge trigger configuration to avoid recursive invocation issues.
    - Click "Add" to create trigger.

## CSV to JSON from S3 Bucket using Lambda Function

```python
import os 
import boto3
import json 

def lambda_handler(event, context):
    bucket_name = os.environ.get("BUCKET_NAME") # corrected typo in os.environ.get()
    file_key = event["Records"][0]["s3"]["object"]["key"]

    s3_client = boto3.client("s3")
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    content = response["Body"].read().decode('utf-8') # read the content and decode it as UTF-8

    # Split the content into records
    records = content.split("\n")
    json_records = []

    # Iterate over each record and create JSON
    for rec in records:
        rec_details = rec.split(",")
        json_record = {
            "order_id": int(rec_details[0]),
            "order_date": rec_details[1],
            "order_customer_id": int(rec_details[2])
        }
        json_records.append(json_record)

    # Convert JSON records to a JSON document string
    json_doc = json.dumps(json_records)

    # Upload the JSON document to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key="retails_json/orders/part-000.json",
        Body=json_doc.encode('utf-8')
    )
   
    # Optionally, return a response
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
