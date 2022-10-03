import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    countTable = dynamodb.Table('website-counter')
    
    response = countTable.scan()
    
    return {
    'statusCode': 200,
    'body': response['Items']
    }