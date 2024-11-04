# Overview
This project implements a Serverless Cloud solution for creating REST APIs that support basic CRUD(Create, Read, Update and Delete) operations by utilizing AWS services such as AWS Lambda for backend logic, AWS API Gateway for managing API calls and AWS DynamoDB as persistence storage. The AWS resources have been provisioned by using Infrastructure as a Code (IaC) called Serverless Framework. Lastly, a multi-stage deployment has been automated by making use of Github Actions for building a CI/CD pipeline.

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
* `lambdas` directory contains 4 files which have the backend code for each of the CRUD operations. The code in these files will be deployed to AWS Lambda functions by Serverless Framework.
*  `serverless.yml` is the file in which the IaC is written for:
    1. 4 lambdas and their corresponding REST APIs
    2. DynamoDB table
    3. IAM role required by the Lambdas to access the DynamoDB table.
# Setup
1. Clone this repo on your local machine and then push this repo to a GitHub account owned by you or fork this repo.
2. You would need to have a Serverless Framework account. Once account is created, you would need to <a href= "https://www.serverless.com/framework/docs/guides/dashboard/cicd/running-in-your-own-cicd#create-an-access-key-in-the-serverless-framework-dashboard">create an Access Key in the Serverless Framework Dashboard</a> (**SERVERLESS_ACCESS_KEY**) and save it with you in a secure location.
3. You would also need to have an AWS account. Once account is created, you would need to create an IAM user with administrator access and <a href="https://docs.aws.amazon.com/cli/v1/userguide/cli-authentication-user.html">retrieve **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY**</a> for that user and secure it in a safe location. 
4. Go to your `GitHub repo-> Settings->Secrets and variables->Actions` and create three repository secrets: 
    1. SERVERLESS_ACCESS_KEY
    2. AWS_SECRET_ACCESS_KEY
    3. SERVERLESS_ACCESS_KEY and provide the corresponsing values you had saved in Step 2 and 3
5.  Go to your `GitHub repo-> Settings->Secrets and variables->Actions` and create repository variable: DEPLOYMENT_STAGE and provide either `dev` or `prod` values dependig on deplpyment stage you wish to have.
6. In the `serverless.yml` file, change the value of `org:`with the organization name you had kept while creating the Serverless Framework account in Step2. 

# Deployment
After the steup is completed, commit any changes and push them to the main branch. This will trigger the CI/CD pipeline:

1. **Deployment for Dev environment**
![deploy-on-dev](/cicd-screenshots/2.deploy-on-dev.png?raw=true)
2. **Deployment for Prod environment**
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
The following sources have been used for building this project:-
* **For Creating the Architecture Diagram**: https://app.diagrams.net/?splash=0&libs=aws4 
* **For Github Actions CI/CD**:
    * *Knowledge Base*: 
        1. https://www.youtube.com/watch?v=vNCNLhc7-6U&t=523s
        2. https://stackoverflow.com/questions/63148639/create-dependencies-between-jobs-in-github-actions
        3. https://www.serverless.com/framework/docs/guides/dashboard/cicd/running-in-your-own-cicd
        4. https://ianwhitestone.work/aws-serverless-deployments-with-github-actions/
        5. https://www.youtube.com/watch?v=KorJPUKvHKc&t=295s
        6. https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables
        7. https://www.youtube.com/watch?v=dPLPSaFqJmY
    * *YAML file*: https://github.com/serverless/github-action
* **For Testing APIs**: <a href="">Postman API Platform</a>
* **For Lambda Code**: 
    1. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-python.html
    2. https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/put_item.html
    3. https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/table/delete_item.html
    4. https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_item.html
    5. https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/scan.html
* **For Serverless Framework**:
    * *Knowledge Base*:
        1. https://www.youtube.com/watch?v=KQRGM9_eqIw
        2. https://www.youtube.com/playlist?list=PLmexTtcbIn_gP8bpsUsHfv-58KsKPsGEo
        3. https://www.serverless.com/framework/docs#philosophy
        4. https://www.youtube.com/playlist?list=PLL2hlSFBmWwzA7ut0KKYM6F8LKfu84-5c
    * *YAML File*: 
        1. https://medium.com/@ahmedSalem2020/building-a-serverless-rest-api-with-aws-lambda-api-gateway-dynamodb-and-serverless-framework-f3fb34395349
        2. https://github.com/serverless/examples/tree/v4/aws-python-rest-api-with-dynamodb






