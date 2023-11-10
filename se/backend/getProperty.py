import json
import boto3

# Get the service resource and instantiate a table resource object
dydbTable = boto3.resource('dynamodb').Table('PropertyBasic')

def lambda_handler(event, context):
    try:
        property_id = event["queryStringParameters"]["pid"]
        dydbTable.delete_item(
            Key={
                "pid": property_id
            }
        )

        body = {"result": f"The property {property_id} is deleted"}
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps(body)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({"error": str(e)})
        }
