
1. **Create a Dockerfile**: This file defines the environment for your Lambda function.
```Dockerfile
# Use the official AWS Lambda Python 3.8 image as the base image
FROM public.ecr.aws/lambda/python:3.8

# Copy the application code to the container
COPY . /var/task

# Set the CMD to your handler (adjust as needed)
CMD ["app.lambda_ingest"]
```

2. **Build the Docker image**: Run the following command in the directory containing your Dockerfile and application code.

```bash
docker build -t aws-data .
```

3. **Validate the Docker image**: Create a Docker container from the image and validate its contents.

```bash
docker run -d aws-data
docker exec -t <container_id> bash
ls -ltr
pwd
pip list
env
cd app
cat __init__.py
```

4. **Run the application using Python CLI in the Docker Container**: Execute your Lambda function within the Docker container.

```bash
python -c "import app;app.lambda_ingest(None,None)"
```

5. **Create AWS ECR Repository for Custom Docker Image**: Use the AWS CLI or AWS Management Console to create a repository in Amazon Elastic Container Registry (ECR) to store your Docker image.

6. **Create IAM roles for Lambda function**: Create IAM roles with the necessary permissions for your Lambda function to access resources like S3 and DynamoDB.

7. **Create AWS Lambda Function using Custom Docker Image in AWS ECR**:
   - Log in to the AWS Management Console and navigate to AWS Lambda.
   - Click "Create function", then select "Container image".
   - Provide a name for your function (e.g., "aws-data") and select the container image you pushed to ECR.
   - Configure the environment variables, memory, timeout, and other settings as needed.
   - Create the Lambda function.

8. **Create Shell Script to Build and Push Docker Image to AWS ECR**:

```bash
sh -x docker_build.sh
#!/bin/bashs

# Build Docker image
docker build -t aws-data .

# Login to AWS ECR
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com

# Tag Docker image
docker tag aws-data:latest <account-id>.dkr.ecr.<region>.amazonaws.com/aws-data:latest

# Push Docker image to ECR
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/aws-data:latest
```
