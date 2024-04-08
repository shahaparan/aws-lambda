

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