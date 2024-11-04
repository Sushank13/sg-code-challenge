# Overview
This project implements a Serverless Cloud solution for creating REST APIs that support basic CRUD(Create, Read, Update and Delete) operations by utilizing AWS services: AWS Lambda for backend logic, AWS API Gateway for managing API calls and AWS DynamoDB as persistence storage. The AWS resources have been provisioned by using Infrastructure as a Code (IaC) called Serverless Framework. Lastly, a multi-stage deployment has been automated by making use of Github Actions for building a CI/CD pipeline.

# Architecture
Below is a simple and high level architecture of the serverless cloud solution being built.

![architecture](/architecture/architecture.jpg?raw=true)

The client sends any of the POST, PUT, GET or DELETE request. The request is routed by the API Gateway to the respective Lambda. The Lambda then interacts with the DynamoDB table to perform the operation. Finally, the response is sent back from the Lambda to the client via the API Gateway
# Structure
This repository has the following folder structure:
* `.github/workflows` directory contains the `deploy-main.yml` file that executes the multi-stage CI/CD pipeline when a new commit is pushed to the `main` branch.
* `api-testing-screenshots` directory has the screenshots of API testing using Postman.
* `architecture` directory has the screenshot of the simple and high level architecture of the serverless cloud solution.
* `cicd-screenshots` directory has the screenshots of CI/CD pipeline execution.
* `deployed-aws-resources` directory has the screenshots of the main deployed resources.
* `lambdas` directory contains 4 `.py` files which have the backend code for each of the CRUD operations. The code in these files will be deployed to AWS Lambda functions by Serverless Framework.
*  `serverless.yml` is the file in which the IaC is written for:
    1. 4 lambdas and their corresponding REST APIs
    2. DynamoDB table
    3. IAM role required by the Lambdas to access the DynamoDB table.
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

1. **Multi-Stage deployment visualization**
![multi-stage-deployment](/cicd-screenshots/1.multi-stage-deployment.png?raw=true)
2. **Deployment for Dev environment**
![deploy-on-dev](/cicd-screenshots/2.deploy-on-dev.png?raw=true)
3. **Deployment for Prod environment**
![deploy-on-prod](/cicd-screenshots/3.deploy-on-prod.png?raw=true)

The APIs provided in the output can be tested to perform the CRUD operations.

# Deployed Resources
After deployment, the main AWS resources would be as shown below:
1. **AWS Lambdas**
![lambdas](/deployed-aws-resources/lambdas-1.png?raw=true)

![lambdas](/deployed-aws-resources/lambdas-2.png?raw=true)
2. **AWS API Gateway**

**For Dev**
![dev-api](/deployed-aws-resources/dev-api.png?raw=true)

**For Prod**
![prod-api](/deployed-aws-resources/prod-api.png?raw=true)

3. **AWS DynamoDB**
![dynamodb-table](/deployed-aws-resources/dynamodb-table.png?raw=true)
# API Testing
The DynamoDB table has been configured with `user_email` as the primary key. This primary key attribute needs to be used while interacting with the DynamoDB table.
1. **POST (/adduserdetails)**
![post](/api-testing-screenshots/post.png?raw=true)

![post-dynamodb](/api-testing-screenshots/post-dynamodb.png?raw=true)

2. **PUT (/updateuserdetails)**
![put](/api-testing-screenshots/put.png?raw=true)

![post-dynamodb](/api-testing-screenshots/put-dynamodb.png?raw=true)
3. **GET (/getallusers)**
![get](/api-testing-screenshots/get.png?raw=true)
4. **DELETE (/deleteuserdetails)**
![delete](/api-testing-screenshots/delete.png?raw=true)

![delete-dynamodb](/api-testing-screenshots/delete-dynamodb.png?raw=true)

# References




