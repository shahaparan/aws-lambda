import os
import requests
import boto3

def lambda_handler(event, context):
    file_hour = event.get("filehour")
    file_name = f"{file_hour}.json.gz"
    file_content = requests.get(f'https://data.ghachreive.org/{file_name}').content

    bucket_name = os.environ.get("bucket_name")

    s3_client = boto3.client('s3')
    s3_client.put_object(
        Body=file_content,
        Bucket=bucket_name,
        Key=f'ghachrive/{file_name}'
    )
    return {
        'status_message': f'{file_name} successfully updated'
    }
