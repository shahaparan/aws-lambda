## Setting Up Scheduled Event with AWS EventBridge
### AWS EventBridge Console:
- Access the AWS EventBridge console to manage rules and events.
- Navigate to the page displaying current rules.

### Creating a Rule:

- Click on "Create Rule" and name it `invoke ghactivity ingestor`.
- Choose the event bus as default and select the schedule for the rule.

### Defining Schedule:

- Set the schedule to run every 15th minute in every hour.
- Specify the schedule using the cron expression `*/15 * * * ?`.

### Target Configuration:

- Select the target type as AWS Service since we are configuring a Lambda function.
- Choose the type as Lambda Function and search for the function name `ghactivity ingestor`.
- Expand additional settings if needed, but usually not necessary for this setup.

### Review and Create Rule:

- Review the rule details, including the schedule, target type, and Lambda function name.
- Click on "Create Rule" to finalize the event bridge rule creation.

**Validation:**
- Ensure the schedule is set to trigger the Lambda function every 15 minutes as expected.


### validation and monitoring process for your AWS data pipeline after setting up scheduled events using AWS EventBridge.

1. **Monitoring Lambda Execution:**
   - Access the AWS Lambda console and monitor the execution of the Lambda functions (e.g., `ghactivity ingestor` and `ghactivity transformer`).
   - View logs in CloudWatch to verify if the Lambda functions are triggered according to the schedule.

2. **Verification of S3 Data:**
   - Use AWS CLI commands to list objects in the S3 buckets where data is ingested and transformed.
    - aws s3 https"//bucket/data --recursive 
   - Verify that new files are created in the S3 bucket, confirming successful data ingestion and transformation.



## 1. S3 Bucket Creation

### Set AWS profile:

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
  aws s3 mb s3://aws-glue-data/
  aws s3 mb s3://athenaqueries/
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

## 2. IAM Role Creation

- Create a new IAM role named "AWSGlueS3FullAccess" or use an existing one.
- Assign permissions for AWS Glue and full access to S3.

## 3. AWS Glue Crawler Setup

### Create a Crawler:

- Navigate to the AWS Glue Console and click on "Add Crawler."
- Provide the crawler name (e.g., "ghactivity").
- Data Store: Specify S3 as the data store.
- Path: Enter the S3 path where data is located (e.g., `s3://aws-glue/data`).
- IAM Role: Create a new IAM role or use an existing one for the crawler.
- Database: Choose an existing database or create a new one for the crawled data.

## 4. Running the Crawler

- Crawler Execution:
  - Run the created crawler immediately or set a schedule.
  - The crawler will process the data in the specified S3 location, infer its structure, and create tables in the designated database.

## 5. Athena Setup

### Setting Up Athena:

- Go to the Athena console and access the query editor.
- Configure the query result location in Amazon S3 for storing query results.
- Create a new S3 bucket, e.g., `aiathena-results`, and specify the path for query results (e.g., `s3://aiathena-results/query`).
- Enable full access for Athena in the bucket settings for Athena query results.


