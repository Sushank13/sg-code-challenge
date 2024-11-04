# Overview
This project implements a Serverless Cloud solution for creating REST APIs that support basic CRUD(Create, Read, Update and Delete) operations by utilizing AWS services: AWS Lambda for backend logic, AWS API Gateway for managing API calls and AWS DynamoDB as persistence storage. The AWS resources have been provisioned by using Infrastructure as a Code (IaC) called Serverless Framework. Lastly, a multi-stage deployment has been automated by making use of Github Actions for building a CI/CD pipeline.

# Structure
This repository has the following folder structure:
* `.github/workflows` directory contains the `deploy-main.yml` file that executes the multi-stage CI/CD pipeline when a new commit is pushed to the `main` branch.
* `lambdas` directory contains 4 `.py` files which have the backend code for each of the CRUD operations. The code in these files will be deployed to AWS Lambda functions by Serverless Framework.
*  `serverless.yml` is the file in which the IaC is written for:
    1. 4 lambdas and their corresponding REST APIs
    2. DynamoDB table
    3. IAM role required by the Lambdas to access the DynamoDB table.
* `cicd-screenshots` directory has the screenshots of CI/CD pipeline execution.
# Setup
1. Clone this repo on your local machine and then push this repo to a GitHub account owned by you.
2. You would need to have a Serverless Framework account. Once account is created, you would need to <a href= "https://www.serverless.com/framework/docs/guides/dashboard/cicd/running-in-your-own-cicd#create-an-access-key-in-the-serverless-framework-dashboard">create an Access Key in the Serverless Framework Dashboard</a> (**SERVERLESS_ACCESS_KEY**) and save it with you in a secure location.
3. You would also need to have an AWS account. Once account is created, you would need to create an IAM user with administrator access and <a href="https://docs.aws.amazon.com/cli/v1/userguide/cli-authentication-user.html">retrieve **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY**</a> for that user and secure it in a safe location. 
4. Go to your `GitHub repo-> Settings->Secrets and variables->Actions` and create three repository secrets: 
    1. SERVERLESS_ACCESS_KEY
    2. AWS_SECRET_ACCESS_KEY
    3. SERVERLESS_ACCESS_KEY and provide the corresponsing values you had saved in Step 2 and 3.
5. In the `serverless.yml` file, change the value of `org:`with the organization name you had kept while creating the Serverless Framework account in Step2. 

# Deployment
After the steup is completed, commit the changes and push them to the main branch. This will trigger the CI/CD pipeline:

1. Multi-Stage deployment visualization
![multi-stage-deployment](/cicd-screenshots/1.multi-stage-deployment.png?raw=true)
2. Deployment for Dev environment
![deploy-on-dev](/cicd-screenshots/2.deploy-on-dev.png?raw=true)
3. Deployment for Prod environment
![deploy-on-prod](/cicd-screenshots/3.deploy-on-prod.png?raw=true)

The APIs provided in the output can be tested to perform the CRUD operations.


