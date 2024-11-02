import json 
import boto3 
import os

print("Initializing DynamoDB client")
dynamodb=boto3.client("dynamodb")
table_name=os.environ["DYNAMODB_TABLE"]

def adduserdetails(event,context):
    print("Entered inside function.")
    body=json.loads(event["body"])
    print("Parsing input data from the Lambda event")
    user_email=body["user_email"]
    user_full_name=body["user_full_name"]
    
    try:
        if(user_email is None or user_full_name is None): # input validation 
            print("Wrong input by user")
            return{
                "statusCode": 400,
                "body": json.dumps("Please provide correct input")
            }
        print("Inserting user details in DynamoDB Table")
        db_response=dynamodb.put_item(
            TableName=table_name,
            Item={
                "user_email": {"S": user_email},
                "user_full_name": {"S": user_full_name}
            }
        )
        if (db_response is not None):
            print("User details added successfully!")
            return{
                "statusCode": 200,
                "body": json.dumps("User details added successfully!")
            }
    except Exception as e:
        print("Exception in adding user details")
        return {
            "statusCode": 500,
            "body": json.dumps(f'Error:{e}')
            }
        
    