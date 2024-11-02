import json 
import boto3 
import os

print("Initializing DynamoDB client")
dynamodb=boto3.client("dynamodb")
table_name=os.environ["DYNAMODB_TABLE_NAME"]

def deleteuserdetails(event,context):
    print("Entered inside function.")
    print("Extracting user email from the Lambda event")
    user_email=event["user_email"]
    try:
        if(user_email is None): # input validation 
            print("Wrong input by user")
            return{
                "statusCode": 400,
                "body": json.dumps("Please provide correct input")
            }
        print("Deleting user details from DynamoDB Table")
        db_response=dynamodb.delete_item(
            TableName=table_name,
            Key={
                "user_email": {"S": user_email}
            }
        )
        if (db_response is not None):
            print("User details deleted successfully!")
            return{
                "statusCode": 200,
                "body": json.dumps("User details deleted successfully!")
            }
    except Exception as e:
        print("Exception in deleting user details")
        return {
            "statusCode": 500,
            "body": json.dumps(f'Error:{e}')
            }
        
    