import json 
import boto3 
import os

print("Initializing DynamoDB client")
dynamodb=boto3.client("dynamodb")
table_name=os.environ["DYNAMODB_TABLE_NAME"]

def updateuserdetails(event,context):
    print("Entered inside function.")
    body=json.loads(event["body"])
    print("Extracting user email and new full name from the Lambda event")
    user_email=body["user_email"]
    new_user_full_name=body["user_full_name"]
    try:
        if(user_email is None): # input validation 
            print("Wrong input by user")
            return{
                "statusCode": 400,
                "body": json.dumps("Please provide correct input")
            }
        print("Updating user details in DynamoDB Table")
        db_response=dynamodb.update_item (
            TableName=table_name,
            Key={
                "user_email": {"S": user_email}
            },
            UpdateExpression="SET user_full_name=:val",
            ExpressionAttributeValues= {
                ":val":{
                    "S":new_user_full_name
                    },
                },
            ReturnValues="UPDATED_NEW"
        )
        if (db_response is not None):
            updated_value=db_response["Attributes"]
            print("User details updated successfully!")
            return{
                "statusCode": 200,
                "body": updated_value
            }
    except Exception as e:
        print("Exception in retrieved user details")
        return {
            "statusCode": 500,
            "body": json.dumps(f'Error:{e}')
            }