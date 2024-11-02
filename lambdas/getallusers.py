import json 
import boto3 
import os

print("Initializing DynamoDB client")
dynamodb=boto3.client("dynamodb")
table_name=os.environ["DYNAMODB_TABLE"]

def getallusers(event,context):
    print("Entered inside function.")
    try:
        print("Fetching all users from DynamoDB Table")
        db_response=dynamodb.scan(
            TableName=table_name
            )
        if (db_response is not None):
            users=db_response["Items"]
            print("User details retrieved successfully!")
            return{
                "statusCode": 200,
                "body": json.dumps(users)
            }
    except Exception as e:
        print("Exception in retrieved user details")
        return {
            "statusCode": 500,
            "body": json.dumps(f'Error:{e}')
            }