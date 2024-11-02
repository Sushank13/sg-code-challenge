import json 
import boto3 
import os

print("Initializing DynamoDB client")
dynamodb=boto3.client("dynamodb")
table_name=os.environ["DYNAMODB_TABLE"]

def getuserdetails(event,context):
    print("Entered inside function.")
    body=json.loads(event["body"])
    print("Extracting user email from the Lambda event")
    user_email=body["user_email"]
    try:
        if(user_email is None): # input validation 
            print("Wrong input by user")
            return{
                "statusCode": 400,
                "body": json.dumps("Please provide correct input")
            }
        print("Fetching user details from DynamoDB Table")
        db_response=dynamodb.get_item(
            TableName=table_name,
            Key={
                "user_email": {"S": user_email}
            },
            ProjectionExpression="user_full_name"
        )
        if (db_response is not None):
            users=db_response["Item"]
            print("User details retrieved successfully!")
            return{
                "statusCode": 200,
                "body": users
            }
    except Exception as e:
        print("Exception in retrieved user details")
        return {
            "statusCode": 500,
            "body": json.dumps(f'Error:{e}')
            }