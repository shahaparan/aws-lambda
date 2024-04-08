### Setup:

1. **Creating Directories and Installing Dependencies:**
    ```bash
    mkdir -p layers/layersdemo/python
    cd layers/layersdemo
    python3 -m pip install pandas -t python
    python3 -m pip install requests -t python
    ```

2. **Check Directory Contents:**
    ```bash
    ls -ltr
    du -sh python
    ```

3. **Create Zip File:**
    ```bash
    zip -r layerdemo.zip python
    ls -ltr layerdemo.zip
    unzip -t layerdemo.zip
    ```

4. **Upload Zip File to S3:**
    ```bash
    aws s3 cp layerdemo.zip s3://bucketname/layer/layerdemo.zip
    ```


1. Remove any existing `boto3` directory:
    ```bash
    rm -rf boto3
    ```

2. Create a new directory for the updated `boto3` version:
    ```bash
    mkdir -p boto3.1/python
    ```

3. Navigate into the `boto3.1` directory:
    ```bash
    cd boto3.1
    ```

4. Install `boto3` into the `python` directory within `boto3.1`:
    ```bash
    python3 -m pip install boto3 -t python
    ```

5. Check the contents of the directory:
    ```bash
    ls -ltr
    du -sh python
    ```

6. Create a zip file containing the `boto3` library:
    ```bash
    zip -r boto3.1.zip python
    ```

7. Check the contents of the directory and the zip file:
    ```bash
    ls -ltr boto3.1.zip
    unzip -t boto3.1.zip
    ```

### Steps:

1. **Create Lambda Function in AWS Lambda Console:**
    - Create a Lambda function in the AWS Lambda console.
    - Create an IAM role with the `AWSS3FullAccessRole` policy attached for the Lambda function.

2. **Configure Lambda Layers:**
    - Within the Lambda function settings, navigate to the "Layers" section.
    - Click on "Add a Layer" to add a custom layer.
    - Select the appropriate custom layer (in this case, "layer demo") and specify the version.
    - Click on "Add" to attach the layer to the Lambda function.

3. **Data Fetch from Online:**
    ```python
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
    ```

